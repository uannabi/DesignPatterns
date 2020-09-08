class Korean:
    """korean speaker"""

    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"


class British:
    """English speaker"""

    def __init__(self):
        self.name = "British"

    def speak_english(self):
        return "Hello"


class Adapter:
    """this change the generric method name to individualized another name"""

    def __init__(self, object, **adapted_method):
        """change the name fo the method"""
        self._object = object

        # add a new dictonary item that establishe the mapping between the generic method name:Speadk() and the
        # concreeate method for example, speak() will be the tranlated to speak_korean() if the mapping say so

        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """Simply return the rest of attributes"""
        return getattr(self._object, attr)


# list to store speaker objects
objects = []

# create a korean object
korean = Korean()

# Create a British object

british = British()

# append the object to the objects list

objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
    print("{} says '{}'\n".format(obj.name, obj.speak()))
