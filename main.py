# Required Imports
import time
# import Actions
import MyCryptography
import db_helper

named_tuple = time.localtime()
time_string = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)

# User Logging in...
user = input("Enter your name:")
pwd = input("Enter password:")
result = db_helper.is_valid_user(user, pwd)
while True:
    if result == 1:
        print(
            "######################################################################################################################")
        print("Hola " + user + "!!!\t\t" + time_string + "\n")
        print("Enter 1 for encrypting file for the user \t\t\t\t\t\t"
              "Enter 2 for decrypting file you received\n"
              "Enter 3 for sending encrypted message to another user\t\t\t"
              "Enter 4 for reading encrypted messages received by you\n"
              "Enter 5 for adding a user\t\t\t\t\t\t\t\t\t\t"
              "Enter 6 change user\n"
              "Enter 7 to view contacts\t\t\t\t\t\t\t\t\t\t"
              "Enter 8 to to exit")
        print(
            "######################################################################################################################")

        x = int(input("Enter your action: "))

        if x == 1:
            receiver = str(input("Enter the receiver:"))
            filename = str(input("Enter the file to be encrypted:"))
            MyCryptography.encrypt_file(filename, receiver)
            print(filename + " has been encrypted successfully!!")

        elif x == 2:
            filename = str(input("Enter the file to be decrypted:"))
            MyCryptography.decrypt_file(filename, user)
            print(filename + " has been decrypted successfully!!")

        elif x == 3:
            receiver = str(input("Enter the receiver:"))
            message = str(input("Enter the message:"))
            MyCryptography.encrypt_message(message, receiver, user)
            print("Message has been successfully sent!")

        elif x == 4:
            MyCryptography.decrypt_all_messages(user)

        elif x == 5:
            username = input("Enter the user name you want to add: ")
            lastname = input("Enter the last name of the user:")
            # phone_number = int(input("Enter you Phone Number: "))
            # db_helper.add_phone_number_new_user(phone_number)
            # otp_ = MyCryptography.generate_otp(phone_number, 10)
            # otp_verification = int(input("Enter the OTP you have received: "))
            # if otp_verification == otp_:
            #     print("The OTP is valid...")
            password = input("Enter password:")
            db_helper.add_user(username, lastname, password)
            # else:
            #     print("<...Enter a valid OTP...>")

        elif x == 6:
            user = input("Enter user name:")
            pwd = input("Enter password:")
            result = db_helper.is_valid_user(user, pwd)
            if result == 1:
                print("User Changed !!!")
            else:
                print("Invalid user or password!!")

        elif x == 7:
            contacts = db_helper.users()
            for name in contacts:
                print(name[0], name[1])

        elif x == 8:
            print("See Ya Mi Amigo " + user + "!!!")
            break

    else:
        print("Invalid UserName or Password!!")

# MyCryptography.encrypt_file('Secret', 'Kevin')
# MyCryptography.encrypt_file('Secret', 'Jane')
# MyCryptography.encrypt_file('Secret', 'Jason')
# MyCryptography.encrypt_file('Secret', 'Sylvia')
# MyCryptography.encrypt_file('Secret', 'Preetha')

# MyCryptography.decrypt_file('Secret_Kevin_enc', 'Kevin')
# MyCryptography.decrypt_file('Secret_Preetha_enc', 'Preetha')

# MyCryptography.encrypt_message('hello world message3', 'Kevin', 'Prasanna')
# MyCryptography.encrypt_message('hello world message1', 'Kevin', 'Jane')
# MyCryptography.encrypt_message('this is a message to test something', 'Prasanna', 'Kevin')
# MyCryptography.encrypt_message('Hello People', 'Prasanna', 'Kevin')

# MyCryptography.decrypt_all_messages('Prasanna', 1)
# MyCryptography.decrypt_all_messages('Kevin', 1)
