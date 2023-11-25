from datetime import datetime
#USER="ROHIT GANESH"
name=input("enter your name:")
print("""***************WELCOME TO FRESH MART**************

      HERE IS ALL ITEMS WHAT YOU NEED""")
#if name==USER:

lists='''
Rice    Rs 20/kg
Suger   Rs 30/kg
Solt    Rs 20/kg
Oil     Rs 80/lt
Paneer  Rs 110/kg
Maggi   Rs 50/kg
Boost   Rs 90/kg
Colgate Rs 20/small

'''
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]


items={'Rice' : 20,   
'Suger'    : 30,
'Solt'     : 20,
'Oil'      : 80,
'Paneer'   : 110,
'Maggi'    : 50,
'Boost'    : 90,
'Colgate'  : 20
}

option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to but press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your item: ")
        quantity=int(input("enter quality:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalprice=gst+totalprice
        else:
            print("sorry you enterd item is not avilable")
    else:
        print("entered wrong number")

    inp=input("can i bill the items (yes or no)?:")
    if inp=='yes':
        pass
        if finalprice!=0:
            for i in range(len(price)):
                