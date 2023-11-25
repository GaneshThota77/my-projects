class car():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def car_driver(self):
        print("name:",self.name,"age:",self.age)

        d = car("ganesh", 30)
        d.car_driver()
