from bs4 import BeautifulSoup, Comment
import requests
import numpy as np
import time
import smtplib
from email.parser import Parser

def main():
    old_news = []
    while(True):
        # time.sleep(28800)
        time.sleep(3)
        old_news = eventTime(old_news)

def eventTime(old_news):
    new_news = fetchNews()
    all_news = distinctNews(old_news, new_news)
    sendMail(all_news)
    return all_news

def sendMail(news):
    pass
    mailText = ""
    for i in news:
        mailText = mailText + i + "\n"
    print(mailText)

    headers = Parser().parsestr('From: <senderadress587@gmail.com>\n'
        'To: <nalp777@gmail.com>\n'
        'Subject: sn.dk/ringsted nyheder\n'
        'Content-Type: text/plain; charset=utf-8\n'
        '\n'
        +mailText+'\n')

    receivers = ["nalp777@gmail.com"]


    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("senderadress587@gmail.com", "hamsterne")
    for i in range(0,len(receivers)):
        mail.sendmail("senderadress587@gmail.com", receivers[i], headers.as_string())

    mail.close()


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
