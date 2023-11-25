test_list = [1, 4, 5, 6, 7]
list1=[]
#print ([list((i, test_list[i])) for i in range(len(test_list))])
for i in range(len(test_list)):
    list1.append(f'{i},{test_list[i]}')
print(list1)