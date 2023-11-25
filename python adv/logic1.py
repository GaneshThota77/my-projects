list1=["ganesh","vasanth","venkey"]
#output={'ganesh':'hsenag','vasanth':'htnasav','venkey':'yeknev'}
res=[i[::-1] for i in list1]
print(res)
# for i in list1:
#     res.append(i[::-1])
# dict={}
# for i,j in zip(list1,res):
#     keys=i
#     values=j
#     dict[keys]=values
# print(dict)
dictionary = {k: v for k, v in zip(list1, res)}
print(dictionary)