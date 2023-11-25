# st = "this is python"
# words = st.split()
# for i in range(len(words)):
#     if words[i] == "is":
#         words.pop(i)
#         words.insert(0, "is")
#         break
# new_st = " ".join(words)
# rev_st = ""
# for i in range(len(new_st)-1, -1, -1):
#     rev_st += new_st[i]
# print(rev_st)


# st = "this is python"
# word = st[::-1].split()
# for j in range(len(word)):
#     if word[j] == 'si':
#         word.pop(j)
#         word.insert(0, 'si')
# print(word)

# nums = [1,2,3,4,5]
# res = 5
# l = []
# for i in range(len(nums)):
#     for j in range(1,len(nums)):
#         k = nums[i] + nums[j]
#         if k == res :
#             if k not in l:
#                l .append(nums[i])
#                l .append(nums[j])
        
# print(l)

# nums = [1, 2, 3, 4, 5]
# res = 5
# l = []
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == res:
#             pair = (nums[i], nums[j])
#             if pair not in l:
#                 l.append(pair)

# print(l)
#from functools import reduce
# lst = [1,2,3,4,5,6,7,8]
# lsts = []
# for i in lst:
#     if i%2 == 0:
#         lsts.append(i)
#         txt = reduce(lambda x,y : x+y, lsts)
# print(txt)



# def sum_of_evens(lst):
#     return reduce(lambda x, y: x + y, (i for i in lst if i % 2 == 0), 0)
# print(sum_of_evens(lst = [1,2,3,4,5,6,7,8]))

# def second_highest(lst):
#     unique_lst = sorted(list(set(lst)), reverse=True)
#     if len(unique_lst) < 2:
#         return None
#     return unique_lst[1]
# print(second_highest(lst = [1,2,3,4,5,6]))

# lst = [1,5,3,9,8,4,2,7,6]
# val1,val2 = lst[0],lst[1]
# n = len(lst)
# for i in range(2,n):
#     if lst[i] > val1:
#         val2 = val1
#         val1 = lst[i]

#     elif (lst[i] >val2):

#         val2 = lst[i]
    
# print(val2)

# def second_largest(lst):
#     largest = second_largest = float('-inf')
#     for num in lst:
#         if num > largest:
#             second_largest = largest
#             largest = num
#         elif num > second_largest and num != largest:
#             second_largest = num
#     return second_largest


# inp = [2, 4, 5, 1, 3, 5, 4]
# #op = [(2, 4), (5, 1), (3, 3), (4, 2)]
# target = 6
# val = len(inp)
# empty = []
# for i in range(val):
#     for j in range(i+1,val):
#         if inp[i] + inp[j] == target:
#             lt = (inp[i],inp[j])
#             empty.append(lt)
#         elif inp[i] + inp[i] == target:
#             lt = (inp[i],inp[i])
#             empty.append(lt)
# print(empty)

# def find_pairs(numbers, target):
#     visited = set()
#     pairs = []
#     for i, num1 in enumerate(numbers):
#         num2 = target - num1
#         if num2 in visited:
#             pairs.append((num2, num1))
#         visited.add(num1)
#     return pairs

# inp = [2, 4, 5, 1, 3, 5, 4]
# target = 6
# pairs = find_pairs(inp, target)
# print(pairs) # Output: [(4, 2), (1, 5), (3, 3), (5, 1)]


# def longest_consecutive_sequence(nums):
#     num_set = set(nums)
#     max_length = 0
    
#     for num in num_set:
#         if num - 1 not in num_set:
#             curr_num = num
#             curr_length = 1
            
#             while curr_num + 1 in num_set:
#                 curr_num += 1
#                 curr_length += 1
            
#             max_length = max(max_length, curr_length)
    
#     return max_length
# nums = [1, 9, 3, 10, 4, 20, 2]
# print(longest_consecutive_sequence(nums))

# inp = [5,10,2,6,8]
# #op = (10,8)
# val = sorted(inp)
# res = val[-1] + val[-2]
# for i in range(len(val)):
#     for j in range(i+1, len(val)):
#         if val[i] + val[j] == res:
#             txt = (val[i],val[j])
# print(txt)

# def find_largest_sum_pair(lst):
#     max_sum = lst[0] + lst[1]
#     max_pair = (lst[0], lst[1])
#     for i in range(2, len(lst)):
#         if lst[i] > max_pair[0] or lst[i] > max_pair[1]:
#             if max_pair[0] > max_pair[1]:
#                 max_pair = (lst[i], max_pair[0])
#             else:
#                 max_pair = (lst[i], max_pair[1])
#         if lst[i] + max_pair[0] > max_sum:
#             max_sum = lst[i] + max_pair[0]
#             max_pair = (lst[i], max_pair[0])
#         elif lst[i] + max_pair[1] > max_sum:
#             max_sum = lst[i] + max_pair[1]
#             max_pair = (lst[i], max_pair[1])
#     return max_pair
# print(find_largest_sum_pair(lst = [5,10,2,6,8]))


#inp = [2,4,6,8,10]
#op = 480
# inp = [1, 2, 3, 4]
# #op = 24
# fm = inp[0]
# sm = inp[1]
# tm = inp[2]
# for i in range(3,len(inp)):
#     if inp[i] > fm:
#         fm = sm
#         sm = inp[i]
#     elif inp[i] > sm:
#         sm = inp[i]

#     txt = (fm * sm * tm)
# print(txt)

# stng =  "Hello, world!"
# inp = 'Hello'
# for i in inp:
#     if i == stng:
#         print(True)
#     else:
#         print(False)
# def can_form_string(s1: str, s2: str) -> bool:
#     # Convert the strings to lowercase and remove whitespace
#     s1 = s1.lower().replace(" ", "")
#     s2 = s2.lower().replace(" ", "")

#     # Create a dictionary to store the character counts in the first string
#     char_counts = {}
#     for c in s1:
#         if c in char_counts:
#             char_counts[c] += 1
#         else:
#             char_counts[c] = 1

#     # Check if the characters in the second string can be formed from the first string
#     for c in s2:
#         if c in char_counts and char_counts[c] > 0:
#             char_counts[c] -= 1
#         else:
#             return False

#     return True


# inp = [3, 5, 7, 2,8, 9, 1]
# #op = [(3, 7), (2, 8), (9, 1)]
# empty = []
# target = 10
# for i in range(len(inp)):
#     for j in range(i+1, len(inp)):
#         if inp[i] + inp[j] == target:
#             txt = (inp[i],inp[j])
#             empty.append(txt)
# print(empty)

# inp = [1, 2, 3, 4] 
# #[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
# n = 2
# dic = {}
# empthy = []
# for i in range(len(inp)):
    
    
#     for j in range(i+1 ,len(inp)):
#         txt =(inp[i],inp[j])
#         empthy.append(txt)
# print(empthy)


# inp = [1, 3, 5, 7, 9]
# target=  12
# empty = []
# for i in range(len(inp)):
#     for j in range(len(inp)-1,-1,-1):
#         if inp[i] + inp[j] == target:   
#             txt = (inp[i],inp[j])
#             empty.append(txt)
#         break
# print(empty)

# num = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# for i in num:
#     if i%3 == 0 & i%5 == 0:
#        sum+=1 
#     # elif (i%3 ==0) != (i%5==0):
# print(sum)
    
# inp = [10, 4, 3, 50, 23, 90]
# lst = []
# max = inp[0]
# for i in inp:
#     if max < i:
#         max = i
#         lst.append(max)
#         inp.remove(max(inp))
# print(max)

# s = "cbaebabacd"
# p = "abc"
# dic = {}
# lst = []
# for k,i in enumerate(s):
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i] = 1
# for j in p:
#     if j in dic and dic[j] > 0:
#         dic[j] -= 1
#         lst.append(s.index(j))
# print(lst)

# s = "cbaebabacd"
# p = "abc"
# dic = {}
# lst = []

# # count the occurrence of each character in "p"
# for i in s:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1

# # check if the dictionary contains all the characters in "p" with count greater than zero
# for k, i in enumerate(p):
#     if i in dic and dic[i] > 0:
#         dic[i] -= 1
#         if len(lst) == 0:
#             # append the index of the first character in "p"
#             lst.append(k - len(p) + 1)
#             if len(lst) == len(p):
#                 break
# print(tuple(lst))

# s = "cbaebabacdabc"
# p = "abc"
# # Output: [0, 6]

# p_dict = {}
# for c in p:
#     if c in p_dict:
#         p_dict[c] += 1
#     else:
#         p_dict[c] = 1

# window = {}
# for c in s[:len(p)]:
#     if c in window:
#         window[c] += 1
#     else:
#         window[c] = 1

# output = []
# if window == p_dict:
#     output.append(0)

# for i in range(len(p), len(s)):
#     left_char = s[i-len(p)]
#     right_char = s[i]
    
    
    # if left_char in window:
    #     window[left_char] -= 1
    #     if window[left_char] == 0:
    #         del window[left_char]
    # if right_char in window:
    #     window[right_char] += 1
    # else:
    #     window[right_char] = 1
    
    # if window == p_dict:
    #     output.append(i-len(p)+1)

# print(output) 

#s = 'ganensh'
# s1 = ''
# for i in s:
#     if i == 'n':
#         s1 += 'z'
#     else:
#         s1 += i
# print(s1) # Output: "gazesh"

# b = ''
# for j, i in enumerate((s)):
#     if j == 2:
#         b += i.replace('n','z') 
        
#     else:
#         b+=i
# print(b)

# b = ''
# for j, i in enumerate((s)):
#     if j == 2:
#         b += i.replace('n','z') 
        
#     else:
#         b+=i
# print(b)
# s = 'ganesh thota'.split()
# b = ''
# for i in (s):
#     if 'thota' in i:
#         b += i.replace('thota','T') 
        
#     else:
#         b+=i
# print(b)

# s = "aaabbbcccddee"
# s1 = ''
# for i in s:
#     if i not in s1:
#         s1+=i
# print(s1)

# dct = {'a':5,'b':6,'c':3}
# sum = 0
# for keys , values in dct.items():
#     sum+=values
# print(sum)
#empty = {}
# for i , j in dct.items()
#     keys = j
#     values = i
#     empty[keys] = values
#print(empty)

s = 'hello world'.split()
# s1 = s.title()
# print(s1)
#print(s)
s1 = ''
for i in s:
    s1+=i.capitalize() + ' '
print(s1)
    
# st = 'ganesh'
# s = ''
# for i,j in enumerate(st):
#     if i == 2 or i == 5:
#         s+=j.replace('n','c').replace('h','H')
#     # elif i == 5:
#     #     s+=j.replace('h','z')
#     else:
#         s+=j
# print(s)

# st = 'hello world'
# s = ''
# for i in st:
#     if 'h' in st or 'w' in st:
#         s+= i.replace('h','H').replace('w','W')    
#     else:
#         s+=i
# print(s)








