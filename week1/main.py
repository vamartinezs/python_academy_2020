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

#start = time.time()

#all_color_types = set([(movie_dataset[x][0]) for x in range(1, dataset_samples_number)])
# all_color_types ={'', 'Color', 'Blackand White'}

#black_and_white_counter = sum([(movie_dataset[x][0] == 'Blackand White' or movie_dataset[x][0] == 'Color')
#                               for x in range(1, dataset_samples_number)])
#elapsed_time = time.time() - start

# 5024 Black and White and color movies are present - elapsed time : 6 ms
#print("Number of Black and White Movies : {} - Elapsed time : {} seconds".format(black_and_white_counter, elapsed_time))

# ======================================================================================================================
# How many movies were produced by director in the list?
#start = time.time()

#all_directors_list = [(movie_dataset[x][1]) for x in range(1, dataset_samples_number)]
#director_occurrences = get_histogram_of(all_directors_list)
#director_occurrences = [(k, director_occurrences[k]) for k in sorted(director_occurrences, key=director_occurrences.get, reverse=True)]
#elapsed_time = (time.time() - start)

# Director Histograms - 6.8 ms
#print("Director per movie quantity {}, \n\n Elapsed time : {} seconds ".format(director_occurrences, elapsed_time))

# ======================================================================================================================
# Which are the 10 less criticized movies in the list?

#start = time.time()

all_movies_titles = [(movie_dataset[x][10]) for x in range(0, dataset_samples_number)]
#all_movies_critics = [(movie_dataset[x][2]) for x in range(0, dataset_samples_number)]

#titles_critics = [(all_movies_titles[k], all_movies_critics[k]) for k in range(1, dataset_samples_number-1)]
#titles_critics = list(filter(lambda k: k[0] != '', titles_critics))
#titles_critics.sort(reverse=True)
#titles_critics = titles_critics[0:10]

#elapsed_time = (time.time() - start)

#print("10 less criticized movies are : '\n' {} \n\nElapsed time {} seconds ".format(titles_critics, elapsed_time))

# ======================================================================================================================
# Which are the 20 longest-running movies in the list?

#start = time.time()

#all_movies_duration = [(movie_dataset[x][3]) for x in range(0, dataset_samples_number)]
#titles_duration = [(all_movies_titles[k], all_movies_duration[k]) for k in range(1, dataset_samples_number-1)]
#titles_duration = list(filter(lambda k: k[0] != '', titles_duration))
#titles_duration.sort()
#titles_duration = titles_duration[0:20]

#elapsed_time = (time.time() - start)
#print("20 longest movies are : '\n' {} \n\nElapsed time {} seconds ".format(titles_duration, elapsed_time))

# ======================================================================================================================
# Which are the top 5 movies that raised more money in the list?

start = time.time()

all_movies_profit = [(movie_dataset[x][8]) for x in range(0, dataset_samples_number)]
titles_profit = [(all_movies_titles[k], all_movies_profit[k]) for k in range(1, dataset_samples_number-1)]
titles_profit = list(filter(lambda k: k[0] != '' and k[1] != '', titles_profit))
titles_profit.sort(key=lambda x: int(x[1]), reverse= True)
titles_profit = titles_profit[0:5]

elapsed_time = (time.time() - start)

# ('CCH Pounder', '760505847'), ('Leonardo DiCaprio', '658672302'), ('Bryce Dallas Howard', '652177271'),
# ('Chris Hemsworth', '623279547'), ('Chris Hemsworth', '623279547')]
print("5 more profitable movies are : '\n' {} \n\nElapsed time {} seconds ".format(titles_profit, elapsed_time))

# ======================================================================================================================
# Which are the top 5 movies that made the least money in the list?
start = time.time()

titles_profit = [(all_movies_titles[k], (all_movies_profit[k])) for k in range(1, dataset_samples_number-1)]
titles_profit = list(filter(lambda k: k[0] != '' and k[1] != '', titles_profit))
titles_profit.sort(key=lambda x: int(x[1]), reverse=False)
titles_profit = titles_profit[0:5]

elapsed_time = (time.time() - start)

# [('Michael Jai White', '162'), ('Lynn Cohen', '703'), ('David Keith', '721'),
# ('William Kircher', '728'), ('Jim Broadbent', '828')]
print("5 less profitable movies are : '\n' {} \n\nElapsed time {} seconds ".format(titles_profit, elapsed_time))
