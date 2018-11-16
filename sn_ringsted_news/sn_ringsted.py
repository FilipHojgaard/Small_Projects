from bs4 import BeautifulSoup, Comment
import requests

def fetchNews():
    newsArray = []

    sn = requests.get("https://sn.dk/ringsted")
    soupsn = BeautifulSoup(sn.content, 'lxml')

    tableNum = 0
    for tables in soupsn.find_all("table"):
        for news in tables.find_all("a"):
            if (tableNum == 1):
                newsArray.append(news.get_text())
        tableNum += 1

    return newsArray

# RUN FOR TESTING
newsArray = fetchNews()
for i in newsArray:
    print(i)
