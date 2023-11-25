'''a =[1,2,3,4,5]
b=[]
for i in str(a):
    if i=='3':
        b=a[:int(i)]
#b=int(b)
print(b)'''


i = [1,2,3,4,5]
s=''
for k in (i):
    if k==3:
        for j in i[:k]:
            s=s+str(j)
print(int(s))
