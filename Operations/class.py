# classes is blueprint  that we can use represent anything  in real world or software
# classes created with properties and behavior
# object is real thing
# class is blueprint

class Person:
    def __init__(self, name, age):
        self.name = name  # properties
        self.age = age

    def walk(self):
        print(self.name + ' is walking')

    def speak(self):
        print(self.name + ' and I am ' + str(self.age) + ' Years old ')


john = Person('John', 22)  # objects
naveen = Person('Naveen', 23)

print(john.name + ' ' + str(john.age))
john.walk()
print(naveen.name + ' ' + str(naveen.age))
naveen.speak()
