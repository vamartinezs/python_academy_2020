from week2.driving_age_exercise.Person import Person
from week2.driving_age_exercise.Register import Register

# Load drivers register
users_register = Register()
users_register.show()

# Insert drivers

users_register.add(Person("Juan", "López", 33, True))
users_register.add(Person("Ana", "Méndez", 40, True))
users_register.add(Person("Juan", "López", 33, True))
users_register.add(Person("Sara", "Castano", 18, True))
users_register.add(Person("Pepito", "Perez", 5, False))

users_register.show()
