import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

print ('---Start---')

s= smtplib.SMTP('smtp.office365.com',587)
s.starttls()

print('Logging In...')
s.login("EMAIL","PASSWORD")
print('Logged-in Successfully')

msg = MIMEMultipart()
msg['From']='SENDER_EMAIL'
msg['To']='TO_EMAIL'
msg['Cc']='CC_EMAIL'
msg['Subject']= 'This is test'
body= 'Hello ---, \nThis is --- from ---. \n\nThanks,\---\n\n\nNote* This message was sent through a python script'
msg.attach(MIMEText(body,'plain'))


files=["text.txt","abc.jpg"]
for f in files:
    with open(f,"rb") as fil:
        part= MIMEApplication( fil.read(),Name=basename(f))
        part['Content-Displosition']= 'attachment; filename="%s"' % basename(f);
        msg.attach(part)

print('sending your message,please wait...')
s.send_message(msg)
print('Message sent successfully')
del msg

s.quit()

print('---End---')
