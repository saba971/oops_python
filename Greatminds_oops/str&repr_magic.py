class octafit:
    def __init__(self,name,age):
        self.name =name
        self.age= age
    def __str__(self):
        return self.name
    def __repr__(self):
        return f'octafit({self.name})'


#In backgorund it will call __str__ magic method.when we gave it as a string.
app1=octafit("saba","24")
print(app1)

#In background it will call ___repr__ magic method.when we gave object as a list.
print([app1])