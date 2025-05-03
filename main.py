import pandas as pd
from functions import verify_user

def main():
    try:
        df = pd.read_csv("User-Details.csv")
    except FileNotFoundError:
        df = pd.DataFrame({"IC Number": [], "Income": [], "Tax Relief": [], "Tax Payable": []})
        df.to_csv("User-Details.csv", index=False)

    registryCheck = input("Are you a registered user? (Y/N): ")

    if registryCheck.upper() == "N":
        while True:
            ic_number = input("Enter your IC Number to register: ")
            if verify_user(ic_number):
                break
            else:
                print("Invalid IC Number. Format accordingly \"012345678910\" or \"012345-67-8910\" \n")

        ic_df = pd.DataFrame({
            "IC Number": [ic_number],
            "Income": [""],
            "Tax Relief": [""],
            "Tax Payable": [""]
        })

        df = pd.concat([df, ic_df], ignore_index=True)
        df.to_csv("User-Details.csv", index=False)
    
    elif registryCheck.upper() == "Y":
         while True:
            ic_number = input("Enter your IC Number: ")
            if verify_user(ic_number):
                break
            else:
                print("Invalid IC Number. Format accordingly \"012345678910\" or \"012345-67-8910\" \n")


main()