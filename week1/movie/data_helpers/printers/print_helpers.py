def print_array(array):
    # Print in ordered manner the attributes contained inside a tuple.
    for index in array:
        for i, elements in enumerate(index):
            print(index[i], ":", end=" ")
        print(" ")
