class Employee:

    def __init__(self, firstname, lastname, age):
        self.firstName = firstname
        self.lastName = lastname
        self.Age = age

    @classmethod
    def from_str(cls, emp_String):
        firstname, lastname, age = emp_String.split("-")
        return cls(firstname, lastname, age)


saurabh = Employee("saurabh", "kandekar", 22)

sk = Employee.from_str("sk-kk-22")

shankar = Employee("shankar", "kandekar", 22)

print(sk.firstName)
print(sk.lastName)
print(sk.Age)
