inp=[1,2,3,[4,5,[6]],7,8,9,10]
print(type(inp))

l=[]
for i in inp:
    if type(i)==int:
        l.append(i)

for j in inp:
    if type(j)==list:
        l.extend(j)

for k in l:
    if type(k)==list:
        l.extend(k)
        l.remove([6])
        l.sort()
print(l)