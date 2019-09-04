import os
import pandas
import time

while True:
    if os.path.exists("birth.csv"):
        data=pandas.read_csv("birth.csv")
        df = pandas.DataFrame(data)
        print(df.loc[1::, ['Region', 'Count']])
    else:
        print("file doesn't exists.!")
    time.sleep(10)
