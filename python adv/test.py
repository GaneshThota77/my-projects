import json
# deserialization
employee='''{
    "name":"durga",
    "age":35,
    "salary":25000,
    "married":true,
    "havegirlfriend":null    
}'''
dict_obj =json.loads(employee)
print(dict_obj)
# print('employee name:{}'.format(dict_obj['name']))
# print('emp name:',dict_obj['age'])
for k,v in dict_obj.items():
    print('{} : {}'.format(k,v))
    