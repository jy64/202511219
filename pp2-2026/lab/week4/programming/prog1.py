class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + "," + str(self.age)

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

missy = Cat('Missy', 3)
lucky = Cat('Lucky', 5)

print(missy)
print(lucky)