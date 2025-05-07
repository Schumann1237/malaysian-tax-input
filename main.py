from functions import *

def main():
    #* initialize the csv file if not found
    initialize_csv()

    while True:
        print("MAIN MENU")
        print("===============")
        print("\n 1. Register")
        print("2. Login")
        print("3. Exit Program")

        procedure = int(input("Insert Operation: "))
        if procedure == 1:
            register_user()
        elif procedure == 2:
            login_user()