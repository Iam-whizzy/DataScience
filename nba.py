#importing pandas package
import pandas as pd

#making data frame from csv file
data = pd.read_csv("nba.csv")

#converting and overwriting values in column
data["Team"] = data ["Team"].str.upper()

#display
print(data)