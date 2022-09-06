import psycopg2
import pandas as pd
#conn=mysql.connect(host='localhost', passwd='pass1234', user='root')

#db = SQL("sqlite:///test.db")
"""if conn.is_connected:
    print("connected")

cur=conn.cursor()

cur.execute("create table rbi(PSI varchar(50), Volume_inlakh_FY_202122 decimal, Volume_inlakh_2021_July decimal, Volume_inlakh_2022_June decimal,Volume_inlakh_2022_July decimal, Value_in_cr_FY_202122 decimal,Value_in_cr_2021_July decimal,Value_in_cr_2022_June decimal,Value_in_cr_2022_July decimal)")

conn.close()"""
cur= None
conn = None
try:
    conn = psycopg2.connect("postgres://vwpkaplfstsyet:a18fac716920660cc193273388c4a0b730573307377c86e50afac2642e3a842c@ec2-107-23-76-12.compute-1.amazonaws.com:5432/d83pvmb3c63v2c")
    print("Connected")

    cur = conn.cursor()
    df = pd.read_csv("PSI_System_Statistics.csv")
    #print(df.columns)

    cur.execute("CREATE TABLE PSI (Payment_System_Indicators varchar(150), Volume_inlakhs_FY_202122 decimal, Volume_inlakhs_2021_July decimal, Volume_inlakhs_2022_June decimal, Volume_inlakhs_2022_July decimal, Value_inCrore_FY_202122 decimal, Value_inCrore_2021_July decimal, Value_inCrore_2022_June decimal, Value_inCrore_2022_July decimal)")
    # Changed column names accordig to required)
    df.columns =['PSI', 'Volume_inlakhs_FY_202122', 'Volume_inlakhs_2021_July', 'Volume_inlakhs_2022_June','Volume_inlakhs_2022_July',
            'Value_inCrore_FY_202122','Value_inCrore_2021_July','Value_inCrore_2022_June','Value_inCrore_2022_July']   # changing headers
    
    for row in df.itertuples():
        print(row.Volume_inlakhs_2021_July, row.Volume_inlakhs_2022_June, row.Volume_inlakhs_2022_July, row.Value_inCrore_FY_202122, row.Value_inCrore_2021_July, row.Value_inCrore_2022_June, row.Value_inCrore_2022_July)
        cur.execute(" INSERT INTO PSI (Payment_System_Indicators, Volume_inlakhs_FY_202122, Volume_inlakhs_2021_July, Volume_inlakhs_2022_June, Volume_inlakhs_2022_July, Value_inCrore_FY_202122, Value_inCrore_2021_July, Value_inCrore_2022_June, Value_inCrore_2022_July) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);",
         ([row.PSI, row.Volume_inlakhs_FY_202122, row.Volume_inlakhs_2021_July, row.Volume_inlakhs_2022_June, row.Volume_inlakhs_2022_July, row.Value_inCrore_FY_202122, row.Value_inCrore_2021_July, row.Value_inCrore_2022_June, row.Value_inCrore_2022_July]))
    conn.commit()
    print("DONE!")
    
except Exception as error:
   print("Wrong credential")

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()