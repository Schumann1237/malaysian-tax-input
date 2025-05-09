import pandas as pd

# Create an empty DataFrame with specified columns and data types
#df = pd.DataFrame(columns=["IC Number", "Password", "Income", "Tax Relief", "Tax Payable"])

#df = df.astype({
#    "IC Number": "string",
#    "Password": "string",
#    "Income": "Int64",
#    "Tax Relief": "Int64",
#    "Tax Payable": "Int64"
#})
#
## Loop to get IC Number and append to the DataFrame
#for i in range(6):
#    user_ic = input("Enter IC Number: ")
#    
#    # Create a new row with only IC Number filled in
#    new_row = pd.DataFrame([{
#        "IC Number": user_ic,
#        "Password": pd.NA,
#        "Income": pd.NA,
#        "Tax Relief": pd.NA,
#        "Tax Payable": pd.NA
#    }])
#    
#    # Ensure data types match and append to df
#    new_row = new_row.astype(df.dtypes.to_dict())
#    df = pd.concat([df, new_row], ignore_index=True)
#
#print(df)

def initialise_csv():
    try:
        df = pd.read_csv("User-Details.csv", dtype={
            "IC Number": "string",
            "Password": "string",
            "Income": "Int64",
            "Tax Relief": "Int64",
            "Tax Payable": "Int64"
        })

   
        return df
    except FileNotFoundError:
        df = pd.DataFrame(columns=["IC Number", "Password", "Income", "Tax Relief", "Tax Payable"])
        
        df = df.astype({
            "IC Number": "string",
            "Password": "string",
            "Income": "Int64",
            "Tax Relief": "Int64",
            "Tax Payable": "Int64"
        })

        df.to_csv("User-Details.csv", index=False)
   
        return df

def register_user(df):
    while True:
        print("USER REGISTRATION") 
        print("====================")
        print()
        user_ic = input("Enter IC Number to register: ").replace("-", "").strip()
        user_password = input("Enter password [last 4 digits of IC] to register: ")

        if verify_user(user_ic, user_password):
            print("Details verified.")            

            # Check if the user already exists
            user_search = df[(df["IC Number"] == user_ic) & (df["Password"] == user_password)]
            if user_search.empty:
                new_user = pd.DataFrame({
                    "IC Number": [user_ic],
                    "Password": [user_password],
                    "Income": [""],
                    "Tax Relief": [""],
                    "Tax Payable": [""]
                })

                # Append the new user to the dataframe
                df = pd.concat([df, new_user], ignore_index=True)

                # Save the dataframe back to CSV
                df.to_csv("User-Details.csv", index=False)
                print("Registration successful. Please login again.\n")
                
                return df
            else:
                print("User already exists.")
                return True
        else:
            print("Verification failed. Try again.")
            return False

def login_user(df):
    print("USER LOGIN")    
    print("===============")
    print()
    user_ic = input("IC Number: ").replace("-", "").strip()
    user_password = input("Password: ")

    user_search = df[(df["IC Number"] == user_ic) & (df["Password"] == user_password)]
    if user_search.empty:
        print("Error. User not found.")
        return False
    else:
        return user_ic 

def calculate_relief():
    total_relief = 0

    disabled_relief = input("Are you disabled [Y/N]: ")
    if disabled_relief == 'Y':
        total_relief += 6000

    print("1. Single")
    print("2. Married")
    print("3. Divorced / Widow / Widower")
    marital_status = int(input("Marital Status: "))
    child_status = input("Do you have children [Y/N]: ")

    if marital_status == 1:
        total_relief += 9000
    
    if marital_status == 2:
        total_relief += 9000

        spouse_disability = input("Is your wife/husband disabled [Y/N]: ")
        if spouse_disability == 'Y':
            total_relief += 5000
        
        spouse_employed = input("Is your wife/husband working [Y/N]: ")
        if spouse_employed == 'N':
            total_relief += 4000
        
        alimony_payment = int(input("Payment of alimony [amount] to former wife: "))
        total_relief += alimony_payment

        child_status = input("Do you have children [Y/N]: ")

    if marital_status == 3:
        while True:
            try:
                alimony_payment = int(input("Payment of alimony to former wife [RM0 - RM4000]: "))
                if 0 <= alimony_payment <= 4000:
                    break  # valid input
                else:
                    print("Error: Amount must be between 0 and 4000.")
            except ValueError:
                print("Error: Please enter a valid number.")

    if child_status == 'Y':
        below_eighten = int(input("Number of children (<18): "))
        a_level = int(input("Number of children (>18), A-Level: "))
        dip_above = int(input("Number of children (>18), diploma and above: "))

        total_relief += (below_eighten * 2000) + (a_level * 2000) + (dip_above * 8000)
        
        disabled_children = int(input("Number of disabled children: "))
        disabled_dipabove = int(input("Number of disabled children (>18), diploma and above: "))

        total_relief += (disabled_children * 6000) + (disabled_dipabove * 8000)

        while True:
            try:
                sspn_saving = int(input("Child education saving [RM0 - RM8000]: ")) 
                breast_equip = int(input("Breastfeeding equipment [RM0 - RM1000]: "))
                childcare_fees = int(input("Childcare centres and kindergarten fees [RM0 - RM3000]: "))
                if 0 <= sspn_saving <= 8000 and 0 <= breast_equip <= 1000 and 0 <= childcare_fees <= 3000:
                    break # valid input
                else:
                    print("Please enter the appropriate amount")
            except ValueError:
                print("Error. Please input a valid number.")

    while True:
        try:
            parent_medic = int(input("Parent Medical Fees [RM0 - RM8000]: ")) 
            if 0 <= parent_medic <= 8000:
                break
            else:
                print("Please enter appropriate amount.")
        except ValueError:
            print("Error. Please input a valid number.")

    while True:
        try:
            annuity_prs = int(input("Annuity Scheme Premium/Private Retirement Scheme [RM0 - RM3000]: "))
            if 0 <= annuity_prs <= 3000:
                break
            else:
                print("Please enter appropriate amount.") 
        except ValueError:
            print("Error. Please input a valid number.")

    while True:
        try:
            edu_medifees = int(input("Education & Medical Insurance (Self/Spouse/Child) [RM0 - RM3000]: "))
            if 0 <= edu_medifees <= 3000:
                break
            else:
                print("Please enter appropriate amount.")
        except ValueError:
            print("Error. Please input a valid number.")

    while True:
        try:
            edu_fees = int(input("Education Fees (Self) [RM0 - RM3000]: "))
            if 0 <= edu_fees <= 3000:
                break
            else:
                print("Please enter appropriate amount.")
        except ValueError:
            print("Error. Please input a valid number.")
    
    while True:
        try:
            supporting_equip = int(input("Supporting Equipment [RM0 - RM6000]: "))
            if 0 <= supporting_equip <= 6000:
                break
            else:
                print("Please enter appropriate amount.")
        except ValueError:
            print("Error. Please input a valid number.")
    
    while True:
        try:
            medical_expense = int(input("Medical Expenses (Self/Spouse/Child) [RM0 - RM10000]: "))
            if 0 <= medical_expense <= 10000:
                break
            else:
                print("Please enter appropriate amount.")
        except ValueError:
            print("Error. Please input a valid number.")
    
    while True:
        try:
            epf_kwsp = int(input("EPF/KWSP [RM0 - RM4000]: "))
            if 0 <= epf_kwsp <= 4000:
                break
            else:
                print("Please enter appropriate amount.")
        except ValueError:
            print("Error. Please input a valid number.")
    
    while True:
        try:
            takaful = int(input("Life Insurance/Family Takaful/Additional Voluntary Contribution to EPF [RM0 - RM3000]: "))
            if 0 <= takaful <= 3000:
                break
            else:
                print("Please enter appropriate amount.")
        except ValueError:
            print("Error. Please input a valid number.")
    
    while True:
        try:
            lifestyle = int(input("Lifestyle [RM0 - RM2500]: "))
            if 0 <= lifestyle <= 2500:
                break
            else:
                print("Please enter appropriate amount.")
        except ValueError:
            print("Error. Please input a valid number.")

    while True:
        try:
            equip_actvt = int(input("Sport Equipment & Activities (Self/Spouse/Child) [RM0 - RM1000]: "))
            if 0 <= equip_actvt <= 1000:
                break
            else:
                print("Please enter appropriate amount.")
        except ValueError:
            print("Error. Please input a valid number.")

    while True:
        try:
            socso_perkeso = int(input("SOCSO/PERKESO [RM0 - RM350]: "))
            if 0 <= socso_perkeso <= 350:
                break
            else:
                print("Please enter appropriate amount.")
        except ValueError:
            print("Error. Please input a valid number.")

    while True:
        try:
            ev_charging = int(input("Electrical Vehicle Charging Expenses [RM0 - RM2500]: "))
            if 0 <= ev_charging <= 2500:
                break
            else:
                print("Please enter appropriate amount.")
        except ValueError:
            print("Error. Please input a valid number.")

    pcb = int(input("PCB [amount]: "))
    zakat = int(input("Zakat [amount]: "))
    total_relief += zakat + pcb



    return total_relief

def calculate_tax(income):
    tax = 0
    brackets = [
        (5000, 0.00),
        (20000, 0.01),
        (25000, 0.03),
        (25000, 0.06),
        (50000, 0.11),
        (100000, 0.19),
        (250000, 0.25),
        (250000, 0.26),
        (500000, 0.28),
        (float('inf'), 0.30)
    ]

    remaining_income = income
    for bracket in brackets:
        amount, rate = bracket
        if remaining_income <= 0:
            break
        taxable = min(remaining_income, amount)
        tax += taxable * rate
        remaining_income -= taxable

    return int(round(tax))


def verify_user(user_ic, user_password):
    return len(user_ic) == 12 and user_ic[-4:] == user_password

def save_to_csv(user_ic, user_relief, user_tax, user_income, df):
    df.loc[df["IC Number"] == user_ic, "Tax Payable"] = user_tax
    df.loc[df["IC Number"] == user_ic, "Tax Relief"] = user_relief
    df.loc[df["IC Number"] == user_ic, "Income"] = user_income
    df.to_csv("User-Details.csv", index=False)

def read_from_csv(user_ic, df):
    matched_user = df[(df["IC Number"] == user_ic)]

    # Check and print
    if not matched_user.empty:
        print("User found:")
        print(matched_user.to_string(index=False))
    else:
        print("No matching user found.") 
