import smtplib
from  email.parser import Parser

def sendASCII(msg):
    headers = Parser().parsestr('From: <senderadress587@gmail.com>\n'
            'To: <nalp777@gmail.com>\n'
            'Subject: test af smtp\n'
            '\n'
            +msg+'\n')

    receivers = ["nalp777@gmail.com"]
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("senderadress587@gmail.com", "hamsterne")
    for i in range(0,len(receivers)):
        mail.sendmail("senderadress587@gmail.com", receivers[i], headers.as_string())
    mail.close()


def sendUTF8(msg):
    headers = Parser().parsestr('From: <senderadress587@gmail.com>\n'
            'To: <nalp777@gmail.com>\n'
            'Subject: test af smtp\n'
            '\n'
            +msg+'\n')

    receivers = ["nalp777@gmail.com"]
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("senderadress587@gmail.com", "hamsterne")
    for i in range(0,len(receivers)):
        mail.sendmail("senderadress587@gmail.com", receivers[i], headers.endcode("utf-8"))
    mail.close()


# ------------ RUN TESTS

# sendASCII("god test 123")
sendUTF8("hallo")
