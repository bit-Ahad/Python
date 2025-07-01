# Getter and setter should be of same name

class person:
    def __init__(self):
        self.value = 0

    # Getter
    @property
    def value(self):
        print(f"Value is : {self._value}")

    # Setter
    @value.setter
    def value(self,x):
        self._value = x

a = person()
a.value = 30
print(a.value)