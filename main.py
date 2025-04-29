from functions import save_to_csv

user_details = input("Enter name and IC number (comma-separated): ") # Isaac,031004101725
save_to_csv(user_details, "User-Details.csv")