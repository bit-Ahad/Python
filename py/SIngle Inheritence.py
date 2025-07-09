class parent:
    def __init__(self,s):
        self.name = s

    def sound():
        print("Parent Class")

class child(parent):
    def __init__(self,aa):
        self.age = aa

    def sound():
        print("Child Class")
        super.sound()
