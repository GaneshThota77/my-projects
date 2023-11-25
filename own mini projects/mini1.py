empty_dict = {}

while True: 
    def exam():
        score = 0
        print('*********** WECOME TO THE EXAM ***********')
        user = input(f"do you want start the exam ? (yes or no) :").lower() 
        if user != 'y':
            quit()
        user_name = input('enter your name :')
        print(f"welcom to the exam MR. {user_name}")

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
    
        # empty_dict[user_name] = score
        # # highest_score = max(empty_dict.values())
        # highest_marker = max(empty_dict, key = empty_dict.get)
        # highest_marker= max(empty_dict.values())
        highest_marker = None
        highest_marks = 0
        for name, marks in empty_dict.items():
            if marks > highest_marks:
                highest_marks = marks
                highest_marker = name
        print(f'high scorere of the school {highest_marker} --> scored {highest_marks}')
        
    exam()           
            # print("3.who is the virat kohli?\na)acter\nb)comedian\nc)cricketer\nd)painter")
            # ansr=input("enter ur ansr:")
            # if ansr=='c':
            #     score+=1
            #     print("correct")
            # else:
            #     print("wrong")
                

            # print("4.who is the wall of cricket?\na)dravid\nb)sachin\nc)kohli\nd)ricky pointing")
            # ansr=input("enter ur ansr:")
            # if ansr=='a':
            #     score+=1
            #     print("correct")
            # else:
            #     print("wrong")
                

            # print("5.what is capital of america?\na)usa\nb)philadephaia\nc)newyark\nd)Washington")
            # ansr=input("enter ur ansr:")
            # if ansr=='d':
            #     score+=1
            #     print("correct")
            # else:
            #     print("wrong")
                

            # print("6.who is the powerstar in heros?\na)pavan kalayam\nb)ramcharam\nc)allu\nd)ram")
            # ansr=input("enter ur ansr:")
            # if ansr=='a':
            #     score+=1
            #     print("correct")
            # else:
            #     print("wrong")
                

            # print("7.who is the stlyes star in heros?\na)pavan kalayam\nb)ramcharam\nc)allu arjun\nd)ram")
            # ansr=input("enter ur ansr:")
            # if ansr=='c':
            #     score+=1
            #     print("correct")
            # else:
            #     print("wrong")
                

            # print("8.who is the rebal star in heros?\na)pavan kalayam\nb)ramcharam\nc)allu\nd)non of the above")
            # ansr=input("enter ur ansr:")
            # if ansr=='d':
            #     score+=1
            #     print("correct")
            # else:
            #     print("wrong")
        
            # key = user_name
            # value = score

        # else:
    # empty_dict[user_name] = score
    #     # # score = 0
    #     # #highest_score = max(empty_dict.values())
    #     # max_key = max(empty_dict, key = empty_dict.get)
    #     # max_value = max(empty_dict.values())
    # highest_marks = 0
    # highest_marker = None
    # for name, marks in empty_dict.items():
    #     if marks > highest_marks:
    #         highest_marks = marks
    #         highest_marker = name
    # print(f'high scorere of the school {highest_marker} --> scored {highest_marker}') 
         
    

