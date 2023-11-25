s = 'abcbbadc'
count = 0
d = {}
for i in (s):
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
# print(d)
#max_key = max(zip(d.values(), d.keys()))[1]
max_key = max(d, key = d.get)
print(max_key)


