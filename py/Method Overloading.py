# Different classes, typically involving inheritance. The child class redefines a method of the parent class.
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):  # Overrides parent method
        print("Dog barks")

d = Dog()
d.speak()  # Output: Dog barks
