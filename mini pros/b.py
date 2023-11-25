import time

print("welcome to my computer quiz!")
playing = input("do you want to play?:")
if playing.lower()!="yes":
    quit()

time=time.sleep(1)
print("okey! lets play......")
print("GO")
score=0
answer = input("what does CPU stands for?:")
if answer.lower()=="cerntral processing unit":
    print("correct")
else:
    print("wrong")
    score+=1

answer = input("what is pip8?:")
if answer.lower()=="coding guide":
    print("correct")
else:
    print("wrong")
    score+=1

answer = input("who is god of cricket?:")
if answer.lower()=="Sachin":
    print("correct")
else:
    print("wrong")
    score+=1

answer = input("who did three 200 in cricket?:")
if answer.lower()=="Rohit":
    print("correct")
else:
    print("wrong")
    score+=1
print("you got " + str(score)+ "for answers")
print("you got " + str((score/4) * 100)+ "%.")