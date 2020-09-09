class Subject(object):  # Represent what is being 'observed'

    def __init__(self):
        self._observers = []  # this is where refereances to all the observers are being kept
        # Node that this is a one-to-many relationship: there will be one subject to be observed by multiple _observers

    def attach(self, observer):
        if observer not in self._observers:  # if the observer is not already in the observers list
            self._observers.append(observer)  # append the observer to the list

    def detach(self, observer):  # simply remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:  # for all the observers in the list
            if modifier != observer:  # Don't notifiy the observer who is acctually updating the temperature
                observer.update(self)  # alart the observer!


class Core(Subject):

    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name  # set the name fo the core
        self._temp = 0  # initialize the temperature of the core

    @property  # greater thet gets the core temperature
    def temp(self):
        return self._temp

    @temp.setter  # setter that sets the core temperature
    def temp(self, temp):
        self._temp = temp
        self.notify()  # notify the boservers whenever somebody change the core temperature


class TempViewr:

    def update(self, subject):  # alert method that is invoked when the notify() method in a create subject is invoked
        print("Temperature Viewr: {} has Temperature {}".format(subject._name, subject._temp))


# let's create our subjects
c1 = Core("Core 1")
c2 = Core("Core 2")

# let's create our observers

v1 = TempViewr()
v2 = TempViewr()

# let's attach our observers to the first core
c1.attach(v1)
c2.attach(v2)

#let's change the temperature of our first core
c1.temp = 80
c1.temp = 90
