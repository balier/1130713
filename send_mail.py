import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = "wzh609@gmail.com"
receiver = ["psp4588@gmail.com","wzh609@gmail.com"]


for i in receiver:

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = i
    heard = Header("Test Send Email","utf-8")
    msg["Subject"] = heard.encode() 


    boby = "This is email send from python"
    msg.attach(MIMEText(boby))


    ssl_context = ssl.create_default_context() 
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context =ssl_context) as server: 
        server.login(sender,"knkoypfcmfkghjju")
        server.sendmail(sender,i,msg.as_string())
    print ("Success send email")