a= [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(a)):
    col = [ele[i] for ele in a]
    if len(set(col))!=len(col):
        print(True)
    else:
        print(False)