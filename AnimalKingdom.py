class Animal:

    def speak(self):
        raise NotImplemented("Speak method must be defined in the subclasses.")

class Dog(Animal):

    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

dog = Dog().speak()
cat = Cat().speak()