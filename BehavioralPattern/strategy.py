import types


class Strategy:
    """The strategy pattern class"""

    def __init__(self, function=None):
        self.name = "Default Strategy"

        # if a reference to function is provided, replace the execute() method with the given function

        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):  # this gets replaced by another version if another strategy is provided
        """the default method that printes the name of the strategy being used"""
        print("{} is used!".format(self.name))


# replacement method
def strategy_one(self):
    print("{} is used to execute method 1 ".format(self.name))


# replacement method
def strategy_two(self):
    print("{} is used to execute method 2 ".format(self.name))


# Let's create our default strategy
s0 = Strategy()
# Let's execute our default strategy
s0.execute()

# Let's create the first varition of our default strategy by providing a new behavior
s1 = Strategy(strategy_one)
# Let's set its name
s1.name = "Strategy One"
# Let's execute the strategy
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()
