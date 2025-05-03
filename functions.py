import pandas as pd 

def verify_user(ic_number):
    input = ic_number.replace("-", "")
    if len(input) == 12:
        return True
    else:
        return False