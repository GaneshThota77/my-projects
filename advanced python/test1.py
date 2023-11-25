# sum=0
# for i in range(101):
#     if i%2==0:
#         sum+=i 
# print(f'total sum of even number from 2 to 100 is :{sum}.')
  
# import random
# name_string = "Angela, Ben, Jenny, Michael, Chloe"
# names = name_string.split(",")
# print(names)
# len_strng = len(names)
# print(len_strng)
# rand_name = random.randrange(0,len_strng-1)
# print(rand_name)
# print(f'{names[rand_name]} is going to buy the meal today!')

# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# inp = input("list of student scroes:")
# student_scores = inp.split()
# print(student_scores)
# max = student_scores[0] 
# print(max)
# for i in student_scores:
#     if max < i:
#         max = i
# print(f'The highest score in the class is: {max}')


# row1 = ['⬜️', '⬜️', '⬜️']
# row2 = ['⬜️', '⬜️', '⬜️']
# row3 = ['⬜️', '⬜️', '⬜️']
# # map = [row1 , row2, row3]
# #print(f"{row1}\n{row2}\n{row3}")
# position = (input("Where do you want to put the treasure? "))
# items = [row1 , row2, row3]

# a = int(position[0])

# b = int(position[1])

# stored = [i for i in items]
# stored[b-1][a-1] = "X"
# print(f"{row1}\n{row2}\n{row3}")
# #-Row1

# if a == 1 and b == 1:

#     (row1[0]) = "X"

# elif a == 1 and b == 2:

#     (row1[1]) = "X"

# elif a == 1 and b == 3:

#     (row1[2]) = "X"
# #---Row2

# elif a == 2 and b == 1:

#     (row2[0]) = "X"

# elif a == 2 and b == 2:

#     (row2[1]) = "X"

# elif a == 2 and b == 3:

#     (row2[2]) = "X"

# #---Row3

# elif a == 3 and b == 1:

#     (row3[0]) = "X"

# elif a == 3 and b == 2:

#     (row3[1]) = "X"

# elif a == 3 and b == 3:

#     (row3[2]) = "X"

# print(f"{row1}\n{row2}\n{row3}")




# row = int(position[0])
# print(row)
# col = int(position[1])
# print(col)        
# map[col-1][row-1] = "X"
# print(f"{row1}\n{row2}\n{row3}")

#Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input(f"How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
# pasword = ''
# count = 0
# for i in range((nr_letters)):
#         pasword+= random.choice((letters))
#         count+=1

# for i in range(nr_numbers):
#         pasword+= random.choice(numbers)
#         count+=1

# for i in range(nr_symbols):
#         pasword+= random.choice(symbols)
#         count+=1
# jumble =""
# while pasword:    
#     position = random.randrange(len(pasword))
#     jumble += pasword[position]
#     pasword = pasword[:position] + pasword[(position + 1):]

# print(f"{nr_letters} letters,{nr_symbols} symbol,{nr_numbers} numbers = {jumble}")



# for num in range(1,101):
#         if (num % 3 == 0) and (num % 5 == 0):
#                 print("FizzBuzz")
#                 continue
#         if num % 3 == 0:
#                 print("Fizz")
#                 continue
#         elif num % 5 == 0:
#                 print("Buzz")
#                 continue
#         # elif (num % 3 == 0) and (num % 5 == 0):
#         #         print("FizzBuzz")
#         #         continue
#         print(num)

# inp = input("input a list of student heights  :").split()
# count=0
# index = 0
# for i in inp:
#     count+=1
#     index+=int(i)
#     res = index/count
# print(int(res))


# import random
# import time
# def play_again():
#     ans = input("you want to play again? y or n : ")
#     if ans == 'y':
#         guss_game()
#     else:
#         print("Thank You For Playing!")
#         exit()
# #guess = input("guess a character:")
# def guss_game():
#     word_list = ["aardvark", "m", "baboon", "camel", "bus"]
#     char = random.choice(word_list)
#     empty = ''
#     choices = 9
#     while choices > 0:
#         failed = 0
#         for i in char:
#             if i in empty:
#                 print(i)
#             else:
#                 print("_")          
#                 failed+=1
#         if failed == 0:
#             print("you win")
#             time.sleep(2)
#             play_again()
#         guess = input("guess a character:")
#         empty += guess
#         if guess not in i:
#             choices -= 1
#             print("You have",  choices, 'more guesses')
#             if choices == 0:
#                 print("You Loose")
#                 time.sleep(2)
#                 play_again()
# guss_game()
