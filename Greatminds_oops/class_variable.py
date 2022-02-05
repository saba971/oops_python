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

app1=octafit("Arun","palani",20)
app2=octafit("Kumar","coimbatore",17)
#print(app2.register())
#app1.fees(500)
print(app1.fees(500))
print(app1.fixamt)
print(app1.__dict__)
print(app2.__dict__)

#printing no.of.object that is number of customer.
print(app1.no_of_customer)