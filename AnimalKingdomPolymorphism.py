class Animal:
    def speak(self):
        raise NotImplemented("Speak function must be defined in the subclasses.")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Parrot(Animal):
    def speak(self):
        print("Squawk")

def describe_pet(animal):
    animal.speak()

dog = Dog()
cat = Cat()
parrot = Parrot()

describe_pet(dog)
describe_pet(cat)
describe_pet(parrot)