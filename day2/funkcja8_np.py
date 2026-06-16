import numpy as np
import tracemalloc

tracemalloc.start()

lista1 = list(range(10_000_000))
lista2 = list(range(10_000_000))
#
# array1 = np.arange(10_000_000, dtype=np.int64)
# array2 = np.arange(10_000_000, dtype=np.int64)

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Current memory usage: {current / 1024 ** 2} MB")
print(f"Peak memory usage: {peak / 1024 ** 2} MB")
