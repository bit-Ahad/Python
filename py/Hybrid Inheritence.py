# Hybrid Inheritance is a combination of two or more types of inheritance like:
# Single
# Multiple
# Multilevel
# Hierarchical

    #     A
    #    / \
    #   B   C
    #    \ /
    #     D

# Base class
class A:
    def methodA(self):
        print("A")

# Class B inherits A
class B(A):
    def methodB(self):
        print("B")

# Class C also inherits A
class C(A):
    def methodC(self):
        print("C")

# Class D inherits both B and C
class D(B, C):
    def methodD(self):
        print("D")

d = D()
d.methodA()  # From A
d.methodB()  # From B
d.methodC()  # From C
d.methodD()  # From D
