# inp = [5,6,7,8,9]
# l=[]
# #Output= [5,6,7,6,7,8,7,8,9,8,9,10,9,10,11]
# for i in inp:
#     if i==5 or i==6 or i==7 or i==8 or i==8 or i==9:
#         a=i+1
#         b=i+2
#         l+=i,a,b
# print(l)

#************************************************************

# # inp = [5,6,7,8,9]
# l=[]
# user=input("enter no:")
# #Output= [5,6,7,6,7,8,7,8,9,8,9,10,9,10,11]
# for i in user:
#     for j in i:
#         if j==i:
#            a=int(i)+1
#            b=int(i)+2
#            l+=int(i),a,b
# print(l)

#****************************************************************

inp = [1,2,3,4]
# r=[([int(inp[i]),int(inp[i])+1,int(inp[i])+2]) for i in range(len(inp))]
# # res=[c for k in r for c in k]
# print(r)
# user=input("enter no:")
#Output= [5,6,7,6,7,8,7,8,9,8,9,10,9,10,11]
# for i in range(len(inp)):
#     # for j in i:
#     #     if j==i:
#     r.append([int(inp[i]),int(inp[i])+1,int(inp[i])+2])
# res=[c for k in r for c in k]
# print(res)


# l = []
# for i in range(1,len(inp)+1):
#     for j in range(i):
#         k = k + (inp[j])
#         if i-1 == j:
#            l.append(k)
# print(l)





