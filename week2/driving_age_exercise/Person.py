class Person:

    def __init__(self, name, lastname, age, allow_driving):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.allow_driving = allow_driving
        self.has_permission = False
        print("A new person register has been created")

    def __str__(self):
        return "User : {} {} is {} years old ".format(self.name, self.lastname, self.age)

    def is_allowed_to_drive(self, minimum_age):
        if 80 > self.age > minimum_age:
            self.has_permission = True
        else:
            self.has_permission = False
        self.user_msg()
        return self.has_permission

    def user_msg(self):
        if self.has_permission:
            print("{} {} is allowed to drive".format(self.name, self.lastname))
        else:
            print("{} {} is not allowed to drive".format(self.name, self.lastname))
