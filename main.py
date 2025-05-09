from functions import *

def main():
    df = initialise_csv()

    while True:
        print("MAIN MENU")
        print("1. Register")
        print("2. Login")
        print("3. View Tax Record")
        print("4. Exit Program")

        try:
            procedure = int(input("Select an option: "))
            if procedure == 1:
                if not register_user(df):
                    print("Registration failed.")
            elif procedure == 2:
                df = initialise_csv()
                user_ic = login_user(df)
                if user_ic:
                    user_income = int(input("Total Annual Income: "))
                    tax_relief = calculate_relief()
                    taxable_income = user_income - tax_relief
                    user_tax = calculate_tax(taxable_income)
                    save_to_csv(user_ic, tax_relief, user_tax, user_income, df)
            elif procedure == 3:
                user_ic = login_user(df)
                if user_ic:
                    read_from_csv(user_ic, df)
            elif procedure == 4:
                print("Exiting program...")
                break
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print()

main()