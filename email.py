import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
msg['From'] = "sender@example.com"
msg['To'] = "receiver@example.com"
msg['Subject'] = "Hello from Python"

body = "This is the email body."
msg.attach(MIMEText(body, 'plain'))

with smtplib.SMTP('smtp.example.com', 587) as server:
    server.starttls()
    server.login("sender@example.com", "password")
    server.sendmail("sender@example.com", "receiver@example.com", msg.as_string())
