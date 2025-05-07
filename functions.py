import pandas as pd

def initialize_csv():
    try:
        return pd.read_csv("User-Details.csv")
    except FileNotFoundError:
        df = pd.DataFrame({
            "IC Number": [],
            "Password": [],
            "Income": [],
            "Tax Relief": [],
            "Tax Payable": []
        })
        df.to_csv("User-Details.csv", index=False)
        return df

def register_user():
    print("USER REGISTER")
    print("=================")
    user_ic = input("\nEnter IC Number to register: ").replace("-", "")
    user_pass = input("Enter password (last 4 digits of IC) to register: ")

    verify_user(user_ic, user_pass)
    if verify_user:
       df = pd.read_csv("User-Details.csv")




def verify_user(user_ic, user_pass):
    if len(user_ic) == 12:

        if user_pass[12:7:-1] == user_ic:
            return True
    else:
        return False