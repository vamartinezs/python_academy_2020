def get_histogram_of(elements_list):
    hist = {}
    for element in elements_list:
        hist[element] = int(hist.get(element, 0)) + 1
    return hist


def sort_dictionary(dictionary):
    for i in sorted(dictionary.keys()):
        print(i, end=" ")
