class DrawingAPIOne(object):
    """Implementation-specific abstraction: concrete class one"""

    def draw_circle(self, x, y, radius):
        print("Api 1 drawing a circle at ({}, {} with radisu {}!)".format(x, y, radius))


class DrawingAPITwo(object):
    """Implementation-specific abstraction: concrete class two"""

    def draw_circle(self, x, y, radius):
        print("Api 1 drawing a circle at ({}, {} with radisu {}!)".format(x, y, radius))


class Circle(object):
    """Implementation-independent abstraction: for example , there could be rectangle class"""

    def __init__(self, x, y, radius, drawing_api):
        """Initialize the necessary attribute"""
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """Implementation-specific abstraction taken care of by another class DrawingAPI"""
        self._drawing_api.draw_circle(self._x, self._y, self._radius)
        # self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        """Implementation-Independent"""
        self._radius *= percent


# build the first cirlce object using API one
circel = Circle(1, 2, 3, DrawingAPIOne())

# draw a circle
circel.draw()

# build the second circle object using two
circel1 = Circle(2, 3, 4, DrawingAPITwo())

# draw a circle
circel1.draw()
