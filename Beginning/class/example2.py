class Car:
    Type="Maruti"
    def __init__(self, name, model):
        self.name=name
        self.model=model
    def drive(self):
        return f"{self.name} drives nicely "
    

mycar =Car("Ram", "2024")
print(mycar.drive())

print(mycar.Type)
print(mycar.name)
print(mycar.model)

