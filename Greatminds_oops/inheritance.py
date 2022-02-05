class octafit:
    #class varaiable
    fixamt=1000
    #calculating no.of.object.
    no_of_customer=0
    def __init__(self,name,place,age):
        #below are instance variable
        self.name=name
        self.place=place
        self.age=age
        octafit.no_of_customer=octafit.no_of_customer+1
    def register(self):
        if self.age <18:
            app=f"Hi {self.name}.your are not eligible."
        if self.age >18 and self.age<40:
            app=f"Hi {self.name}.welcome to octafit!"
        return app
    def fees(self,amount):
        self.amount = self.fixamt - amount
        return self.amount
class boxing(octafit):
    #overriding fixamt attirubute.
    fixamt=1500
    #super example.
    def __init__(self,name,place,age,practise):
        #Acessing init method of parent class.
        super().__init__(name,place,age)
        self.practise=practise
    
#acessing the parent class using child class
app1=boxing("Arun","palani",20,1)
app2=boxing("Kumar","coimbatore",17,3)
print(app1.name)
print(app2.name)
print(app1.register())
#all parent class (octafit) method and variable can be acessed by child class object.
print(dir(app1))
# to check the flow of child class 
print(boxing.__mro__)
#overriding fixamt attirubute.
print(app1.fixamt)

#super()->example
app3=boxing("sanjay","trichy",21,2)
print(app3.name)
print(app3.practise)
