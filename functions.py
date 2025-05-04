import pandas as pd 

def verify_user(ic_number, password):
    input = ic_number.replace("-", "")
    if len(input) == 12 and ic_number[-4:] == password:
        return True
    else:
        return False