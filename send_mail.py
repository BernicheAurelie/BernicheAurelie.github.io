# coding: utf-8
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import cgi
import cgitb
import html


print('test envoi email')

# mode debug (à supprimer si ok):
cgitb.enable()

expediteur = 'berniche.aurelie@orange.fr'
password = 'A20081113b'
destinataire = 'berniche.aurelie@orange.fr'

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
    print("<script> alert('Merci, message bien envoyé. Je vous répond dans les plus brefs délais.')</script>")
except:
    print("<p> Merci de renseigner tous les champs du formulaire.</p>")
    print(Exception)

print("Content-type: text/html; charset=utf-8\n")
doc_html = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Send mail</title>
</head>
<body>
    <h1> Mail envoyé</h1>
"""
print(doc_html)
print(f"<h2>Merci {prenom}</h2>")
doc_html = """
</body>
</html>
"""
print

msg = MIMEMultipart()
msg['From'] = expediteur
msg['To'] = destinataire
msg['Subject'] = subject 
msg.attach(MIMEText(message))
print(msg)
mailserver = smtplib.SMTP('smtp.orange.fr', 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login(expediteur, password)
mailserver.sendmail(expediteur, expediteur, msg.as_string())
mailserver.quit()
print(msg)
print('done?')
