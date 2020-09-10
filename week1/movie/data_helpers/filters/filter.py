def get_histogram_of(elements_list):
    # Function for creating the dictionary based on keys and the frequency in which the key get's repeated
    hist = {}
    for i in elements_list:
        hist[i] = hist.get(i, 0) + 1
    return hist


def filter_imb_crazy_values(lista):
    # Function for dismissing empty keys and very big, outliers, values.
    result = []
    for i, v in enumerate(lista):
        number = 0
        if v == '':
            number = 0
        else:
            number = float(v)
            if number > 10 or number < 0:
                number = 0
        result.append(number)
    return result


def filter_likes_crazy_values(lista):
    # Function for dismissing  empty keys and big values.
    result = []
    for i, like in enumerate(lista):
        if like == '' or not str.isdigit(like):
            number = 0
        else:
            number = int(like)
            if number < 0:
                number = 0
        result.append(number)
    return result


def create_ranking_authors_from_list(dict, elements_list):
    # Function for accomodating distinct authors names and increasing their values attributes in case the actor
    # has already been reated
    for element in elements_list:
        if element[0] in dict.keys():
            dict[element[0]] = (element[0], dict[element[0]][1] + 1,
                                dict[element[0]][2] + element[2],
                                (dict[element[0]][3] + element[3]) / 2)
        else:
            dict[element[0]] = (
                element[0], element[1], element[2], element[3])

    return dict


def filter_movie_title(titles):
    # Function for taking out weird breaklines characters, empty spaces and parenthesis
    for mov in titles:
        mov = mov.replace('[', " ").replace(']', "").replace('\\xa0', '').replace(" \\' ", "").replace("  ", " ").split()
    return titles


def filter_dictionary_keys_as_numbers(dictionary):
    # Function for filtering empty inputs
    wrong = []
    for key in dictionary.keys():
        if str.isdigit(key) or key == '':
            wrong.append(key)
    for i in wrong:
        del dictionary[i]


def find_sum_if_repeated(list):
    # Function for increasing the value in a dictionary as many times as thee element is found in a list.t
    unrepeated = {}
    for element in list:
        if element[0] in unrepeated:
            unrepeated[element[0]] += int(element[1]) if str.isdigit(element[1]) else 0
        else:
            unrepeated[element[0]] = int(element[1])
    return [(k, v) for k, v in unrepeated.items()]



