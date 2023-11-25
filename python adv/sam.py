
lst = ['a','is','this','them','it','john']
sub ="john has to report them it he is late".split()

#output=[]
res =''
#output = "Jhon has to report Them It he Is late"
'''print(sub)
for i in sub:
    if i in lst:
        output.append(i.capitalize())
        print(output)
    elif i not in lst:
        output.append(i)
print(output)
for j in output:
    res=res+j+' '
print(res)'''

new=[i.capitalize() if i in lst else i for i in sub]              
for j in new:
    res=res+j+' '
print(res)