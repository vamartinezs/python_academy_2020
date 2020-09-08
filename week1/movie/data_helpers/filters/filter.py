def get_histogram_of(elements_list):
    hist = {}
    for i in elements_list:
        hist[i] = hist.get(i, 0) + 1
    return hist


def filter_imb_crazy_values(lista):
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
    result = []
    for i, like in enumerate(lista):
        if like == '' or  not str.isdigit(like):
            number = 0
        else:
            number = int(like)
            if  number < 0:
                number = 0
        result.append(number)
    return result


def create_ranking_authors_from_list(dict, elements_list):
    for element in elements_list:
        if element[0] in dict.keys():
            dict[element[0]] = (element[0], dict[element[0]][1] + 1,
                                dict[element[0]][2] + element[2],
                                (dict[element[0]][3] + element[3]) / 2)
        else:
            dict[element[0]] = (
                element[0], element[1], element[2], element[3])

    return dict


def filter_dictionary_keys_as_numbers(dictionary):
    wrong = []
    for key in dictionary.keys():
        if str.isdigit(key) or key == '':
            wrong.append(key)
    for i in wrong:
        del dictionary[i]

