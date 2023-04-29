import time
import main
import MyCryptography
import db_helper

named_tuple = time.localtime()
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
User = main.user
Pwd = main.pwd


def actions(User, Pwd):
    result = db_helper.is_valid_user(User, Pwd)
    if result != 0:
        print(
            "######################################################################################################################")
        print("Hola " + User + "!!!\t\t" + time_string)
        print("Enter 1 for encrypting file for the user \t\t\t\t\t\t"
              "Enter 2 for decrypting file you received\n"
              "Enter 3 for sending encrypted message to another user\t\t\t"
              "Enter 4 for reading encrypted messages received by you\n"
              "Enter 5 for changing user\t\t\t\t\t\t\t\t\t\t"
              "Enter 6 for adding a user\n"
              "Enter 7 to exit")
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
            MyCryptography.decrypt_file(filename, User)
            print(filename + " has been decrypted successfully!!")

        elif x == 3:
            receiver = str(input("Enter the receiver:"))
            message = str(input("Enter the message:"))
            MyCryptography.encrypt_message(message, receiver, User)
            print("Message has been successfully sent!")

        elif x == 4:
            MyCryptography.decrypt_all_messages(User)

        elif x == 5:
            Result = 0
            while Result == 0:
                user = input("Enter user name:")
                pwd = input("Enter password:")
                Result = db_helper.is_valid_user(User, Pwd)
                if Result == 1:
                    actions(User, Pwd)
                else:
                    print("Invalid user or password!!")
                    exit()

        elif x == 6:
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

        elif x == 7:
            print("See Ya Mi Amigo " + User + "!!!")

    else:
        print("Invalid UserName or Password!!")
