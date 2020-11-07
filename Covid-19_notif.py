from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "E:\\Python_VSC\\Covid-19\\favicon.ico",
        timeout = 30
    )

def getData(url):
    return requests.get(url).text

if __name__ == '__main__':
   # while True:
        myHtmlData = getData("https://www.worldometers.info/coronavirus/country/india/")
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        #print(soup.prettify())
        # for t in soup.find_all('table'):
        #     print(t.get_text())
        updates = soup.title.get_text().split(' ')   
        message = f"Total Cases: {updates[2]} and Total Deaths: {updates[5]}"
        notifyMe("Covid-19 update is here... INDIA",message)
        #time.sleep(86400)