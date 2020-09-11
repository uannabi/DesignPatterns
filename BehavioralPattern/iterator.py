def count_to(count):
    """our iterator implementation """
    """our list"""
    coffee_in_mug = ["suger", "stream", "foam", "espresso", "hazelnuts", "redeye"]
    """Our build in iterator"""
    """Create a tuble such as (1,"spresso")"""
    Iterator = zip(range(count), coffee_in_mug)
    # iterate through our iterable lsit
    # extract the coffe element
    # put them in generator called number
    for things, item in Iterator:
        # return a generator containing coffee item
        yield item


for num in count_to(4):
    print("{}".format(num))

for num in count_to(5):
    print("{}".format(num))
