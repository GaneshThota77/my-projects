# inp=[1,2,3,[4,5,6],7,[8],9,10,[11,12,13]]

l=[]
# for i in inp:
#     if type(i)==int:
#         l.append(i)
# for j in inp:
#     if type(j)==list:
#         l.extend(j)
#         l.sort()
# print(l)
def flot(inp):
    for i in inp:
        if type(i) == int:
            l.append(i)
        else:
            flot(i)
    return(l)
print(flot(inp=[1,2,3,[4,5,6],7,[8],9,10,[11,12,13]]))