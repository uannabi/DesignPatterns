import copy


class Prototype:

    def __init__(self):
        self._objects = {}

    def register_objects(self, name, obj):
        """register an object"""
        self._objects[name] = obj

    def unregister_objects(self, name):
        """unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:
    def __init__(self):
        self.name = "Tesla"
        self.color = "Silver"
        self.options = "SpaceX"

    def __str__(self):
        return '{} | {} | {} '.format(self.name, self.color, self.options)


c = Car()

prototype = Prototype()
prototype.register_objects('Tesla', c)

c1 = prototype.clone('Tesla')

print(c1)
