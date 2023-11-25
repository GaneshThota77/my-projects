import time


user=input("enter ue name:").lower()
print("hellow "+ user +" welcom to examination")
req=input('Are u ready to write an exam:?')
if req.lower()!='yes':
    quit()

time.sleep(2)
print("OKEY LETS PLAY.........")
print("HERE WE GO FIRST QUATION...")
score=0
print("1.who is the god of cricket?\na)dravid\nb)sachin\nc)kohli\nd)ricky pointing")
ansr=input("enter ur ansr:")
if ansr=='b':

    score+=1
    print("correct")
else:
    print("wrong")
    

print("2.who did 100 centuries in cricket?\na)dravid\nb)virat\nc)sachin\nd)ricky pointing")
ansr=input("enter ur ansr:")
if ansr=='c':
    score+=1
    print("correct")
else:
    print("wrong")
    

print("3.who is the virat kohli?\na)acter\nb)comedian\nc)cricketer\nd)painter")
ansr=input("enter ur ansr:")
if ansr=='c':
    score+=1
    print("correct")
else:
    print("wrong")
    

print("4.who is the wall of cricket?\na)dravid\nb)sachin\nc)kohli\nd)ricky pointing")
ansr=input("enter ur ansr:")
if ansr=='a':
    score+=1
    print("correct")
else:
    print("wrong")
    

print("5.what is capital of america?\na)usa\nb)philadephaia\nc)newyark\nd)Washington")
ansr=input("enter ur ansr:")
if ansr=='d':
    score+=1
    print("correct")
else:
    print("wrong")
    

print("6.who is the powerstar in heros?\na)pavan kalayam\nb)ramcharam\nc)allu\nd)ram")
ansr=input("enter ur ansr:")
if ansr=='a':
    score+=1
    print("correct")
else:
    print("wrong")
    

print("7.who is the stlyes star in heros?\na)pavan kalayam\nb)ramcharam\nc)allu arjun\nd)ram")
ansr=input("enter ur ansr:")
if ansr=='c':
    score+=1
    print("correct")
else:
    print("wrong")
    

print("8.who is the rebal star in heros?\na)pavan kalayam\nb)ramcharam\nc)allu\nd)non of the above")
ansr=input("enter ur ansr:")
if ansr=='d':
    score+=1
    print("correct")
else:
    print("wrong")
    

print(f'congratulations you got{score}makrs ')


