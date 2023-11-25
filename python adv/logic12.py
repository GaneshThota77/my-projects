l=[]
d={}
def start():
    l1=[1,2,3,4,5,6,7]
    for i in range(len(l1)):
        l.append(i)
        for a,b  in zip(l1,l):
            values=b
            keys=a
            d[values]=keys
    print(d)

start()

