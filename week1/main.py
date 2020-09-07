from collections import OrderedDict

from movie.data_helpers.import_helper.import_dataset import get_movie_dataset
from movie.data_helpers.filters.filter import *
import time

# **************************************************
# Title  : Movie dataset exercisee
# Author : Victor Alfonso Martínez Solarte
# Description : Python Academy 2020 - Globant
# **************************************************


MOVIE_DATASET_PATH = "dataset/movie_metadata.csv"
movie_dataset = get_movie_dataset(MOVIE_DATASET_PATH)

dataset_title = movie_dataset[0]
dataset_samples_number = len(movie_dataset)

# ======================================================================================================================
# - How many Black & White and color movies are in the list?

start = time.time()

all_color_types = set([(movie_dataset[x][0]) for x in range(1, dataset_samples_number)])
# all_color_types ={'', 'Color', 'Blackand White'}

black_and_white_counter = sum([movie_dataset[x][0] == 'Blackand White' for x in range(1, dataset_samples_number)])
elapsed_time = time.time() - start

# 209 Black and White movies - elapsed time : 6 ms
print("Number of Black and White Movies : {} - Elapsed time : {} seconds".format(black_and_white_counter, elapsed_time))

# ======================================================================================================================
# How many movies were produced by director in the list?
start = time.time()

all_directors_list = [(movie_dataset[x][1]) for x in range(1, dataset_samples_number)]
director_occurrences = get_histogram_of(all_directors_list)

elapsed_time = time.time() - start

# Director Histograms - 5.8 ms
print("Director per movie quantity {}, \n\n Elapsed time : {} seconds ".format(director_occurrences, elapsed_time))





