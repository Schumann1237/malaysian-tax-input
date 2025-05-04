import pandas as pd
from functions import verify_user

def main():
    try:
        df = pd.read_csv("User-Details.csv")
    except FileNotFoundError:
        df = pd.DataFrame({"IC Number": [], "Password": [],"Income": [], "Tax Relief": [], "Tax Payable": []})
        df.to_csv("User-Details.csv", index=False)

    registryCheck = input("Are you a registered user? (Y/N): ")

    if registryCheck.upper() == "N":
        while True:
            print("USER REGISTRATION")
            user_ic = input("Enter IC Number to register: ")
            user_pass = input("Enter password to register (Last 4 digits of IC Number): ")
            if verify_user(user_ic, user_pass):
                break
            else:
                print("Invalid IC Number. Format accordingly \"012345678910\" or \"012345-67-8910\" \n")

        ic_df = pd.DataFrame({
            "IC Number": [user_ic],
            "Income": [""],
            "Tax Relief": [""],
            "Tax Payable": [""]
        })

        df = pd.concat([df, ic_df], ignore_index=True)
        df.to_csv("User-Details.csv", index=False)
    
    elif registryCheck.upper() == "Y":
        while True:
            print("USER LOGIN")
            user_ic = input("Enter IC Number: ")
            user_pass = input("Enter password: ")
            if verify_user(user_ic, user_pass):
                
                user_search = df[(df["IC Number"] == user_ic) & (df["Password"] == user_pass)]
                if user_search.empty:
                    print("User record not found. Please register.\n")
                    print("Exiting program\n")
                    return
                else:
                    print("User record found.")
                    break
            else:
                print("Invalid IC Number. Format accordingly \"012345678910\" or \"012345-67-8910\" \n")
            
    else:
        print("Invalid input. Exiting program.")

main()