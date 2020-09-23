from week3.read_save_csv_exercise.csv_decorators.csv_decorators import write_employees_records, update_employees_records


class SaverCSV:

    def __init__(self, file_path=None):
        if file_path is not None:
            self.file_path = file_path
        else:
            self.file_path = "../persistence/*.csv"
        print("Object Saver CSV file was created")

    def write_employees(self, file_path=None, employees=None):
        if file_path is not None:
            write_employees_records(file_path, employees)
        else:
            write_employees_records(self.file_path, employees)

    def update_employees(self,file_path=None, employees=None):
        if file_path is not None:
            update_employees_records(file_path,employees)
        else:
            update_employees_records(file_path,employees)


