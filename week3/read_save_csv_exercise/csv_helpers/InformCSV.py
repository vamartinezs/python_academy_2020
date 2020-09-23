from week3.read_save_csv_exercise.csv_decorators.csv_decorators import get_file_information

class InformCSV:

    def __init__(self, file_path=None):
        if file_path is not None:
            self.file_path = file_path
        else:
            self.file_path = "../persistence/*.csv"
        print("Information Object for CSV file was created")

    def print_dictionary(self, dictionary):
        for k, v in dictionary.items():
            print(k, v)

    def get_data_information(self, file_path=None):
        data = []
        if file_path is not None:
            data = get_file_information(file_path)
        else:
            data = get_file_information(self.file_path)
        print("\nHistogram of Employees Countries")
        self.print_dictionary(data[0])
        print("\nHistogram of Employees Ages")
        self.print_dictionary(data[1])