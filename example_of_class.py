#class computer:
#    def __init__(self,cpu,ram):
#        self.cpu=cpu
#        self.ram=ram
#    def config(self):
#        print("config is",self.cpu,self.ram)

#comp1=computer('i5',16)
#comp2=computer('Ryzen 3',8)
#comp1.config()
#comp2.config()


class info: 
  def __init__(self,name,age,gender):
    self.name=name
    self.age=age
    self.gender=gender
  def persons(self): 
    print("name is",self.name,"age is",self.age,"gender is",self.gender)

"""
person1 = info()
person2 = info()

person2.name = "John"
person2.age = 39
person2.gender = "male"

info.persons(person1)
info.persons(person2)

"""

obj1 = info("John", 39, "male")
obj2 = info("Mary", 29, "female")

info.persons(obj)
obj2.persons()
