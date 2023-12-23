# Import the timeit module
import timeit
# Import the Timer class defined in the module
from timeit import Timer

pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")

# x = list(range(2000000))
# print(pop_zero.timeit(number=1000))
# # 3.6902685000095516

# x = list(range(2000000))
# print(pop_end.timeit(number=1000))
# # 4.4100015657022595e-05

print("pop(0) pop()")
for i in range(1000000,100000001,1000000):
    x = list(range(i))
    pt = pop_end.timeit(number=1000)
    x = list(range(i))
    pz = pop_zero.timeit(number=1000)
    print("%15.5f, %15.5f" %(pz,pt))