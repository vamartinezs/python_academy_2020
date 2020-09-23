class Employee:

    def __init__(self, name, age, phone, address, country, employee_id):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.country = country
        if employee_id is not None :
            self.employee_id = employee_id
        else:
            self.employee_id = None

    def __str__(self):
        return "Name : {}, Age{}, Phone : {} Address : {} Country {}, employee_id {}".format(
            self.name, self.age, self.phone, self.address, self.country, self.employee_id)

    def get_raw_data(self):
        return [self.name, self.age, self.phone, self.address, self.country, self.employee_id]
