#def cube():
#   n=1
#   while n<=10:
#      r = n**3
##      n+=1
#       return(r)
        #yield(r)
#x=cube()
#print(x)
#for i in x:
    #print(i)


def main():
    #list1=[]
    for i in range(10):
        #list1.append(i)
    #return list1
        yield i
obj = main()
#print(obj)

for j in obj:
    print(j)