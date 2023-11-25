print('--------------WELCOME TO SBI ATM------------------')
username="ROHIT GANESH"
PIN = 8919

c_name=int(input("ENTER YOUR PIN:"))

if c_name==PIN:
    print('''
    1.Deposite
    2.Withdraw
    3.Mini statement
    4.cancel
    ''')
    amount=50000
    option=int(input("select your option:"))
    if option==1:
        dep=int(input("enter the amount:"))
        amount+=dep
        print("Total smount:",amount)
    elif option==2:
        withd=int(input("Enter your ammount:"))
        amount-=withd
        print("Total amount:",amount)
    elif option==3:
        print("*****SBI ATM*****")
        print("username:",username)
        print("Total amount:",amount)
        print("*****THANKS FOR VISITING*****")

    elif option==4:
        exit()
else:
    print("please enter correct pin.....")
