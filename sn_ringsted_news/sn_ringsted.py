from bs4 import BeautifulSoup, Comment
import requests
import numpy as np
import time
import smtplib
from email.parser import Parser
import datetime

def main():
    old_news = []
    while(True):
        time.sleep(28800)
        # time.sleep(1800) # half an hour
        old_news = eventTime(old_news)

def eventTime(old_news):
    new_news = fetchNews()
    all_news = distinctNews(old_news, new_news)
    parsedNews = parseNews(all_news)
    sendMail(parsedNews)
    print("\n *** Sent mail at: " + str(datetime.datetime.now()) + " *** \n")
    print(parsedNews)
    return all_news


def parseNews(input):
    parsedString = ""
    for i in range(0,len(input)):
        parsedString = parsedString + input[i] + " \n <br>"
    return parsedString

def sendMail(message):
    tls = True
    sender = "<senderadress587@gmail.com.com>"
    to = "<nalp777@gmail.com.com>"
    subject = "SN - RINGSTED NEWS SCRAPER"


    headers = {
        'Content-Type': 'text/html; charset=utf-8',
        'Content-Disposition': 'inline',
        'Content-Transfer-Encoding': '8bit',
        'From': sender,
        'To': to,
        'Date': datetime.datetime.now().strftime('%a, %d %b %Y  %H:%M:%S %Z'),
        'X-Mailer': 'python',
        'Subject': subject
    }

    msg = ''
    for key, value in headers.items():
        msg += "%s: %s\n" % (key, value)

    msg += "\n%s\n"  % (message)

    receivers = ["nalp777@gmail.com"]
    s = smtplib.SMTP("smtp.gmail.com",587)
    s.ehlo()
    s.starttls()
    s.ehlo() # igen? måske vigtigt?
    s.login("senderadress587@gmail.com", "hamsterne")
    for i in range(0,len(receivers)):
        s.sendmail("senderadress587@gmail.com", receivers[i], msg.encode("utf8"))
    s.close()


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

def distinctNews(oldNews, newNews):
    return list(set(oldNews + newNews))




main()
