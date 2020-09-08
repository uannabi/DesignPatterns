class Component(object):
    """Abstract class"""

    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass


class Child(Component):  # Inherits from the abstract class, Component
    """Concrete class"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, *kwargs)

        # this is where we store the name of y0our child item!
        self.name=args[0]

    def component_function(self):
        # print the name of your child item here
        print("{}".format(self.name))


class Composite(Component):  # Inherits from the abstract class, Component
    def __init__(self, *args, **kwargs):
        Component.__init__(self,*args,**kwargs)
        # this is where we store the name of the composite object

        # this is where we keep our child items
        self.name = args[0]

        self.children = []

    def append_child(self, child):
        """Method to add a new child item"""
        self.children.append(child)

    def remove_child(self, child):
        """Method to remove a child item"""
        self.children.remove(child)

    def component_function(self):
        """Print the name of composite object"""
        print("{}".format(self.name))

        # iterrate through the chuld objects and invoke their component function printing their name

        for i in self.children:
            i.component_function()


# build composit sub menu
sub1 = Composite("submenu1")

# create a new child sub_submenu 11
sub11 = Child("sub_submenu 11")
# create a new child sub_submenu 12
sub12 = Child("sub_submenu 12")

# add the sub_submenu 11 to submenu 1
sub1.append_child(sub11)
# add teh sub_submenu 12 to submenu 1
sub1.append_child(sub12)

# build a top level composite menu

top = Composite("Top_menu")

# build a submenu 2 that is not a composite

sub2 = Child("Submenu2")

# add the composite submenu 1 to the top-level  composite menu
top.append_child(sub1)

# add the plain submenu 2 the top.level composite menu
top.append_child(sub2)

#lets test composit pattern
top.component_function()