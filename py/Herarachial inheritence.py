# Hierarchical Inheritance means:
# Multiple child classes inherit from the same single parent class.

#        Parent
#        /   \
#    Child1  Child2

class Parent:
    def house(self):
        print("Parent's house")

class Child1(Parent):
    def car(self):
        print("Child1's car")

class Child2(Parent):
    def bike(self):
        print("Child2's bike")

c1 = Child1()
c1.house()  # From Parent
c1.car()

c2 = Child2()
c2.house()  # From Parent
c2.bike()