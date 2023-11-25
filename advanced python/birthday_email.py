# First we have to import smtplib which is allows us to sending emails in python
# We need to get birthday persons data from birthday.csv file
# We have three text file in a folder so we need to get one text file randomly and read that data 
# now we have to use for loop for getting data from csv file
# Then we need to import datetime for time and date
# then we have to take birthdate for today so for that we have to use datatime.time(month,day)
# then if bithdate is equal to today it need to be send an email to birthday person 
#   
# Then we have to create  sender_email of who is going to sending mail,reciver_email for who is going to recives and massage for which massage we want to parse over the mail
# Password for email to login
# To send the mail we have to use server variable to connect to the SMTP server
# In that server we passing the server addres(email.com) and port number(587)
# Then we have to start server
# After then we have to create login so we use server.loin and sending emails for server.email

#import os
import glob
import random
import datetime
import pandas as pd 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

df = pd.read_csv("C:\\Users\\thtgn\\Desktop\\pandas\\exm1.csv")
#os.chdir(r"C:\\Users\\thtgn\Desktop\\letter_template")
my_file = glob.glob('C:\\Users\\thtgn\Desktop\\letter_template\\*.txt')
file = random.choice(my_file)
with open(file,'r') as f:
    chg = (f.read())
    
def email_func(reciver_email):
    email = reciver_email
    
    sender = "thotaganesh590@gmail.com"
    sender_password = 'ixwivcfzxwoofkgx'
    server = smtplib.SMTP('smtp.gmail.com',587)#passing server address(gmial.com) and port number 
    server.starttls()
    server.login(sender,sender_password)
    msg = MIMEMultipart("alternatives")
    msg['Subject'] = "Greetings From Thota Ganesh!!!!"
    msg["'From"] = sender
    #msg['To'] = email
    msg.attach(MIMEText(chng))
    email_str = msg.as_string()
    server.sendmail(sender,email,email_str)

today = datetime.date.today()
year = today.year
email_st = ''
for i in range(0,len(df)):
    month = df['Birth_month'][i]
    day = df['Birth_day'][i]
    name = df['Name'][i]
    email_l = df['Email'][i]
    

    chng = chg.replace('[NAME]',name )

    birthdate = datetime.date(year, month, day)
    
    if birthdate == today: 
        email_st = email_st + email_l + ','
        print('sent happy birthday')
        
    else:
        print('did not sent')
email_func(email_st)