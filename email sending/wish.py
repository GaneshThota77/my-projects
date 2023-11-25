import datetime
import pandas as pd 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Read the data
df = pd.read_csv("C:\\Users\\thtgn\\Desktop\\pandas\\exm1.csv")
#print(df)

def email_func(subject,birthday_receiver,name):
    reciver = birthday_receiver
    sender = "thotaganesh590@gmail.com"
    sender_password = 'ixwivcfzxwoofkgx'
    server = smtplib.SMTP('smtp.gmail.com',587)#passing server address(gmial.com) and port number 
    server.starttls()

    server.login(sender,sender_password)
    msg = MIMEMultipart("alternatives")
    msg['Subject'] = "Greetings From Thota Ganesh!!!!"+" "+ subject +' '+ name +'!'
    msg["'From"] = sender
    msg['To'] = reciver
    HTML = """
    <html>
        <body>
            <h1>HAPPY BIRTHDAY!</h1>
            <img src="https://media.tenor.com/BF4LXetTi0kAAAAd/birthday-wishes.gif" alt = "image" width = "640" height = "360"></img>
            <h2>
               <p>Hellow,<br>
               I hope you have a wonderful day today !<br><br>
               from;<br>
               your Friend.
               </p>
        </body>
    </html>
    
    
    """

    msg.attach(MIMEText(HTML,'html'))
    email_str = msg.as_string()
    server.sendmail(sender,reciver,email_str)
    # print("email has been sent")
today = datetime.date.today()
year = today.year

for i in range(0,len(df)):
    month = df['Birth_month'][i]
    day = df ['Birth_day'][i]
    name = df['Name'][i]
    email = df['Email'][i]

    birthdate = datetime.date(year, month, day)
    if birthdate == today:
        print('sent happy birthday')
    else:
        print('did not sent')
email_func("Happy Birthday",email, name)