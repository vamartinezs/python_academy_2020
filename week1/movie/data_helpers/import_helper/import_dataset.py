import csv


def get_movie_dataset(path):
    with open(path, newline='') as csvfile:
        return list(csv.reader(csvfile, delimiter=',', quotechar='\n'))
