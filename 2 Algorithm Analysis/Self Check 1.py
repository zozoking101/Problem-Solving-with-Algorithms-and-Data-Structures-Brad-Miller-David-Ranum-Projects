# Min Alg O(n^2)
import time

def min(list_name):
    n = len(list_name)
    for i in range(n):
        smallest = list_name[i]
        for j in range(i + 1, n):
            if list_name[j] < smallest:
                smallest = list_name[j]
        return smallest

def min_2(list_name):
    smallest = list_name[0]
    for i in list_name:
        if i < smallest:
            smallest = i
    return smallest

l = [0.3, 0.2, 0.1, 0.9, 0.5, 0.6, 0.8, 0.3, 0.4, 0.5, 0.8]

start = time.time()
print(min_2(l))
end = time.time()

print(end - start)

        