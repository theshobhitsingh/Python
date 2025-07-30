# A Decorator that measures the time a Fuction takes to execute
import time


def time_calculator(func):
    start_time = time.time()

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} ran in {end_time - start_time} time")
        return result
    return wrapper


@time_calculator
def example_function(n):
    time.sleep(n)


example_function(3)
