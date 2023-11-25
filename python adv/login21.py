# myList = [3,4,3,5,6,3,4,8,5,23,2,4]
# dic = {}

# # "2 counted: 1 times."
# # "3 counted: 3 times."
# # "4 counted: 3 times."
# # "5 counted: 2 times."
# # "6 counted: 1 times."
# # "8 counted: 1 times."
# # "23 counted: 1 times."

# for i in  myList:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1
# for i,j in dic.items():
#     print(f'{i} counted : {j} times')

# s = 'hello world'
# s1 = ''
# for i in range(0,len(s)):
#     if i%2 != 0:
#         s1+=s[i].upper()
#     else:
#         s1+=s[i]

# print(s1)

# a =  "hello world"
# s = ""
# for c in a:
#     for d in c:
#         if c == d:
#             s+=c+d
# print(s)

# def combine_strings(s1, s2):
#     combined = ''
#     for i, c in enumerate(s1 + s2):
#         combined += c * (i + 1)
#     return combined
# print(combine_strings('hello', 'world'))

# prime number 
# inp  = int(input("enter number :"))
# count = 0
# for i in range(1,inp+1):
#     if inp%i == 0:
#         count+=1
# if count == 2:
#     print('prime')
# else:
#     print('not a prime')

# find prime number from 1 to nth 
# n = 100
# for i in range(2, n+1):
#     for j in range(2, i):
#         if i%j == 0:
#            break
#     else:
#         print(i)


        