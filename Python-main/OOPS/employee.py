class company:
    no_of_Emmployee = 0

    def __init__(self, firstName, lastName, Salary):
        self.firstname = firstName
        self.lastname = lastName
        self.salary = Salary
        company.no_of_Emmployee += 1

    def increase(self):
        self.salary = int(self.salary * company.increment)


print(company.no_of_Emmployee)

saurabh = company("saurabh", "kandekar", 44000)
print(company.no_of_Emmployee)
shankar = company("shankar", "kandekar", 45000)
print(company.no_of_Emmployee)
