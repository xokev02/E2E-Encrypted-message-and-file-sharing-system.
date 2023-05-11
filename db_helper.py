import mysql.connector
from cryptography.fernet import Fernet


def is_valid_user(username, pwd):
    mydb = mysql.connector.connect(user='developer', password='K3vin@123',
                                   host='127.0.0.1',
                                   database='new_schema')

    my_cursor = mydb.cursor()

    my_cursor.execute("select count(1) from new_schema.users where userFName='" + username + "'")
    records = my_cursor.fetchall()

    count = 0
    for row in records:
        count = int(row[0])
        if count == 0:
            return 0
        else:
            my_cursor.execute("select * from new_schema.users where userFName='" + username + "'")
            record = my_cursor.fetchone()
            enc_Key = record[3]
            db_pwd = record[5]

            fernet = Fernet(enc_Key)
            dec_pwd = fernet.decrypt(db_pwd).decode()
            if pwd == dec_pwd:
                return 1
            else:
                return 0


def add_user(username, lastname, pwd):
    eKey = Fernet.generate_key()
    mydb = mysql.connector.connect(user='developer', password='K3vin@123',
                                   host='127.0.0.1',
                                   database='new_schema')

    my_cursor = mydb.cursor()

    fernet = Fernet(eKey)
    enc_pwd = fernet.encrypt(pwd.encode())

    sql = "INSERT INTO new_schema.users (userFName, userLName, EncKey, Password) VALUES (%s, %s, %s, %s)"
    val = (username, lastname, eKey, enc_pwd)
    print(val)
    my_cursor.execute(sql, val)
    mydb.commit()
    mydb.close()


def add_message_for_user(message: bytes, username, fromuser):
    mydb = mysql.connector.connect(user='developer', password='K3vin@123',
                                   host='127.0.0.1',
                                   database='new_schema')
    my_cursor = mydb.cursor()

    try:
        sql = "INSERT INTO `new_schema`.`messages` (`UserFName`, `Message`, `FromUser`) VALUES ('" + username + "', '" + message.decode() + "', '" + fromuser + "')"
        my_cursor.execute(sql)
        mydb.commit()
        mydb.close()
    except Exception as e:
        mydb.close()
        raise Exception(e)


def get_messages_for_user(username, include_old):
    if include_old == 0:
        print("Reading ALL messages for : " + username + "\n")
    else:
        print("Reading NEW messages for : " + username + "\n")
    mydb = mysql.connector.connect(user='developer', password='K3vin@123',
                                   host='127.0.0.1',
                                   database='new_schema')

    my_cursor = mydb.cursor()

    sql = ""
    if include_old == 0:
        sql = "select Message, FromUser, Received from new_schema.messages where userFName='" + username + "'"
    else:
        sql = "select Message, FromUser, Received from new_schema.messages where userFName='" + username + "' and Status=0"
    my_cursor.execute(sql)
    records = my_cursor.fetchall()

    sql = "update new_schema.messages set Status=1 where userFName='" + username + "'"
    my_cursor.execute(sql)
    mydb.commit()
    mydb.close()

    return records


def get_key_for_user(username):
    global key

    mydb = mysql.connector.connect(user='developer', password='K3vin@123',
                                   host='127.0.0.1',
                                   database='new_schema')
    my_cursor = mydb.cursor()

    my_cursor.execute("SELECT EncKey FROM new_schema.users where userFName='" + username + "'")

    records = my_cursor.fetchall()
    if len(records):
        for row in records:
            key = row[0]

    mydb.close()

    if key is None or len(key) == 0:
        key = Fernet.generate_key()

        mydb = mysql.connector.connect(user='developer', password='K3vin@123',
                                       host='127.0.0.1',
                                       database='new_schema')
        my_cursor = mydb.cursor()

        sql = "UPDATE new_schema.users SET EncKey = '" + key.decode() + "' WHERE UserFName = '" + username + "'"
        my_cursor.execute(sql)
        mydb.commit()
        mydb.close()
        return key.decode()
    else:
        return key


def lname(userFname):
    mydb = mysql.connector.connect(user='developer', password='K3vin@123',
                                   host='127.0.0.1',
                                   database='new_schema')

    my_cursor = mydb.cursor()
    query = "SELECT userLname FROM users WHERE userFname = %s;"
    my_cursor.execute(query, userFname)
    record = my_cursor.fetchone()
    mydb.close()
    return record

def users():
        mydb = mysql.connector.connect(user='developer', password='K3vin@123',
                                       host='127.0.0.1',
                                       database='new_schema')

        my_cursor = mydb.cursor()
        query = 'SELECT userFname, userLname FROM users'
        my_cursor.execute(query)
        record = my_cursor.fetchall()
        mydb.close()
        return record



    # def add_phone_number_existing_users(username, lastname, phonenumber):
    #     mydb = mysql.connector.connect(user='developer', password='K3vin@123',
    #                                    host='127.0.0.1',
    #                                    database='new_schema')
    #     my_cursor = mydb.cursor()
    #     query = "INSERT INTO new_schema.users (userFname, userLName, phonenumber) VALUES (%s, %s, %s)"
    #     val = (username, lastname, phonenumber)
    #     print(val)
    #     my_cursor.execute(query, val)
    #     mydb.commit()
    #     mydb.close()

    # def add_phone_number_new_user(phonenumber):
    #     mydb = mysql.connector.connect(user='developer', password='K3vin@123',
    #                                    host='127.0.0.1',
    #                                    database='new_schema')
    #     my_cursor = mydb.cursor()
    #     query = "INSERT INTO phone_numbers (phone_number) VALUES (%s)"
    #     val = phonenumber
    #     my_cursor.execute(query, val)
    #     mydb.commit()
    #     mydb.close()
