# import json

# def func():
#     d = {}
#     for i in range(3):
        
#         name = input("enter nm")
#         score = (input("entre no"))
#         # l.append(name)
#         # l1.append(score)
#         # d = {}
#         # for i,j in zip(l,l1):
#         # d = {}

#         key = name
#         value = score
#         d[key] = value
#         # with open('convert.txt', 'w') as f:
#         #     dictt = f.write(json.dumps(d))
        
#         #func()
#         user = input('yes or no')
#         if user != 'yes':
#             print(d)
#             quit()
#         func()
    
# print(func())
# import functools
# c = 1
# for i in range(5,0,-1):
#    c = i * c
# print(c)
# r = (functools.reduce(lambda a,b : a*b,lst))
# print(r) 

def add(a, b): 
    while b: 
        carry = a & b 
        a = a ^ b 
        b = carry << 1
    return a 

num1 = 12
num2 = 15
print("The sum of {} and {} is: {}".format(num1, num2, add(num1, num2)))


