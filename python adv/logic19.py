
num =str(1000000)
lst=[]
for i in num:
   lst.append(i)
lst.insert(1,',')
lst.insert(5,',')
stng = ''
for j in lst:
    stng+=j
print(stng)
