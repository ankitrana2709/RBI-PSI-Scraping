import pandas as pd

df = pd.read_html('https://rbi.org.in/Scripts/PSIUserView.aspx?Id=14')

#print(df[1]['column'])

print(df[1].dropna)
#print(df[2][1:])

#print(df[3][1:14])