n= [1,2,3,5,6,7,8,9,10]
n1 =len(n)+1
totalsum =n1*(n1+1)//2
#print('total sum',sum)
sum=0
for i in n:
    sum=sum+i
print(totalsum-sum)