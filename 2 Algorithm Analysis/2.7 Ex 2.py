import timeit

# Function to measure the time it takes to get an item from a dictionary
def measure_get_item(dictionary):
    return dictionary.get(0)

# Function to measure the time it takes to set an item in a dictionary
def measure_set_item(dictionary):
    dictionary[0] = 1

# Experiment
for i in range(10000, 1000001, 20000):
    dictionary = {j: j for j in range(i)}

    # Measure time for getting an item
    get_time = timeit.timeit(lambda: measure_get_item(dictionary), number=1000)

    # Measure time for setting an item
    set_time = timeit.timeit(lambda: measure_set_item(dictionary), number=1000)

    print("%d,%10.6f,%10.6f" % (i, get_time, set_time))
