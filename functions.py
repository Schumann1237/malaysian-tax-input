import pandas as pd 

def verify_user(ic_number, password):
    input = ic_number.replace("-", "")
    if len(input) == 12 and ic_number[-4:] == password:
        return True
    else:
        return False

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

def register_user(df):
    print("\nRegistration\n")
    while True:
        user_ic = input("Enter IC Number to register: ")
        user_pass = input("Enter password to register: ")
        if verify_user(user_ic):
            new_user = pd.DataFrame({
                "IC Number": [user_ic],
                "Password": [user_pass],
                "Income": [""],
                "Tax Relief": [""],
                "Tax Payable": [""]
            })
            df = pd.concat([df, new_user], ignore_index=True)
            df.to_csv("User-Details.csv", index=False)
            print("Registration successful.\n")
            break
        else:
            print("Invalid IC Number. Format accordingly \"012345678910\" or \"012345-67-8910\"\n")

def login_user(df):
    print("\nLogin\n")
    while True:
        user_ic = input("Enter IC Number: ")
        user_pass = input("Enter password: ")
        if verify_user(user_ic):
            user_search = df[(df["IC Number"] == user_ic) & (df["Password"] == user_pass)]
            if user_search.empty:
                print("User record not found. Please register.\nExiting program.\n")
                return False
            else:
                print("Login successful.\n")
                return True
        else:
            print("Invalid IC Number. Format accordingly \"012345678910\" or \"012345-67-8910\"\n")

