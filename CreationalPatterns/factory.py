class Espresso:
    def __init__(self, name):
        self._name = name

    def flavour(self):
        return "Bitter!"


class Latte:
    def __init__(self, name):
        self._name = name

    def flavour(self):
        return "Sweeet!"


def get_coffee(coffie="espresso"):
    coffies = dict(espresso=Espresso("Black"), latte=Latte("Milky"))
    return coffies[coffie]


mug = get_coffee("espresso")
print(mug.flavour())

mugs = get_coffee("latte")
print(mugs.flavour())
