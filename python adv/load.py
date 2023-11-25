import json
with open('emp.json','r') as f:
    dict_obj=json.load(f)
print('emp name:',dict_obj['name'])
print('emp age:',dict_obj['age'])

# for k,v in dict_obj.items():
#     print('{} : {}'.format(k,v))