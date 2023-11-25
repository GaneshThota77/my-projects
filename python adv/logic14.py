inp= {'vasanth':101,'siva':23,'ganesh':86}
d={}
#Out= {'siva':23,'ganesh':86,'vasanth':101}
st_dict=sorted(inp.values())
print(st_dict)
for i in st_dict:
    for j in inp.keys():
        if inp[j]==i:
            d[j]=inp[j]
print(d)