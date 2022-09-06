import pandas as pd


clean = 'out.xlsx'
main = pd.read_excel(clean)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 100)
#df.drop(df.index[0:7], inplace=True)

# for first sheet
df = main.iloc[7:50]
#print(df.head(100))
df = df.set_index(['Payment System Indicators'])    # changing index
df.columns =['PSI', 'Volume_inlakhs_FY_202122', 'Volume_inlakhs_2021_July', 'Volume_inlakhs_2022_June','Volume_inlakhs_2022_July',
            'Value_inCrore_FY_202122','Value_inCrore_2021_July','Value_inCrore_2022_June','Value_inCrore_2022_July']   # changing headers
df = df.drop(columns="PSI") # dropping PSI
df = df.dropna()        # dropping rows with null values
#print(df.head(100))
df.to_csv("PSI_System_Statistics.csv")

# For second Sheet
dff = main.iloc[56:72]
dff = dff.set_index(['Payment System Indicators'])
dff.columns =['PSI', 'Volume_inlakhs_FY_202122', 'Volume_inlakhs_2021_July', 'Volume_inlakhs_2022_June','Volume_inlakhs_2022_July',
            'Value_inCrore_FY_202122','Value_inCrore_2021_July','Value_inCrore_2022_June','Value_inCrore_2022_July']   # changing headers
dff = dff.drop(columns="PSI")
dff = dff.dropna()
#print(dff.head(100))
dff.to_csv("Payment_Modes_and_Channels.csv")

# third sheet
dfff = main.iloc[76:]

dfff = dfff.set_index(['Payment System Indicators'])
dfff.columns =['PSI', 'Volume_inlakhs_FY_202122', 'Volume_inlakhs_2021_July', 'Volume_inlakhs_2022_June','Volume_inlakhs_2022_July',
            'Value_inCrore_FY_202122','Value_inCrore_2021_July','Value_inCrore_2022_June','Value_inCrore_2022_July']   # changing headers
dfff.drop(['PSI','Value_inCrore_FY_202122','Value_inCrore_2021_July','Value_inCrore_2022_June','Value_inCrore_2022_July'], axis=1, inplace=True)

dfff = dfff.dropna()
dfff.to_csv("Payment_Infrastructures(lakh).csv")
#print(dfff.head(100))

with pd.ExcelWriter('cleaned_july.xlsx') as writer:     # Creating output in one file
    df.to_excel(writer, sheet_name='PSI System Statistics')
    dff.to_excel(writer, sheet_name='Payment Modes and Channels')
    dfff.to_excel(writer, sheet_name='Payment Infrastructures (lakh)')