

# a='venky'

# count=0
# #print(len(a))


# for i in a:
#     count+=1
# print(count)

 
# -------------------------------------------------------------------------

# a='venky'                                                                                                      
# b=''
# #   'veky'
# #print(a[:2]+a[-2:])  
# for i in a:
#     if i!='k':
#         b=b+i
# print(b)
# -------------------------------------------------------------------------

# name='''Dear [NAME],

# It's your birthday! Have a great day!

# Have a great day!.

# TechOptima'''.split()

# string=''
# for i in name:
#      if '[NAME]' in i:
#         string += ' ' +i.replace('[NAME]','venkey')
#      else:
#          string = string + ' ' + i
# print(string)   
# --------------------------------------------------------------------------

# a=[1,2,3,4,5,6,7,7,8]
# max=a[0]
# #print(max(a))
# for i in a:
#     if max<i:
#         max=i 
# print(max)        


# a='st'
# #print(a+'ly')

# if len(a)>3:
#     a=a+'ly'
#     print(a)
# else:
#    print(a) 
            

    

# list=[(2,5),(1,2),(4,4),(2,3),(2,1)]
# #output=[(2,1),(1,2),(2,3),(4,4),(2,5)]
# list[0],list[-1]=list[-1],list[0]
# list[1],list[3]=list[3],list[1]
# print(list)

    

# '''x=lambda a,b:a+b
# print(x(30,50))    

# 300,00,000
# a=3000000
# string=[]
# a=str(a)
# for i in a:
#     string.append(i)
# #print(string)
# string.insert(2,',')
# string.insert(5,',')
# print(string)
# emp=''
# for j in string:
#     emp+=j
# print(emp)
           


# # list = ['abc','xyz','aba','1221']
# # count = 0
# # for i in list:
# #     if i[0] == i[-1]:
# #         count+=1
# #         #i = count
# # print(count)

# import random as rdm  
  
# # Here the user will be asked to enter their name first  
# name1 = input("What is your NAME ? ")  
  
# print("Best of Luck! ", name1)  
   
# words1 = ['Donkey', 'Aeroplane', 'America', 'Program',  
#          'Python', 'language', 'Cricket', 'Football',  
#          'Hockey', 'Spaceship', 'bus', 'flight']  
   
# # rdm.choice() function will choose one random word from the gven list of words  
# word1 = rdm.choice(words1)  
   
   
# print ("Please guess the characters: ")   
# guesses1 = ''   
# turns1 = 10    
# while turns1 > 0:     
#     failed1 = 0     
#     for char in word1:  
#         if char in guesses1:  
#             print(char)                
#         else:  
#             print("_")            
#             failed1 += 1     
#     if failed1 == 0:         
#         print("User Win")           
#         print("The correct word is: ", word1)  
#         break      
#     guess1 = input("Guess another character:")  
#     guesses1 += guess1       
#     if guess1 not in word1:            
#         turns1 -= 1                   
#         print("Wrong Guess")  
#         print("You have ", + turns1, 'more guesses ')            
#         if turns1 == 0:  
#             print("User Loose")  

