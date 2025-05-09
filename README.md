# Malaysia Income Tax Estimator (CLI)

This command-line tool estimates Malaysian annual income tax based on your personal profile. It allows users to register, log in, input income and eligible tax reliefs, and then calculates tax payable based on LHDN Malaysia's tax brackets. Data is stored in a CSV file for record keeping.

---

## 📁 Files

- **`main.py`** — Entry point of the program.
- **`functions.py`** — Contains core functions: register, login, tax estimation, and data handling.
- **`User-Details.csv`** — Stores user information and tax results.
- **`autorun.cmd`** - Automates the process of running the program

---

## 🚀 Getting Started

### 1. Requirements

- Python 3.9 or above
- `pandas` module

Install pandas:

```bash
pip install pandas
```
### 2. Running the program

- run the **`autorun.cmd`** file

## 🧭 How to Use
When the program starts, the program will prompt the main menu

```python
MAIN MENU
===============
1. Register
2. Login
3. View Tax Record
4. Exit Program
```
Option 1: Register

- Enter your IC number (e.g., 991212076543).

- Password will be the last 4 digits of your IC.

- This info is stored in User-Details.csv.

Option 2: Login

-   Log in using your IC and password.

-   Input your annual income.

-   Answer a series of yes/no questions and provide numerical inputs for:

-    Personal disability

-    Marital status

-    Number of children (and disabilities if any)

-    Education, insurance, lifestyle expenses, etc.

-    The program calculates:

-   Total tax relief

-   Chargeable income

-   Tax payable

    Results are saved in **`User-Details.csv`**

Option 3: View Tax Record

After logging in, you can view your stored:

-   Total income

-   Tax relief

-   Tax payable

Option 4: Exit

Exit the application cleanly.

## 🧮 How is Tax Calculated?

The program uses the 2024 LHDN progressive tax brackets to compute tax:

| Chargeable Income (RM) | Tax Rate | Tax Amount (RM) |
| ---------------------- | -------- | --------------- |
| 0 – 5,000              | 0%       | 0               |
| 5,001 – 20,000         | 1%       | 150             |
| 20,001 – 35,000        | 3%       | 450             |
| 35,001 – 50,000        | 8%       | 1,200           |
| 50,001 – 70,000        | 13%      | 2,600           |
| 70,001 – 100,000       | 21%      | 6,300           |
| 100,001 – 250,000      | 24%      | 36,000          |
| 250,001 – 400,000      | 24.5%    | 36,750          |
| 400,001 – 600,000      | 25%      | 50,000          |
| 600,001 – 2,000,000    | 26%      | 364,000         |
| 2,000,001+             | 28%      | *Varies*        |

Deductions include:

-   Personal: RM9,000

-   Spouse: RM4,000

-   Child: RM2,000–RM6,000

-   EPF, SOCSO, education, medical, insurance, etc.

## ⚠️ DISCLAIMER
- Pasword is stored as plain text — this app is meant for learning/demo purposes only.

- No encryption or database — only basic CSV storage.

## 👨‍💻 Author
Developed by:
**Isaac Yang Hao Tung**
**(299825)**