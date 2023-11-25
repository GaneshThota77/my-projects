a = "The7 Fox730 jumpsun9 derthe62 Ta1ble72"
#print(inp)
#output77309 62172
num=''
for i in a:
    if i.isdigit():
        num+=i
        #print(num)       
First_part = num[:5]
scd_part = num[5:]
last_result=First_part+" "+scd_part
print(last_result)
