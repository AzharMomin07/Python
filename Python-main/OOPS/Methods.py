class Employee:
    plus = 2

    def __init__(self, firstname, lastname, age):
        self.firstName = firstname
        self.lastName = lastname
        self.Age = age

    def increase(self):
        self.Age = int(self.Age * self.plus)

    @classmethod
    def change_increment(cls, amount):
        cls.plus = amount


saurabh = Employee("saurabh", "kandekar", 22)
shankar = Employee("shankar", "kandekar", 22)

print(saurabh.Age)
Employee.change_increment(3)
saurabh.increase()
print(saurabh.Age)

# using method increase age
