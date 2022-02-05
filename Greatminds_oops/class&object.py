import os
import re


class octafit:
    def __init__(self,name,place,age):
        self.name=name
        self.place=place
        self.age=age
    def register(self):
        if self.age <18:
            app=f"Hi {self.name}.your are not eligible."
        if self.age >18 and self.age<40:
            app=f"Hi {self.name}.welcome to octafit!"
        return app

app1=octafit("Arun","palani",20)
app2=octafit("Kumar","coimbatore",17)
print(app2.register())

