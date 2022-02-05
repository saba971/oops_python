class customer:
    def __init__(self,name,place,age):
        self.name=name
        self.place=place
        self.age=age
class octafit(customer):
    fixamt=1000
    no_of_customer=0
    def __init__(self,name,place,age):
        super().__init__(name,place,age)
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
#(multi-level inheritance):customer->octafit->boxing.

#2.Example of heirarcy inheritance(totalcustomer,octafit->customer).
class totalcustomer(customer):
    def __init__(self,name,place,age,total=[]):
        super().__init__(name,place,age)
        self.total =total
    def showtotal(self):
        count=1
        for i in self.total:
            print(i.name)
            count+=1
        return count

#muti-level print
app1=octafit("arun","palani",21)
app2=boxing("saba","palani",25,2)
print(app1.name)
print(app2.name)
print(app2.practise)

#heirarcy print
app3=totalcustomer("mani","dindigul",45,[app1,app2])
print(app3.showtotal())
