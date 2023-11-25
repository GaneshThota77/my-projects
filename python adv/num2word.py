#import math

number=input("number")
numls20={"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
#numls100={"10":"ten","11":"elevn","12":"twelve","13":"thirteen","14":"fourteen","15":"fifteen","16":"sixteen","17":"seventeen","18":"eighteen","19":"ninteen"}
numls100={"1":"ten","2":"twenty","3":"thrity","4":"fourty","5":"fifty","6":"sixty","7":"seventy","8":"eighty","9":"ninty","10":"ten","11":"elevn","12":"twelve","13":"thirteen","14":"fourteen","15":"fifteen","16":"sixteen","17":"seventeen","18":"eighteen","19":"ninteen","21":"twentyone","22":"twentytwo","23":"twentythree","24":"twentyfour","25":"twentyfive","26":"twentysix","27":"twentyseven","28":"twentyeight","29":"twentynine"}
numls1000={"1":"hundred","2":"twohundred","3":"threehundred","4":"fourhundred","5":"fivehundred","6":"sixhundred","7":"sevenhundred","8":"eighthundred","9":"ninehundred"}    
def num2str(number):
    if (int(number)<20):
        print(numls20[number])
    elif(int(number)<100):
        print(numls100[number[0]]+" "+numls20[number[1]])
    elif(int(number)<1000):
        if ((int(number))%100 == 0):
            print(numls1000[number[0]])
        else:
            print(numls1000[number[0]]+" and "+numls100[number[1]]+" "+numls20[number[2]])
    elif(int(number)<10000):
        if ((int(number))%1000 == 0):
           print(numls20[number[0]]+" thousand")
        elif(int(number)%100 == 0):
            print(numls20[number[0]]+" thousand "+numls1000[number[1]])
        elif(int(number)%10 == 0):
            print(numls20[number[0]]+" thousand "+numls1000[number[1]]+" and "+numls100[number[2]])
        else:
            print(numls20[number[0]]+" thousand "+numls1000[number[1]]+" and "+numls100[number[2]]+" "+numls20[number[3]])

    elif(int(number)<1000000):
        if ((int(number))%1000 == 0):
           print(numls100[number[0]]+" thousand")
        elif(int(number)%100 == 0):
            print(numls100[number[0]]+" thousand "+numls1000[number[1]])
        elif(int(number)%10 == 0):
            print(numls100[number[0]]+" thousand "+numls1000[number[1]]+" and "+numls100[number[2]])
        else:
            print(numls100[number[:2]]+" thousand "+numls1000[number[2]]+" and "+numls100[number[3]]+"  "+numls20[number[4]])
print(num2str(number))