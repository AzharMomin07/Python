class Employee:
    def __init__(self, firstName, lastName, age):
        self.FirstName = firstName
        self.LastName = lastName
        self.Age = age

    @staticmethod
    def isOpen(day):
        if day == "sunday":
            return False
        else:
            return True


# saurabh = Employee("saurabh","Kandekar",22)  
# print(saurabh.isOpen("monday")
# )   
print(Employee.isOpen("monday"))
