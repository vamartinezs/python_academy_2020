from week3.read_save_csv_exercise.csv_helpers.InformCSV import InformCSV
from week3.read_save_csv_exercise.csv_helpers.ReaderCSV import ReaderCSV
from week3.read_save_csv_exercise.csv_helpers.SaverCSV import SaverCSV


class ManagerCsv:

    def __init__(self, file_path=None):
        self.reader = ReaderCSV()
        self.writer = SaverCSV()
        self.info = InformCSV()

        if file_path is not None:
            self.file_path = file_path
        else:
            self.file_path = "../persistence/*.csv"

        print("Information Object for CSV file was created")

    def read_csv_file(self):
        self.reader = ReaderCSV(self.file_path)
        return self.reader.get_employees(self.file_path)

    def write_csv_file(self, employees=None):
        self.writer = SaverCSV(self.file_path)
        self.writer.write_employees(self.file_path,employees)

    def update_csv_filee(self,employees=None):
        self.writer = SaverCSV(self.file_path)
        self.writer.update_employees(self.file_path,employees)

    def get_csv_info(self, file_path=None):
        self.info = InformCSV(file_path)
        return self.info.get_data_information(self.file_path)