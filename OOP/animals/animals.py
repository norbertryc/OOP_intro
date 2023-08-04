class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print(f"Hi, my name is {self.name}. I am {self.age} years old.")

    def voice(self):
        #print(self.my_voice)
        print(type(self).my_voice) # Dog.my_voice lub Cat.my_voice


class Dog(Animal):
    my_voice = "Wof!Wof"


class Cat(Animal):
    my_voice = "Meow!Meow"
