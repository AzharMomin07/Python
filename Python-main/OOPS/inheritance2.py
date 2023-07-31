class Employee:
    increment = 2

    def __init__(self, firstName, lastName, age):
        self.FirstName = firstName
        self.LastName = lastName
        self.Age = age


class Programmer(Employee):
    def __init__(self, firstName, lastName, age, programingLanguage, Experiance):
        super().__init__(firstName, lastName, age)
        self.ProgramingLanguage = programingLanguage
        self.experiance = Experiance

    def increase(self):
        self.age = int(self.age * (self.increment + 0.2))
        return self.age


saurabh = Programmer("saurabh", "kandekar", 22, "Java", " 2 years")
print(saurabh.FirstName)
saurabh.increase()
print(saurabh.Age)
