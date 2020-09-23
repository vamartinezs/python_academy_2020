import csv

from week3.read_save_csv_exercise.Employee import Employee


def get_csv_reader(func):
    def wrapper(*args, **kwargs):
        print("Retrieving Employees list")
        employees = func(*args, **kwargs)
        print(f"Retrieved a total of {len(employees)} employees")
        return employees

    return wrapper


def save_csv_reader(func):
    def wrapper(*args, **kwargs):
        print("Starting writing process on csv file")
        csv_writer = func(*args, **kwargs)
        print(f"Ended writing {len(args[1])} records")

    return wrapper


@get_csv_reader
def get_employees(file_path):
    with open(file_path) as csv_file:
        list_employees = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            list_employees.append(Employee(row[0], row[1], row[2], row[3], row[4],row[5]))
        csv_file.flush()
        csv_file.close()
        return list_employees


@save_csv_reader
def write_employees_records(file_path=None, employees=None):
    print(file_path)
    with open(file_path, mode='a') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for employee in employees:
            employee_writer.writerow(employee.get_raw_data())
        employee_file.flush()
        employee_file.close()


def get_file_information(file_path=None):
    employees = get_employees(file_path)
    country_hist = get_country_histogram([employee.country for employee in employees])
    employees_ages = get_employees_ages([employee.age for employee in employees])
    return [country_hist, employees_ages]


def histogram(func):
    def wrapper(*args, **kwargs):
        histogram_elements = {}
        list_elements = func(*args, **kwargs)
        for key in list_elements:
            if key in histogram_elements:
                histogram_elements[key] += 1
            else:
                histogram_elements[key] = 1
        return histogram_elements

    return wrapper


@histogram
def get_employees_ages(ages_list):
    return ages_list


@histogram
def get_country_histogram(countries_list):
    return countries_list
