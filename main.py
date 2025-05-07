import pandas as pd
from functions import * 

def main():
    df = initialize_csv()

    registry_check = input("Are you a registered user? (Y/N): ").strip().upper()

    if registry_check == "N":
        register_user(df)
    elif registry_check == "Y":
        if not login_user(df):
            return
    else:
        print("Invalid input. Exiting program.")

main()
