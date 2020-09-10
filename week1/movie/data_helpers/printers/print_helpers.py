def print_array(array):
    for index in array:
        for i, elements in enumerate(index):
            print(index[i], ":", end=" ")
        print(" ")
