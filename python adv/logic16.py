class Data:

    def input_data(self,name,count):
        for i in name:
            count+=1
        return count 

    def length(self):
        name = int(input('enter ur name:'))
        if name:
            return (Data.input_data(self,name=name,count=0))
obj = Data()
print(f'hence the lenght of your given name is : {obj.length()}')
