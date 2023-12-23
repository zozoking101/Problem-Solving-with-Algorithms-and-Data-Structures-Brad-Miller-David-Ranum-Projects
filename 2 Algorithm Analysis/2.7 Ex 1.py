import timeit

# Function to measure the time it takes to access list indices
def measure_index_time(index, lst):
    return lst[index]

# Experiment
for i in range(10000, 1000001, 20000):
    lst = list(range(i))
    
    # Measure time for accessing the first element
    access_time = timeit.timeit(lambda: measure_index_time(0, lst), number=1000)

    print("%d,%10.6f" % (i, access_time))
