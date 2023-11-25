# box = [[1,2,3],
#        [2,1,3],
#        [3,2,1]]
# grid =[[2,3,1],
#       [1,2,3],
#       [3,1,2]]

# for row in range(0,len(box),3):
#     for i in range(1,len(box)):
#        if box[0][row] == box[0][i]:
#               print("not valid")         
# for col in range(1,len(box)):
#     if box[0][row] == box[col][0]:
#        print("not valid")

# for row1 in range(1,len(box),3):
#     for j in range(0,len(box),2):
#        if box[0][row1] == box[0][j]:
#            print("not valid")
# for col1 in range(1,len(box)):
#     if box[0][row1] == box[col1][1]:
#        print("not valid") 

# for row2 in range(len(box)-1,-1,-3):
#     for k in range(0,len(box)-1):
#        if box[0][row2] == box[0][k]:
#           print("not valid")
# for col2 in range(1,len(box)):
#     if box[0][row2] == box[col2][2]:
#        print("not valid")


# # #****************************************************

# for row21 in range(0,len(box),3):
#     for l in range(1,len(box)):  
#        if  box[1][row21] == box[1][l]:
#               print("not valid")       
# for col21 in range(0,len(box),2):
#     if  box[1][row21] == box[col21][0]:
#        print(" not valid")

# for row21 in range(1,len(box),3):
#     for m in range(0,len(box),2):
#         if box[1][row21] == box[1][m]:  
#             print("not valid")
# for col21 in range(0,len(box[1]),2):
#      if box[1][row21] == box[col21][1]:
#        print("not valid")


# for row22 in range(len(box)-1,-1,-3):
#   for k in range(0,len(box)-1):
#        if box[1][row22] == box[1][k]:
#               print("not valid")
# for col22 in range(0,len(box),2):
#      if box[1][row22] == box[col22][2]:
#        print("not valid")

# # #*************************************************

# for row31 in range(0,len(box),3):
#     for o in range(1,len(box)):
#        if box[2][row31] == box[2][o]:
#              print("not valid")
# for col31 in range(0,len(box)-1):
#     if box[2][row31] == box[col31][0]:
#        print("not valid")

# for row32 in range(1,len(box),2):
#     for p in range(0,len(box),2):
#        if box[2][row32] == box[2][p]:
#               print("not valid")
# for col32 in range(0,len(box)-1):
#        if box[2][row32] == box[col32][1]:
#               print("not valid")

# for row33 in range(len(box)-1,-1,-3):
#        for q in range(0,len(box)-1):
#               if box[2][row33] == box[2][q]:
#                    print("not valid")                        
# for col33 in range(0,len(box)-1):
#        if box[2][row33] == box[col33][2]:
#               print("not valid")

# #rows by rows checking 
# hset = set()
# for i in range(3):
#        for j in range(3):
#               if grid[i][j] in hset:
#                   print(False)
#               else:
#                      hset.add(grid[i][j])
#               #hset = set()
# print(hset)
# #cols by cols checking
# hset = set()
# for i in range(3):
#        for j in range(3):
#               if grid[j][i] in hset:
#                   print(False)
#               else:
#                      hset.add(grid[j][i])
#               #hset = set()
# print(hset)   





def isRowValid(row_num):
    return len(set(sudoku[row_num])) == 9

#validate column
def isColValid(col_num):
    col = [item[col_num] for item in sudoku]
    return len(set(col)) == 9

#validate cell
def isCelValid(cel_row, cel_col):
    vals = sudoku[cel_row][cel_col: cel_col+3]
    vals.extend(sudoku[cel_row+1] [cel_col: cel_col+3])
    vals.extend(sudoku[cel_row+2] [cel_col: cel_col+3])
    return len(set(vals)) == 9

#validate sudoku
def validateSudoku():
    for i in range(0,9):
        if not isRowValid(i):
            return False
        if not isColValid(i):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            print(i, j)
            if not isCelValid(i, j):
                return False
    return True

sudoku = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1], 
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]
 
if validateSudoku():
    print("Sudoku is valid.")
else:
    print("Sudoku is not valid.")







