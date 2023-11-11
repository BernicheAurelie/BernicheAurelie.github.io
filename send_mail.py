# coding: utf-8
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import cgi
import cgitb
import html
import os
from dotenv import load_dotenv

load_dotenv()


expediteur = os.getenv('expediteur', 'default')
password = os.getenv('password', 'default')
destinataire = os.getenv('destinataire', 'default')
smtp_server = 'smtp.orange.fr'
port = 587

form = cgi.FieldStorage()

try:
    input_prenom = form.getvalue('prenom')
    prenom = html.escape(input_prenom)
    input_nom = form.getvalue('nom')
    nom = html.escape(input_nom)
    input_email = form.getvalue('email')
    email = html.escape(input_email)
    input_message = form.getvalue('message')
    message = html.escape(input_message)
    subject = [prenom, nom, email]
except:
    print(Exception)
    raise Exception

msg_html_1 = """
<html lang="en">

<body>
    <p> """
msg_html_2 = message.as_string()
msg_html_3 = """   
    </p>
        
</body>
</html>
"""
msg_html = msg_html_1 + msg_html_2 + msg_html_3
msg = MIMEMultipart("alternative")
msg['From'] = expediteur
msg['To'] = destinataire
msg['Subject'] = subject.as_string() 
msg.attach(MIMEText(message, "text"))
msg.attach(MIMEText(msg_html, "html"))
with smtplib.SMTP(smtp_server, port) as mailserver:
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(expediteur, password)
    mailserver.sendmail(expediteur, expediteur, msg.as_string())

