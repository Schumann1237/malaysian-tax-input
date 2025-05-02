# SQIT 3073: Business Analytic Programming Individual Project -  10% Marks


## Tasks:

In this assignment, you will create a Malaysian Tax Input Program using Python. The program will consist of two files: main.py and functions.py. The main.py file will contain the main program logic, while the functions.py file will contain the necessary functions for the program

## Objectives
Implement user registration and authentication using IC (Identity Card) numbers as passwords.
Calculate the tax payable based on the user's annual income and tax relief amount.
Store the user's data (Id, Password using IC number, income, tax relief, and tax payable) in a CSV file.

### Requirements
- Use variables such as strings, numbers, lists, tuples, sets, and dictionaries to store and manipulate data.
- Implement loops (e.g., while loops) for user input validation or other purposes.
Define and use at least one user-defined function in the functions.py file.
- Utilise the pandas library for CSV file operations.

### Tax Calculation Inputs and Available Tax Reliefs
The main inputs needed for tax calculation in Malaysia are:
1. Annual income or employment income
2. Tax relief amounts

#### The key tax reliefs available in Malaysia include:
- Individual tax relief: RM9,000 for resident individual taxpayers.
- Spouse relief: RM4,000 for a resident spouse who has no income or has an income of up to RM4,000 per year.
- Child relief: RM8,000 for each child up to a maximum of 12 children.
- Medical expenses relief: Up to RM8,000 for serious medical treatment expenses for self, spouse, or child.
- Lifestyle relief: Up to RM2,500 for purchases of reading materials, sports equipment, computer, smartphone, internet subscription, etc.
- Education fees relief: Up to RM7,000 for course fees at recognized institutions.
- Parental care relief: Up to RM5,000 for parents.

Additionally, there are other tax reliefs available for disabled individuals, purchase of breastfeeding equipment, purchase of sports equipment, purchase of books, insurance premiums, and more. The specific relief amounts may vary based on the taxpayer's circumstances and are subject to annual revisions by the Inland Revenue Board of Malaysia.

## Tasks
1. Create a main.py file with the following functionality:
    - If not registered. Prompt the user to enter their id, IC number as password for registration. Prompt again password (last 4 digits of their IC) to enter the program. Else if registered, Prompt user id and password (last 4 digits of their IC)
    - Verify the user's credentials using a function from functions.py.If the credentials are valid, prompt the user to enter their annual income and tax relief amount.
    - Calculate the tax payable using a function from functions.py.
    - Display the calculated tax payable to the user.
    - Store the user's data (IC number, income, tax relief, and tax payable) in a CSV file using a function from functions.py. 
    - Ability to read data from the CSV file and display the tax records.


2. Create a functions.py file with the following functions:
    - **verify_user**(ic_number, password): Verify the user's credentials by checking if the IC number is 12 digits long and if the password matches the last 4 digits of the IC number
    - **calculate_tax**(income, tax_relief): Calculate the tax payable based on the Malaysian tax rates for the current year
    - **save_to_csv**(data, filename): Save the user's data (IC number, income, tax relief, and tax payable) to a CSV file. If the file doesn't exist, create a new file with a header row. If the file exists, append the new data to the existing file 
    - **file.read_from_csv**(filename): Read data from the CSV file and return a pandas DataFrame containing the data. If the file doesn't exist, return None.

3. Ensure that the program follows best practices for code organisation, readability, and maintainability.
4. Test your program with various input scenarios to ensure it works as expected.

### Submission
Submit your assignment by uploading the main.py and functions.py files to the designated submission platform or as instructed by your instructor.

### Evaluation Criteria
Your assignment will be evaluated based on the following criteria:

- Correctness: The program should accurately calculate the tax payable and store the data in the CSV file.
- Code organisation and readability: The code should be well-organised, with proper indentation, comments, and meaningful variable names.
- Functionality: The program should meet all the requirements listed in the "Tasks" section and additional functions if required.
- Error handling: The program should handle invalid user inputs and other potential errors gracefully.
- Documentation: The code should include appropriate comments and docstrings to explain the purpose and functionality of the functions and variables.
 
#### Deliverables

- Brief Technical Manual Report (Introduction,Objective, Background, Methodology/Workflow, Initial setup and configuration, Basic Operations, Troubleshooting and FAQs, References) (Not more than 10 pages)
  - Detail Methodology/Workflow using flow-chart ( https://www.drawio.com )
  - Link to Python Source Code in Github

###### Submission Date 	: 08 May 2025 


