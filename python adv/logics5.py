s="vasanth"
#Output:  v0 a1 s2 a3 n4 t5 h6
d =''
for idx,i in enumerate(s):
    c=f"{i}{idx} "
    #print(c,end="")
    d+=c
print(d)