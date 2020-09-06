class Ada:
    """ ada class making class attributes global"""
    _shared_state = {} #attrivute dictionary 

    def __init__(self):
        self.dict = self._shared_state #Make it an attribute dictonary 

class Axiata(Ada): #inherits from the borag class 
    """this class now share all its attributes among its various instances"""
    """this esseentially makes the singleton objects an object-oriented global variable """

    def __init__(self, **kwargs):
        Ada.__init__(self)
        #update the attribute dictonary by inseting a new key  value pair 
        self._shared_state.update(kwargs)

    def __str__(self):
            #Return the attribute dictonary for printing 
        return str(self._shared_state)

#lets' create a singleton objects and add our first acronym
x = Axiata(HTTP = 'Hyper Text Transfer Protocol')
print(x)

#lets create another singleton object and if it refers to the same attribute dictonary by adding another acronym

y = Axiata(SNMP = "simple network managment protocal")
print(y)