class Owl:
    """one of the objects to be returned"""

    def speak(self):
        return "whooom!"

    def __str__(self):
        return "Owl"


class OwlFactory:
    """concrete factory"""

    def get_pet(self):
        """return a owl object"""
        return Owl()

    def get_food(self):
        """return a owl food object"""
        return "Owl Food!"


class PetStore:
    """petstore houses our Abstract factory"""

    def __init__(self, pet_factory=None):
        """pet_factory is our abstract factory"""

        self._pet_factory = pet_factory

    def show_pet(self):
        """utility method to display the details of the objects return by the PetFactory"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}!".format(pet))
        print("Our pet says hello by '{}!".format(pet.speak()))
        print("Its food is '{}!".format(pet_food))


# Create a Concrete Factory
factory = OwlFactory()

# Create a pet store housing our Abstract Factory
shop = PetStore(factory)

# Invoke the utility method to show the details of our pet
shop.show_pet()
