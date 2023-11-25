dict={}
def func():
    list_2=['ganesh','danny','venky','zimmy','zaajo']
    list=[1,2,3,4,5]
    for i,j in zip(list,list_2):
        keys=i
        values=j
        dict[keys]=values
    print(dict)

func()

 

