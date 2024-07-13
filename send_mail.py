import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = "wzh609@gmail.com"
receiver = "psp4588@gmail.com"
msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = receiver
heard = Header("Test Send Email","utf-8")
msg["Subject"] = heard.encode() #編碼


boby = "This is email send from python"
msg.attach(MIMEText(boby))
# mboy=MIMEText(boby)
# msg.attach(mboy)

ssl_context = ssl.create_default_context() #連線設定
with smtplib.SMTP_SSL("smtp.gmail.com",465,context =ssl_context) as server: #把ssl_context default值改掉，指定context=ssl_context
    server.login(sender,"knkoypfcmfkghjju")
    server.sendmail(sender,receiver,msg.as_string())
print ("Success send email")