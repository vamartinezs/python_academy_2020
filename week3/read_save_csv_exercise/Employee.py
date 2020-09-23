class Employee:

    def __init__(self, name, age, phone, address, country):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.country = country

    def __str__(self):
        return "Name : {} Phone : {} Address : {} Country {}".format(self.name, self.age, self.phone, self.address, self.country)

    def get_raw_data(self):
        return [self.name, self.age, self.phone, self.address, self.country]


