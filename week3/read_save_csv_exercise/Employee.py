class Employee:

    def __init__(self, name, phone, address, country):
        self.name = name
        self.phone = phone
        self.address = address
        self.country = country

    def __str__(self):
        return "Name : {} Phone : {} Address : {} Country {}".format(self.name, self.phone, self.address, self.country)


employees = [
    Employee("Luis", "3142536323", "Street 4 - 42 ", "Spain"),
    Employee("Ana", "3142536322", "Street 5 - 43 ", "France"),
    Employee("Carlos", "3142536623", "Street 6 - 44", "Mexico"),
    Employee("Marisol", "3142536323", "Street 7 - 45 ", "Guatemala"),
]

for emp in employees:
    print(emp)
