name = input("Type your name:")
print("****welcom", name, "to this advanture****")

answer=input("you come on a dirt road,it has come to an end and you can go left or right. which way would you like to go(left/right)?").lower()

if answer =="left":
    answer=input("you come to a river, you can walk around it or swim across? type (walk/swim)???:")
    
    if answer =="swim":
        print("you swam across and were eaten by an alligator.")
    elif answer=="walk":
        print("you walked for many miles, ran out of water and you last the game.")
    else:
        print("not valid option. you lost.")

elif answer=="right":
    answer =input("you come to a bridge, it looks wobbly, do you want to across it or head back(cross/back)???:")
    
    if answer=="back":
        print("you got back and lose.")
    elif answer=="cross":
        answer=input("you cross the bridge and meet a stranger. do you talk to them(yes/no)?:")
        if answer=="yes":
            print("you talk to the strangers and they give you gold. you WIN!")
        elif answer=="no":
            print("you ignore the strangers and they are offended and you lose.")
        else:
            print("not valid option. you lose.")
    else:
        print("not valid option. you lose.")

else:
    print("not valid option. you lose.")