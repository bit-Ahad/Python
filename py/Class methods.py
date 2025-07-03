class person:
    person = "shoehow"  # Class variable

    def __init__(self, na):
        self.name = na    # Instance variable

    @classmethod
    def func(cls):
        print(cls.person)

    @classmethod
    def change(cls, af):
        cls.person = af

a = person("ahad")
b = person("sdfs")

a.func()                     # Output: shoehow
b.change("NononNNOOnnoo")   # Changes the class variable
b.func()                     # Output: NononNNOOnnoo

print(person.person)        # Output: NononNNOOnnoo
