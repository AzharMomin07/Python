class Employee:
    def __init__(self,firstName,lastName,age):
        self.FirstName = firstName
        self.LastName = lastName
        self.Age = age


class Person(Employee):
    pass

saurabh = Person("saurabh","kandekar",22)
print(saurabh.FirstName)
        