import os
import pandas as pd

if __name__ == '__main__':
    path = "./data"
    files = [file for file in os.listdir(path) if not file.startswith('.')] # Ignore hidden files

    monthsData = pd.DataFrame()
    newCsv = 'sales_data.csv'

    for file in files:
        print(f"{file} merged with {newCsv}")
        currentData = pd.read_csv(path + "/" + file)
        monthsData = pd.concat([monthsData, currentData])
    
    monthsData.to_csv("sales_data.csv", index=False)
    print(f"\n{newCsv} created successfully.\n")