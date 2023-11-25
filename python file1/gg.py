arr1 = ['A','B','C','D']
arr2 = ['P','Q','A','D']
for i in arr1:
    for j in arr2:
        if j==i:
            print(arr2.index(j))