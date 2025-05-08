import pandas as pd
def debug_csv():
    df = pd.read_csv("test-details.csv")

    print("\n[DEBUG] Raw data:")
    print(df)

    print("\n[DEBUG] Dtypes:")
    print(df.dtypes)

    print("\n[DEBUG] Values with repr:")
    for index, row in df.iterrows():
        print(f"Row {index}: IC={repr(row['IC Number'])}, Password={repr(row['Password'])}")

debug_csv()