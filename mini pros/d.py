import random

user_wins=0
computer_wins=0

options=["rock","paper","scissors"]
options[0]

while True:
    user=input('Type of rock/paper/scissors or Q to quit.').lower()
    if user =="q":
        break

    if user not in options:
        continue
    random_num=random.randint(0,2)
    computer_pick =options[random_num]
    print("computer picked", computer_pick + ".")


    if user == "rock" and computer_pick =="scissors":
        print("you won!")
        user_wins+=1
        continue
    
    elif user == "paper" and computer_pick =="rock":
        print("you won!")
        user_wins+=1
        continue

    elif user == "scissors" and computer_pick =="paper":
        print("you won!")
        user_wins+=1
        continue
    
    else:
        print("you lost!")
        computer_wins+=1

print("you won", user_wins,"times.")
print("the computer won",computer_wins,"times.") 
print("goodbye!")

    