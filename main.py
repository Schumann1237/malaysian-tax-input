from functions import *

def main():
    #* initialize the csv file if not found
    initialize_csv()

    while True:
        print("MAIN MENU")
        print("===============")
        print("\n1. Register")
        print("2. Login")
        print("3. Exit Program")

        procedure = int(input("Insert Operation: "))
        if procedure == 1:
            # User already exist OR Verification failed
            if not register_user():
                break
            else:
                if not login_user():
                    break
                else:
                    calculate_tax()
        elif procedure == 2:
            if not login_user():
                break
            else:
                calculate_tax() 
                
main()