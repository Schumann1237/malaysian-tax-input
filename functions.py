import pandas as pd

def initialize_csv():
    try:
        return pd.read_csv("User-Details.csv", dtype={"IC Number": str, "Password": str})
    except FileNotFoundError:
        df = pd.DataFrame({
            "IC Number": [], #STRING
            "Password": [], #STRING
            "Income": [],
            "Tax Relief": [],
            "Tax Payable": []
        })
        df["IC Number"] = df["IC Number"].astype(str)
        df["Password"] = df["Password"].astype(str)
        df.to_csv("User-Details.csv", index=False)

        return df

def verify_user(user_ic, user_pass):
    return len(user_ic) == 12 and user_ic[-4:] == user_pass

def register_user():
    print("USER REGISTER")
    print("=================")
    ic_num = input("\nEnter IC Number to register: ").strip()
    user_ic = ic_num.replace("-", "")
    user_pass = input("Enter password (last 4 digits of IC) to register: ").strip()

    if verify_user(user_ic, user_pass):
        print("Details verified.")
        df = pd.read_csv("User-Details.csv")
        df["IC Number"] = df["IC Number"].astype(str)
        df["Password"] = df["Password"].astype(str)

        user_search = df[(df["IC Number"] == user_ic) & (df["Password"] == user_pass)]
        if user_search.empty:
            new_user = pd.DataFrame({
                "IC Number": pd.Series([user_ic], dtype="str"),
                "Password": pd.Series([user_pass], dtype="str"),
                "Income": pd.Series([""], dtype="int"),
                "Tax Relief": pd.Series([""], dtype="int"),
                "Tax Payable": pd.Series([""], dtype="int")
            })

            df = pd.concat([df, new_user], ignore_index=True)
            df.to_csv("User-Details.csv", index=False)
            print("Registration successful. Please login again.\n")
            return True
        else:
            print("Error. User already exists.")
            return False
    else:
        print("Verification failed.")
        return False

def calculate_tax():
    print("Function start")

def login_user():
    ic_num = input("\nEnter IC Number: ").strip()
    user_ic = ic_num.replace("-", "")
    user_pass = input("Enter password: ").strip()

    df = pd.read_csv("User-Details.csv", dtype={"IC Number": str, "Password": str})

    df["IC Number"] = df["IC Number"].str.strip()
    df["Password"] = df["Password"].str.strip()

    user_search = df[(df["IC Number"] == user_ic) & (df["Password"] == user_pass)]
    if user_search.empty:
        print("Error. User not registered.")
        return False
    else:
        print("Login successful.")
        return True

