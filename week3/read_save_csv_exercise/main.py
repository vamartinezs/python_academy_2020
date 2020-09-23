from week3.read_save_csv_exercise.Employee import Employee
from week3.read_save_csv_exercise.csv_helpers import ManagerCSV


# Set the path to the csv file
PATH_CSV_FILE= "persistence/employees.csv"

# Instantiate the CSV manager
csv_manager = ManagerCSV.ManagerCsv(PATH_CSV_FILE)

# create data to store in csv file
employees = [
    Employee("Luis", "42", "3142536323", "Street 4 - 42 ", "Spain"),
    Employee("Ana", "35", "3142536322", "Street 5 - 43 ", "France"),
    Employee("Carlos", "42", "3142536623", "Street 6 - 44", "Mexico"),
    Employee("Marisol", "29", "3142536323", "Street 7 - 45 ", "Guatemala")
]

csv_manager.write_csv_file(employees)

# create instance to retrieve data from csv file
csv_manager.read_csv_file()

# get employees data histograms
csv_manager.get_csv_info()