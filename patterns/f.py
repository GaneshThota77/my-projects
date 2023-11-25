a='abc'
b='xyz'
new_a = b[:2] + a[2:] # xy+c
new_b = a[:2] + b[2:] # ab+ z

print (new_a+','+new_b) # xyc abz