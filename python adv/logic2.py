dict1 = {"ganesh":"male","vasanth":"male","aishu":"female","venkey":"male","modini":"female","chandana":"female"}
inp=input("enter gender:")
list1=[]
for i,j in dict1.items():
    if inp == j:
        list1.append(i)
print(list1)
