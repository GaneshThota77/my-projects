#inp = [1,2,3,[4,5,[6,7,8,[9]]]]
inp = [1,2,3,[4,5,[6,7,8,[9,[10],[11],[12],[13,14,[15]]]]]]
# #o/p =[1,2,3,4,5,6,7,8,9]
empty = []
for i in inp:
    if type(i) == list:
        for j in i:
            if type(j) == list:
                for k in j:
                    if type(k) == list:
                       for l in k:
                            if type(l) == list:
                               for m in l:
                                    if type(m) == int:
                                       empty.append(m)
                            else:
                                empty.append(l)
                    else:
                        empty.append(k)
            else:
                empty.append(j)
    else:
        empty.append(i)

print(empty)


# empty = []
# def flot(data):
#     #empty = []   
#     for i in data:
#         if type(i) == int:
#             empty.append(i)
#         else:
#             flot(i)

#     return (empty)
# print(flot(data = [1,2,3,[4,5,[6,7,8,[9,[10],[11,12],[13]]]]]))


# Define a nested dictionary
#inp = {'a': 1, 'c': {'a': 2,'b': {'x': 5,'y' : 10}},'d': [1, 2, 3]}


# my_dict = {'a': 1, 'c': {'a': 2,'b': {'x': 5,'y' : 10}},'d': [1, 2, 3]}
# #my_dict ={'a': 1, 'c': {'a': 2,'b': {'x': 5,'y' : 10}},'d': [1, 2, 3]}
# # #Out = {'a': 1,'c_a': 2,'c_b_x': 5,'c_b_y': 10,'d': [1, 2, 3]}

# emty = {}
# stng = ''
# for key1, val1 in my_dict.items():
#     if isinstance(val1, dict):       
#         for key2, val2 in val1.items():
#             if isinstance(val2, dict):
#                 strg = (key1)+'_'+(key2) 
#                 for key3, val3 in val2.items():
#                     if not isinstance(val3, dict):
#                         strng = strg+'_'+(key3)
#                         emty[strng] = val3
                        
#                     else:
#                         emty[stng] = val3
#             else:
#                 strg = (key1)+'_'+(key2)
#                 emty[strg] = val2        
#     else:
#         emty[key1] = val1
# print(emty)


# def flatten_dict(d, parent_key='', sep='_'):
#     items = []
#     for k, v in d.items():
#         new_key = f"{parent_key}{sep}{k}" if parent_key else k
#         if isinstance(v, dict):
#             items.extend(flatten_dict(v, new_key, sep=sep).items())
#         else:
#             items.append((new_key, v))
#     return dict(items)

# inp = {'a': 1, 'c': {'a': 2,'b': {'x': 5,'y' : 10}},'d': [1, 2, 3]}
# #out = flatten_dict(inp)
# #print(out)

# emty = {}

# def func(mydict, prefix=''):
#     for key, val in mydict.items():
#         if isinstance(val, dict):
#             new_prefix = prefix + key + '_'
#             func(val, prefix=new_prefix)
#         else:
#             emty[prefix + key] = val
#     return emty

# mydict = {'a': 1, 'c': {'a': 2,'b': {'x': 5,'y' : 10}},'d': [1, 2, 3]}
# print(func(mydict))
# name = " "
# def func(data):
#     name = " "
#     for i in data:
#        name = i + name
#     return(name)

# print(func(data = "ganesh"))
