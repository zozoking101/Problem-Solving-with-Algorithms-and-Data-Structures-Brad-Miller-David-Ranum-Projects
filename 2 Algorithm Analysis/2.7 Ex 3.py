import timeit

# Function to measure the time it takes to delete an element from a list
def measure_del_list(lst, index):
    del lst[index]

# Function to measure the time it takes to delete an element from a dictionary
def measure_del_dict(dictionary, key):
    del dictionary[key]

# Experiment
for i in range(1000, 100001, 5000):
    # Create a list with consecutive integers
    my_list = list(range(i))

    # Create a dictionary with integer keys and values
    my_dict = {j: j for j in range(i)}

    # Measure time for deleting an element from the list
    del_list_time = timeit.timeit(lambda: measure_del_list(my_list, 0), number=1000)

    # Measure time for deleting an element from the dictionary
    del_dict_time = timeit.timeit(lambda: measure_del_dict(my_dict, 0), number=1000)

    print("%d,%10.6f,%10.6f" % (i, del_list_time, del_dict_time))
