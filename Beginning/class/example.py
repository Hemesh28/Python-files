class Dog:
    species= "Cannis familiaris "
    def __init__(self, name, age,color):
        self.name=name
        self.age=age
        self.color=color
    def description(self):
        return f"{self.name} is {self.age} years old "
    def speak(self,sound):
        return f"{self.name} says {sound}"
    def walk(self,style):
        return f"{self.name} walks in {style} "

my_dog = Dog("Serpa",6,"red")
print(my_dog.description())
print(my_dog.speak("Woof Woof"))
print(my_dog.species)
print(my_dog.name)
print(my_dog.age)
print(my_dog.walk("random"))