import smtplib
from  email.parser import Parser
import datetime

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


def sendUTF8(message):
    tls = True
    sender = "XYZ <senderadress587@gmail.com.com>"
    to = "ABC <nalp777@gmail.com.com>"
    subject = "GOOD TEST"


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


# ------------ RUN TESTS

# sendASCII("god test 123")
sendUTF8("æøå ÆØÅ")
