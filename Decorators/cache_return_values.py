# Implementation of a Decorator that caches the return values of a Function,
# so that when it is called with the same arguments, the cached value is returned
# instead of re-executing the function

from time import sleep as s


def cache(fun):
    cache_value = {}
    print(cache_value)

    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = fun(*args)
        cache_value[args] = result
        return result
    return wrapper


@cache
def long_running_function(a, b):
    s(3)
    return a + b


print(long_running_function(2, 3))
print(long_running_function(4.36, 96.01))
print(long_running_function(1000, 5.147))
print(long_running_function(2, 3))
