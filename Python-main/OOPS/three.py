class company:
    # pass
    increment = 1.5

    def __init__(self, firstName, lastName, Salary):
        self.firstname = firstName
        self.lastname = lastName
        self.salary = Salary

    def increase(self):
        self.salary = int(self.salary * company.increment)


saurabh = company("saurabh", "kandekar", 44000)
shankar = company("shankar", "kandekar", 45000)

saurabh.increase()

print(saurabh.__dict__)
saurabh.increment = "9"
print(saurabh.__dict__)
