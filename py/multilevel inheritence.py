# A class inherits from a class, which itself inherits from another class.
# Grandparent → Parent → Child



class Grandparent:
    def home(self):
        print("Grandparent's home")

class Parent(Grandparent):
    def car(self):
        print("Parent's car")

class Child(Parent):
    def bike(self):
        print("Child's bike")

c = Child()
c.home()   # From Grandparent
c.car()    # From Parent
c.bike()   # From Child