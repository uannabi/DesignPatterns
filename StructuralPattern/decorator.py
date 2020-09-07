from functools import wraps


def MakeCoffee(function):
    """Defines the decorator"""

    # this makes the decorator transparent in terms of name and docstring
    @wraps(function)
    # define the inner function
    def decorator():
        # Grab the return value of the function being decorated
        ret = function()

        # add new functionality to the function being decorated
        return ret + " with extra Shot of Espresso"

    return decorator


# apply the decorator here
@MakeCoffee
def Espresso():
    """Original function ! """
    return "Cup of Coffee"


# check the result of decorating

print(Espresso())

# check if the function name is still the same name fo the function being decorated

print(Espresso.__name__)

# Check if the docstring is still the same as that of the function being decorated

print(Espresso.__doc__)
