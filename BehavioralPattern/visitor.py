class House(object): #this class being visited
    def accept(self,visitor):
        """Interface a accept a visitor"""
        visitor.visit(self) #tirgger the visiting operational

    def work_on_hvac(self,hvac_specialist):
        print(self,"worked on by", hvac_specialist)#Note that we now hava a referance to the Hvac specialist object in the house object

    def work_on_electricity(self, eleactracian):
        print(self,"worked on by", eleactracian) #note that we now have a reference to the electician

    def __str__(self):
        """simply return the class name when the house object is printed"""
        return self.__class__.__name__



class Visitor(object):
    """Abstracdt visitor"""
    def __str__(self):
        """simply returnt eh class name when visitor object is printed"""
        return self.__class__.__name__


class HavcSpecialist(Visitor):#inherits from the parent class, visitor

    def visit(self,house):
        house.work_on_hvac(self)#note that the visitor now has a reference to the house object



class Electrcian(Visitor):
    """Concrete visitor: electrician"""
    def visit(self,house):
        house.work_on_electricity(self) #note that the visitor now has refereence to the house object


"""create a HVAC specilist"""
hv = HavcSpecialist()
"""create an electician"""
e = Electrcian()

"""Create a house"""
home = House()

"""Let the house accept the HVAC specilist and work on the house by invoking the visit() method"""
home.accept(hv)

"""Let the house accept the electrican and work on the houyse by invoking the visit() method"""
home.accept(e)