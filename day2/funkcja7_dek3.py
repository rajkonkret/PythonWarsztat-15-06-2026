# napisac dekorator mierzący czas wykonania funkcji
# time.time()
# time.perf_counter()
import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        execution_time = time.perf_counter() - start_time

        print(f"Czas wykonania funkcji: {func.__name__}: {execution_time}")

        return result

    return wrapper
