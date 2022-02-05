import os
import re


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
    #This how we declare a class method.
    @classmethod
    def changefee(cls,amnt):
        cls.fixamt=amnt
    @classmethod
    def newcustomer(cls,new_customer):
        name,place,age=new_customer.split(",")
        return octafit(name,place,age) 
        #in return instaed of octafit you can use "cls"(because it contains classname)
    #In static method,object(self) and classname(cls) should not be passed.In this case we can go for static.
    @staticmethod
    def fitmethod(mywish):
        fit_tech=["boxing","HIIT","Yoga"]
        if mywish in fit_tech:
            return "We have training which you choosed"
        else:
            return "We are not training which you choosed"


app1=octafit("Arun","palani",20)
app2=octafit("Kumar","coimbatore",17)

print(app1.fixamt)
print(app2.fixamt)
#changing the class variable using class method.
octafit.changefee(1500)
#If we call the same function using object also same result.class name will be passed first.
app1.changefee(1500)
print(app1.fixamt)
print(app2.fixamt)

#example for class method.
new_customer="mani,dindigul,45"
app3=octafit.newcustomer(new_customer)
print(app3.name)

#static method.
print(app1.fitmethod("martialarts"))
print(app2.fitmethod("Yoga"))

