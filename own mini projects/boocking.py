from datetime import datetime

FIRST_CLASS = 'first class'
SECOND_CLASS = 'second class'
THIRD_CLASS = 'third class'
first_class = 3000
second_class = 2500
third_class = 1500 
print("***********WELCOME TO ROHIT HOMES*************")
user_name = input("enter your name :")
inp = input(f"Do you want to see the book list {user_name} (y or n)").lower()
if inp != 'y':
    quit()   
user = (input(f"we have\n 1. first class {first_class} rs per a day\n 2. second class {second_class} rs per a day\n 3. third clss {third_class} rs per a day\n could you plese select the class :"))

print("how many days do you want to stay please mention dates below..")   
user1 = (input("enter your dates (*-*-*) or (*/*/*):"))
user2 = (input("enter your last date (*-*-*) or (*/*/*):"))

d1 = datetime.strptime(user1,"%d-%m-%Y")
d2 = datetime.strptime(user2,"%d-%m-%Y")
# d3 = datetime.strptime(user1,"%d/%m/%Y")
# d4 = datetime.strptime(user2,"%d/%m/%Y")
res = (d2) - (d1) 
# res1 = d3 - d4
days  = res.days 
def selecting_rooms():

    
    amount = 0
    with open('conformed_detailes.txt','w') as f:
        
        if user == '1':
            amount += first_class
            line = (f"Dear {user_name},\nyou have booked from {user1} to {user2}\nyour room has been booked {FIRST_CLASS} so you have to pay {amount*days} rs for {days} days\nThank you booking at Rohit homes\nhave a great day!!!!!")
            f.write(line)
            print("conformed..............")
        elif user == '2':
            amount += second_class
            line1 = (f"Dear {user_name},\nyou have booked from {user1} to {user2}\nyour room has been booked {SECOND_CLASS} so you have to pay {amount*days} rs for {days} days\nThank you booking at Rohit homes\nhave a great day!!!!!")
            f.write(line1)
            print("conformed..............")

        elif user == '3':
            amount += third_class
            line2 = (f"Dear {user_name},\nyou have booked from {user1} to {user2}\nyour room has been booked {THIRD_CLASS} so you have to pay {amount*days} rs for {days} days\nThank you booking at Rohit homes\nhave a great day!!!!!")  
            f.write(line2)
            print("conformed..............")
        else:
            f.write('enter valid number')
    
selecting_rooms()