def get_histogram_of(elements_list):
    hist = {}
    for i in elements_list:
        hist[i] = hist.get(i, 0) + 1
    return hist
