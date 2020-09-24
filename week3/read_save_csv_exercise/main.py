from week3.read_save_csv_exercise.model.Employee import Employee
from week3.read_save_csv_exercise.csv_helpers import ManagerCSV
from week3.read_save_csv_exercise.id_generator.IdGenerator import IdGenerator
from week3.read_save_csv_exercise.utils.GeneratorLogger import Singleton


# ############################################## Second Part - Employee Records #######################################
print("\n\n # ###############################################  Second Part - Employee Records - ")


# Set the path to the csv file
PATH_CSV_FILE= "persistence/employees.csv"

# Instantiate the CSV manager
csv_manager = ManagerCSV.ManagerCsv(PATH_CSV_FILE)

# create data to store in csv file
employees = [
    Employee("Luis", "42", "3142536323", "Street 4 - 42 ", "Spain","None"),
    Employee("Ana", "35", "3142536322", "Street 5 - 43 ", "France","None"),
    Employee("Carlos", "42", "3142536623", "Street 6 - 44", "Mexico","None"),
    Employee("Marisol", "29", "3142536323", "Street 7 - 45 ", "Mexico","None")
]

csv_manager.write_csv_file(employees)

# create instance to retrieve data from csv file
csv_manager.read_csv_file()

# get employees data histograms
csv_manager.get_csv_info()


# ############################################## Third Part - Generator ID #############################################
print("\n\n # ###############################################  Third Part - Generator ID - Generator Yield Exercise - ")

employees_list = csv_manager.read_csv_file()
length_employees = len(employees_list)
id_generator = IdGenerator().id_ordered_generator(length_employees)

employees_list = [Employee(
    employee.name, employee.age, employee.phone, employee.address, employee.country, next(id_generator))
    for employee in employees_list]

csv_manager.update_csv_filee(employees_list)

print("\nREAD Employees list with ID's")
csv_manager.read_csv_file()


# ###############################################  Fourth Part - Loggin Generator
print("\n\n # ###############################################  Fourth Part - Logging Generator - Logging Exercise - ")
number_generator_instances = Singleton().getInstance().get_number_calls()
number_id_repetitions = Singleton().getInstance().get_repetition_id()

print(" Times the ID Generator was called : {}".format(number_generator_instances))
print(" Times the created ID was repeeated  : {}".format(number_id_repetitions))