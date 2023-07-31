class company:
    # pass
    def __init__(self, firstName, lastName, Salary):
        self.firstname = firstName
        self.lastname = lastName
        self.salary = Salary


saurabh = company()
shankar = company()

saurabh.firstname = "Saurabh"
saurabh.lastname = "Kandekar"
saurabh.salary = "44000"

shankar.firstname = "Shankar"
shankar.lastname = "Kandekar"
saurabh.salary = "44000"

print(saurabh.firstname, shankar.firstname)
