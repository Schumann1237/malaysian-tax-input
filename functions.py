import os.path
import csv

def save_to_csv(data, filename):
    try:
        with open(filename, 'r') as fp:
            user_data = csv.DictReader(fp)

        print(f"{filename} exists.")

    except FileNotFoundError:
        print(f"{filename} does not exist.")

        #with open(filename, 'w', newline='') as fp:
        #    fieldname = ["Name", "IC Number"]
        #    new_csv = csv.DictWriter(fp, fieldnames=fieldname, delimiter=",")
        #    new_csv.writeheader()
#
#            for input in data:
#                name,ic_num = input.split(',')
#                new_csv.writerow({'Name': name.split(), 'IC Number': ic_num.split()})
        


            
