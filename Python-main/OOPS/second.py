class company:
    # pass
    def __init__(self, firstName, lastName, Salary):
        self.firstname = firstName
        self.lastname = lastName
        self.salary = Salary


saurabh = company("saurabh", "kandekar", 44000)
shankar = company("shankar", "kandekar", 45000)

print(shankar.salary, saurabh.salary)
