
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
sender_email = 'thotaganesh590@gmail.com'
#reciver_email = ["ganesh.thota@techoptima.com","krishna.avula@techoptima.in"]
password = 'ixwivcfzxwoofkgx'
#massage_to_reciver = 'mail sent from techoptima'

server = smtplib.SMTP('smtp.gmail.com',587)#passing server address(gmial.com) and port number 
server.starttls()

server.login(sender_email,password)
message = MIMEMultipart("alternatives")
message['Subject'] = "Greetings From Thota Ganesh"
message['From'] = sender_email
message['To'] = 'ganesh.thota@techoptima.in , krishna.avula@techoptima.in , thtgnsh5@gmail.com'
#aravind.terli@techoptima.in,krishna.avula@techoptima.in,balaji.reddy@techoptima.in,mounica.g@techoptima.in,bhaskar.kuchana@techoptima.in,ramcharan.muthyala@techoptima.in,saranya.mudadla@techoptima.in
html = """
        <html>
            <head>
            </head>
            <body>
                <h1>Hellow! Happy Diwali To You And Your Family Members!!!!</h1>
                <img src="https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/e6477844081885.580f6e390f38d.gif" alt="image" width = "640" height = "360"</img>
                <p><strong>Hello,</strong><br>
                <strong>May This Diwali Fulfill All Your Dreams And Bring Happiness To Your Life Forever!!!!!<br><br>
                from;<br>
                your friend.</strong>
                </p>

            </body>
        </html>
        
"""
#textpart = MIMEText(text, 'plain')
message.attach(MIMEText(html,'html'))
#message.attach(MIMEText(text,'text'))
email_string = message.as_string()
#message.attach(textpart,htmlpart)
#v_n = (sender_email,reciver_email,message.as_string())
server.sendmail(sender_email,message['To'].split(','),email_string)
print("email has been sent")
