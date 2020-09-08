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

# start = time.time()

# all_color_types = set([(movie_dataset[x][0]) for x in range(1, dataset_samples_number)])
# all_color_types ={'', 'Color', 'Blackand White'}

# black_and_white_counter = sum([(movie_dataset[x][0] == 'Blackand White' or movie_dataset[x][0] == 'Color')
#                               for x in range(1, dataset_samples_number)])
# elapsed_time = time.time() - start

# 5024 Black and White and color movies are present - elapsed time : 6 ms
# print("Number of Black and White Movies : {} - Elapsed time : {} seconds".format(black_and_white_counter, elapsed_time))

# ======================================================================================================================
# How many movies were produced by director in the list?
# start = time.time()

# all_directors_list = [(movie_dataset[x][1]) for x in range(1, dataset_samples_number)]
# director_occurrences = get_histogram_of(all_directors_list)
# director_occurrences = [(k, director_occurrences[k]) for k in sorted(director_occurrences, key=director_occurrences.get, reverse=True)]
# elapsed_time = (time.time() - start)

# Director Histograms - 6.8 ms
# print("Director per movie quantity {}, \n\n Elapsed time : {} seconds ".format(director_occurrences, elapsed_time))

# ======================================================================================================================
# Which are the 10 less criticized movies in the list?

# start = time.time()

all_movies_titles = [(movie_dataset[x][11]) for x in range(0, dataset_samples_number)]
# all_movies_critics = [(movie_dataset[x][2]) for x in range(0, dataset_samples_number)]

# titles_critics = [(all_movies_titles[k], all_movies_critics[k]) for k in range(1, dataset_samples_number-1)]
# titles_critics = list(filter(lambda k: k[0] != '' and k[1] != '', titles_critics))
# titles_critics.sort(key=lambda x: int(x[1]), reverse=False)
# titles_critics = titles_critics[0:10]

# elapsed_time = (time.time() - start)

# print("10 less criticized movies are : '\n' {} \n\nElapsed time {} seconds ".format(titles_critics, elapsed_time))

# ======================================================================================================================
# Which are the 20 longest-running movies in the list?

# start = time.time()

# all_movies_duration = [(movie_dataset[x][3]) for x in range(0, dataset_samples_number)]
# titles_duration = [(all_movies_titles[k], all_movies_duration[k]) for k in range(1, dataset_samples_number-1)]
# titles_duration = list(filter(lambda k: k[0] != '' and k[1] != '', titles_duration))
# titles_duration.sort(key=lambda x: int(x[1]), reverse=True)
# titles_duration = titles_duration[0:20]

# elapsed_time = (time.time() - start)
# print("20 longest movies are : '\n' {} \n\nElapsed time {} seconds ".format(titles_duration, elapsed_time))

# ======================================================================================================================
# Which are the top 5 movies that raised more money in the list?

# start = time.time()

all_movies_profit = [(movie_dataset[x][8]) for x in range(0, dataset_samples_number)]
# titles_profit = [(all_movies_titles[k], all_movies_profit[k]) for k in range(1, dataset_samples_number-1)]
# titles_profit = list(filter(lambda k: k[0] != '' and k[1] != '', titles_profit))
# titles_profit.sort(key=lambda x: int(x[1]), reverse= True)
# titles_profit = titles_profit[0:5]

# elapsed_time = (time.time() - start)

# [('Avatar\xa0', '760505847'), ('Titanic\xa0', '658672302'), ('Jurassic World\xa0','652177271')
#  ('The Avengers\xa0', '623279547'), ('The Avengers\xa0', '623279547')]
# print("5 more profitable movies are : '\n' {} \n\nElapsed time {} seconds ".format(titles_profit, elapsed_time))

# ======================================================================================================================
# Which are the top 5 movies that made the least money in the list?
# start = time.time()

# titles_profit = [(all_movies_titles[k], (all_movies_profit[k])) for k in range(1, dataset_samples_number-1)]
# titles_profit = list(filter(lambda k: k[0] != '' and k[1] != '', titles_profit))
# titles_profit.sort(key=lambda x: int(x[1]), reverse=False)
# titles_profit = titles_profit[0:5]

# elapsed_time = (time.time() - start)

# [('Michael Jai White', '162'), ('Lynn Cohen', '703'), ('David Keith', '721'),
# ('William Kircher', '728'), ('Jim Broadbent', '828')]
# print("5 less profitable movies are : '\n' {} \n\nElapsed time {} seconds ".format(titles_profit, elapsed_time))


# ======================================================================================================================
# Which are the top 3 movies that expend more money to be produced in the list?

# start = time.time()

# all_movies_budget = [(movie_dataset[x][22]) for x in range(0, dataset_samples_number)]
# titles_budget = [(all_movies_titles[k], (all_movies_budget[k])) for k in range(1, dataset_samples_number-1)]
# titles_budget = list(filter(lambda k: k[0] != '' and k[1] != '' and str.isdigit(k[1]), titles_budget))
# titles_budget.sort(key=lambda x: float(x[1]), reverse=True)
# titles_budget = titles_budget[0:3]

# elapsed_time = (time.time() - start)

# print("Top 3 more expensive movies : '\n' {} \n\nElapsed time {} seconds ".format(titles_budget, elapsed_time))
# Top 3 more expensive movies : '
# ' [('The Host\xa0', '12215500000'), ('Lady Vengeance\xa0', '4200000000'), ('Fateless\xa0', '2500000000')]

# ======================================================================================================================
# Which are the top 3 movies that expend less money to be produced in the list?
# start = time.time()

# titles_budget = [(all_movies_titles[k], (all_movies_budget[k])) for k in range(1, dataset_samples_number-1)]
# titles_budget = list(filter(lambda k: k[0] != '' and k[1] != '' and str.isdigit(k[1]), titles_budget))
# titles_budget.sort(key=lambda x: float(x[1]), reverse=False)
# titles_budget = titles_budget[0:3]

# elapsed_time = (time.time() - start)
# print("Top 3 low cost movies : '\n' {} \n\nElapsed time {} seconds ".format(titles_budget, elapsed_time))

# ======================================================================================================================
# What year was the one who had more movies released ?
# start = time.time()

# all_release_year_list = [(movie_dataset[x][23]) for x in range(1, dataset_samples_number)]
# year_occurrences = get_histogram_of(all_release_year_list)
# year_occurrences = [(k, year_occurrences[k]) for k in sorted(year_occurrences, key=year_occurrences.get, reverse=True)]
# year_occurrences = year_occurrences[0]
# elapsed_time = (time.time() - start)

# print("The year with more movies releases was : '\n' {} \n\nElapsed time {} seconds ".format(year_occurrences, elapsed_time))
# ('2009', 255)

# What year was the one who had less movies released ?
# start = time.time()
# all_release_year_list = [(movie_dataset[x][23]) for x in range(1, dataset_samples_number)]
# year_occurrences = get_histogram_of(all_release_year_list)
# year_occurrences = [(k, year_occurrences[k]) for k in sorted(year_occurrences, key=year_occurrences.get, reverse=False)]
# year_occurrences = list(filter(lambda k: k[0] != '' and k[1] != '' and len(k[0])==4, year_occurrences))
# year_occurrences = year_occurrences[0]
# elapsed_time = (time.time() - start)


# print("The year with less movies releases was {} with {} movie(s)".format(year_occurrences[0],year_occurrences[1]))

## ======================================================================================================================
# Create a actor ranking ordered by number of performances by:
# - Number of movies where the actor performed
# - Social Media Influence
# - Best Movie

# start = time.time()

# actor_1_name = [(movie_dataset[x][10]) for x in range(1, dataset_samples_number - 1)]
# actor_1_likes = [(movie_dataset[x][7]) for x in range(1, dataset_samples_number - 1)]
# actor_1_likes = filter_likes_crazy_values(actor_1_likes)

# actor_2_name = [(movie_dataset[x][6]) for x in range(1, dataset_samples_number - 1)]
# actor_2_likes = [(movie_dataset[x][24]) for x in range(1, dataset_samples_number - 1)]
# actor_2_likes = filter_likes_crazy_values(actor_2_likes)

# actor_3_name = [(movie_dataset[x][15]) for x in range(1, dataset_samples_number - 1)]
# actor_3_likes = [(movie_dataset[x][5]) for x in range(1, dataset_samples_number - 1)]
# actor_3_likes = filter_likes_crazy_values(actor_3_likes)

# imb_qualification = [(movie_dataset[x][25]) for x in range(1, dataset_samples_number - 1)]
# imb_qualification = filter_imb_crazy_values(imb_qualification[:])

# Create a tuple with user Attributes in the form of [name, movies, likes_number, imb ] i.e. ('Lillian Gish', 1, 0, 8.0)
# actor_1_attributes = list(
#    (actor_1_name[k], 1, int(actor_1_likes[k]) if actor_1_likes[k] else 0,
#     float(imb_qualification[k])) for k in range(1, dataset_samples_number - 2))

# actor_2_attributes = list(
#    (actor_2_name[k], 1, int(actor_2_likes[k]) if actor_2_likes[k] else 0,
#     imb_qualification[k]) for k in range(1, dataset_samples_number - 2))

# actor_3_attributes = list(
#    (actor_3_name[k], 1, int(actor_3_likes[k]) if actor_3_likes[k] else 0,
#     imb_qualification[k]) for k in range(1, dataset_samples_number - 2))

# Create a dictionary based on Actors Attributes
# actors_ranking = {}
# create_ranking_authors_from_list(actors_ranking, actor_1_attributes)
# create_ranking_authors_from_list(actors_ranking, actor_2_attributes)
# create_ranking_authors_from_list(actors_ranking, actor_3_attributes)

# Sorted by Number of movies, Social Influence and iMB movie qualification
# filter_dictionary_keys_as_numbers(actors_ranking)
# actors_ranking = [sorted(actors_ranking.values(), key=lambda x: (x[1], x[2], x[3]), reverse=True)]

# elapsed_time = (time.time() - start)

# print("Actor ranking : ")
# for actor in actors_ranking[0][:4]: print(actor) # Change this parameter in case of watching all the results
# print("Elapsed time : ", elapsed_time)

# Actor ranking :
# ('Robert De Niro', 54, 1188000, 7.118836910088769)
# ('Morgan Freeman', 45, 495000, 7.8965078860196005)
# ('Johnny Depp', 41, 1640000, 6.568560059206175)
# ('Bruce Willis', 39, 507000, 6.231539757813152)
# Elapsed time : 0.08010411262512207


## ======================================================================================================================

# Create a “tag cloud” using tags or keywords of the movie: To do this you can create an ordered ranking
# of the number of word occurrences.

# start = time.time()

# Filter titles
# all_movies_titles = str(''.join(all_movies_titles)).strip('[]').replace('\\xa0', ' ').replace(" \\' "," ").replace("  ", " ")

# str_list = all_movies_titles.split()

# Gives set of unique words
# unique_words = set(str_list)
# words_ocurrences = {}

# for words in unique_words:
#     words_ocurrences[words] = str_list.count(words)
# words_ocurrences = {k: v for k, v in sorted(words_ocurrences.items(), key=lambda item: item[1], reverse= True)}


# elapsed_time = (time.time() - start)

# print("Ordered raking based on Keywords Titles recurrences")
# for i in words_ocurrences :
#     print(i, words_ocurrences[i])

# print("Elapsed time : ", elapsed_time)
# The 1123
# of 481
# the 455
# and 138
# A 101
# in 100
# to 99
# Elapsed time :  1.029115915298462


## ======================================================================================================================
# What movie genre raised more money per year?
# What movie genre raised less money per year?

start = time.time()

all_movies_genres = [(movie_dataset[x][9]) for x in range(0, dataset_samples_number)]
all_movies_profit = all_movies_profit
all_movies_year = [(movie_dataset[x][23]) for x in range(0, dataset_samples_number)]

genre_profit_year = [(all_movies_genres[x], all_movies_profit[x], all_movies_year[x]) for x in
                     range(1, len(all_movies_genres))]
# Clearing Empty fields
filtered = []
for item in genre_profit_year:
    if item[0] != '' and item[1] != '' and item[2] != '' and len(item[2]) == 4:
        filtered.append([item[0], item[1], item[2]])


# Split Genres - Money Raised - Year in the form of ('Fantasy', '200074175', '2015')
total_data = []

for i, v in enumerate(filtered):
    s = str(filtered[i][0]).split("|")
    if len(s) == 1:
        total_data.append((s[0], filtered[i][1], filtered[i][2]))
    else:
        for i in range(filtered[i][0].count("|")):
            total_data.append((s[i], filtered[i][1], filtered[i][2]))

years = {}
for i,genre_profit in enumerate(total_data):
    if genre_profit[2] in years:
        if genre_profit[1] in years:
            years[genre_profit[2]][genre_profit[0]] = years[genre_profit[2]][genre_profit[0]] + genre_profit[1]
        else:
            years[genre_profit[2]][genre_profit[0]] = genre_profit[1]
    else:
        years[genre_profit[2]] = {genre_profit[0]:genre_profit[1]}

elapsed_time = (time.time() - start)

for year in years.keys():
    print("==")
    print("Raised more money in ", year, sorted(years[year], reverse=False)[0])
    print("Raised less money in ", year, sorted(years[year], reverse=False)[-1])
    print("==")

print("Elapse time in seconds : ", elapsed_time)
# ==
# Raised more money in  2009 Action
# Raised less money in  2009 Sci-Fi
# ==
# ==
# Raised more money in  2007 Adventure
# Raised less money in  2007 Western
# ==

