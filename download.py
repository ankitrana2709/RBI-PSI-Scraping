import requests
from bs4 import BeautifulSoup
url = "https://rbidocs.rbi.org.in/rdocs/PSI/DOCs/PSIJULY2022E1AFE580359B43F8923AA54EBB4C9771.XLSX"
  
# URL of the xlsx to be downloaded is defined as url
r = requests.get(url) # create HTTP response object
  
# send a HTTP request to the server and save
# the HTTP response in a response object called f
with open("july.xlsx",'wb') as f:
  
    # Saving received content as a xlsx file
    f.write(r.content)