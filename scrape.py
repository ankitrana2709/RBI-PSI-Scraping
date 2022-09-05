def pinpoint():
    import requests
    from bs4 import BeautifulSoup

    DOMAIN = 'https://rbi.org.in/Scripts/PSIUserView.aspx'
    # seeked permission
    data = requests.get(DOMAIN)
    # parse the HTML
    soup = BeautifulSoup(data.text, 'html.parser')
    # pin point your need table> a> href> link
    table = soup.find('table', class_='tablebg')
    for links in table.find_all('a'):
        global link
        link = links.get('href')
        if link[0:3] == "PSI":
            pass
        else:
            #print(link)
            break
    print(link)
    # pinpointed our stuff. ------ reached a checkpoint.

    # URL of the xlsx to be downloaded is defined as url
    r = requests.get(link) # create HTTP response object
    
    # send a HTTP request to the server and save
    # the HTTP response in a response object called f
    with open("out.xlsx",'wb') as f:
    
        # Saving received content as a xlsx file
        f.write(r.content)
    # Checkpoint 2 reached
    # We were able to download the latest file using above code. --------
def testfunction():
    print('ankit')
import schedule
import time
schedule.every(10).seconds.do(pinpoint)
while 1:
    schedule.run_pending()
    time.sleep(1)
