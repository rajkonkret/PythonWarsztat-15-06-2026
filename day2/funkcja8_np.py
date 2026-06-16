import numpy as np
import tracemalloc

# tracemalloc.start()
#
# lista1 = list(range(10_000_000))
# lista2 = list(range(10_000_000))
# #
#
#
# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
#
# print(f"Current memory usage: {current / 1024 ** 2} MB")
# print(f"Peak memory usage: {peak / 1024 ** 2} MB")
# # Current memory usage: 762.9212341308594 MB
# # Peak memory usage: 762.9212341308594 MB

tracemalloc.start()

# array1 = np.arange(10_000_000, dtype=np.int64)
array1 = np.arange(10_000_000, dtype=np.int8)
# array2 = np.arange(10_000_000, dtype=np.int64)
array2 = np.arange(10_000_000, dtype=np.int8)

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Current memory usage: {current / 1024 ** 2} MB")
print(f"Peak memory usage: {peak / 1024 ** 2} MB")
# dla int64
# Current memory usage: 152.5884552001953 MB
# Peak memory usage: 152.5884552001953 MB

# dla int8
# Current memory usage: 19.074050903320312 MB
# Peak memory usage: 19.074050903320312 MB
