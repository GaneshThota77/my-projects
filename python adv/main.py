import json

# serializing
employee={'name':'durga',
         'age':35,
         'salary':25000,
         'married':True,
         'havegirlfriend':None
         }
json_string =json.dumps(employee,indent=4)
print(json_string)

with open('emp.json','w') as f:
    json.dump(employee,f,indent=4)

