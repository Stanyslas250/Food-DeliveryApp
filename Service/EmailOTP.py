import smtplib
from email.mime.text import MIMEText
import pyotp
import os
from dotenv import load_dotenv

load_dotenv()

detail = [os.getenv('emailSender'),
          os.getenv('Password')]

subject = "Email Subject"
OTP = pyotp.TOTP('base32secret3232')
body = "This is the body of the text message"+" "+OTP.now()
sender = detail[0]
recipients = "stanyslas.contact@gmail.com"
password = detail[1]


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")
try:
    send_email(subject, body, sender, recipients, password)
    
except:
    print(sender)