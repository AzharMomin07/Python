class Employee:

    def __init__(self, firstName, lastName, salary):
        self.FirstName = firstName
        self.LastName = lastName
        self.Salary = salary


class Programmer(Employee):
    def __init__(self, firstName, lastName, salary, ):
        super().__init__(firstName, lastName, salary)

    def _add_(self, other):
        return self.Salary + other.Salary

    def __repr__(self):
        return "Employee({},{},{})".format(self.FirstName, self.LastName, self.Salary)

    def __str__(self):
        return "The Name Of Programmer is {}".format(self.FirstName)



saurabh = Programmer("saurabh", "kandekar", 22)
shankar = Programmer("shankar", "kandekar", 22)
print(saurabh._add_(shankar))
print(repr(saurabh))
print(str(saurabh))
