import csv


def get_movie_dataset(path):
    # Function for reading csv file and creating an object base of breaklines at the end of the row
    with open(path, newline='') as csvfile:
        return list(csv.reader(csvfile, delimiter=',', quotechar='\n'))
