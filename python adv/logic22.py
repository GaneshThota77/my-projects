# k = 10
# while  k:
#     k=k-1
#     print(k**2) 
# for i in reversed(range(k)):
#     print(i)

    # k=k-1

# k="string"
# for val in k:
#     if val == "i":
#         continue
#     print(val)

# k="flexiple"
# for char in k:
#     if char == 'p':
#         break
#     print(char)

# inp = 39
# sum = 0
# for i in str(inp):
#     sum=sum+int(i) 
# print(sum)

    

# wet_val = int(input("enter ur weight:"))
# hgt_val = float(input("enter ur height:"))
# total_val = wet_val/(hgt_val * hgt_val)
# print(int(total_val))

# a = int(input("what was the total bill ?"))
# b = int(input("how much tip would you like to give ?10, 12, or 15 :"))
# c = int(input("how many peoples to split the bill ?"))
# total = (a+(a*b)/100)/c
# print(f'Each person should pay :${total:.2f}')
# num = str(total)
# num_list = [i for i in num]
# num_list[1],num_list[2] = num_list[2],num_list[1]
# res = ''
# for i in num_list:
#     res+=i
# # print(f'Each person should pay :{total}')
# print(f'Each person should pay :{res}')

# inp = (int(input("what is ur current age ?")))
# days = inp * 365
# weeks = inp * 52
# months = inp * 12
# print(f'You have {days} days, {weeks} weeks, and {months} months left.')

# from datetime import date
# age = int(input("enter your current age ?"))
# today = date.today()
# time_difference = today - age
# D = time_difference.days
# M = int((D/365)*12)
# W = int(D/365)/7
# print(f'You have {D} days, {W} weeks, and {M} months left.')

# from datetime import date
# def calculate_age(born):
#     today = date.today()
#     return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
# print(calculate_age(25))

# def even_odd():
#     num=int(input("enter ur no :"))
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
# even_odd()

# w = int(input("enter your weight:"))
# h= float(input("enter your height:"))
# x = w/(h*h)
# if x<18.5:
#     print("underweight")
# elif x<25:
#     print("normal")
# elif x<30:
#     print("overweight")
# elif x<35:
#     print("obese")
# else:
#     print("clinically obese")

    

# user = int(input("enter a year:"))
# if (((user%4==0) and (user%100!=0)) or (user%400==0)):
#     print("leap year")
# else:
#     print( "not a leap year")









1
# user = int(input("enter a year:"))
# if (((user/4==500) and (user/100==20)) or (user/400==5)):
#     print("leap year")
# else:
#     print( "not a leap year")



# print("Welcome to Python Pizza Deliveries!")
# inp = input("what size pizza do u want ? S, M,or L :")
# # Sp = 15
# # Mp = 20
# # Lp = 25
# sum = 0
# if inp.lower() == 's':
#     sum+=15
# elif inp.lower() == 'm':
#     sum+=20
# elif inp.lower() == 'l':
#     sum+=25

# inp1 = input("do you wnt pepparoni? Y or N :")
# if inp1.lower() == 'y':
#     if inp.lower() == 's':
#         sum += 2
#     else:
#         sum +=3

# inp2 = input("do you want extra cheese? Y or N :")
# if inp2.lower() == 'y':
#    sum += 1

# print(f'your final bill is : ${sum}.')

# name1 = input("what is ur name :")
# name2 = input("what is their name :")
# word1 = 'true'
# word2 = 'love'
# mixed = word1 + word2               
# count=0
# sum=0                                       
# for i in mixed:
#     if i in name1:  
#         count+=1
#     if i in name2:
#         sum+=1
# a =str(count)
# b =str(sum)
# sng=a+b
# final = int(sng)            
# if (final < 10) or (final > 90):
#     print(f"Your score is {final}, you go together like coke and mentos.")
# elif (final>=40) & (final<50) :
#     print(f'Your score is {final}, you are alright together.')
# else:
#     print(f'Your score is {final}.')

 
   
# import random
# inp = random.randrange(2)
# if inp ==0:
#     print(f"{inp}tails")
# else:
#     print(f"{inp} heads")


 

