from week3.read_save_csv_exercise.csv_decorators.csv_decorators import *


class ReaderCSV:

    def __init__(self, file_path=None):
        if file_path is not None:
            self.file_path = file_path
        else:
            self.file_path = "../persistence/*.csv"
        print("Object Reader CSV file was created")

    def print_employees(self, employees):
        for employee in employees:
            print(employee)

    def get_employees(self, file_path=None):
        employees = []
        if file_path is not None:
            employees = get_employees(file_path)
        else:
            employees = get_employees(self.file_path)
        self.print_employees(employees)
        return employees
