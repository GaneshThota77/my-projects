import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'test'
msg['From'] = 'ganesh.thota@techoptima.in'
msg['To'] = 'thtgnsh5@gmail.com'

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login('ganesh.thota@techoptima.in','ganesh')
server.send_message(msg)
server.quit()
