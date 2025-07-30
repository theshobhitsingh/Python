# A Decorator to print the Function Name and the Values of its arguments every time the Function is called

def debug(fun):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(
            f"{key} : {value}"for key, value in kwargs.items())
        print(
            f"Calling: {fun.__name__} calling with Arguments {args_value} and Kwargs {kwargs_value}")
        return fun(*args, **kwargs)

    return wrapper


@debug
def hello():
    print("Hello, World!")


@debug
def greet(name, greetings="Hello, "):
    print(f"{greetings} {name}")


greet(name="Shobhit Singh", greetings="Namaste")
