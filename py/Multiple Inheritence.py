# A child class having more than one parent
# Method Resolution .mro()

class Father:
    def skills(self):
        print("Father: Gardening, Programming")

class Mother:
    def skills(self):
        print("Mother: Cooking, Painting")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Child: Dancing")

c = Child() 
c.skills()
print(Child.mro())