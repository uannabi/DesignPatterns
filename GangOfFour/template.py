import sys
from abc import ABC, abstractmethod


class AbstractClass(ABC):

    def template_method(self):
        """Ths is the template method that contains a collection of
        		methods to stay the same, to be overriden, and to be overriden optionally.
        		"""
        self.__always_do_this()
        self.do_step_1()
        self.do_step_2()
        self.do_this_or()

    def __always_do_this(self):
        name = sys._getframe().f_code.co_name
        print("{}.{}".format(self.__class__.__name__, name))

    @abstractmethod
    def do_step_1(self):
        pass

    @abstractmethod
    def do_step_2(self):
        pass

    def do_this_or(self):
        print("You can overide me but you do not have to ")


class ConcreteClassA(AbstractClass):

    def do_step_1(self):
        print("Doing step 1 for ConcreateClassA")

    def do_step_2(self):
        print("Doing step 2 for ConcreateClassA")


class ConcreteClassB(AbstractClass):
    def do_step_1(self):
        print("Doing step 1 for ConcreateClassB")

    def do_step_2(self):
        print("Doing step 2 for ConcreateClassb")

    def do_this_or(self):
        print("Doing my own business..")


def main():
    print("-_ConcreteClassA_-")
    a = ConcreteClassA()
    a.template_method()

    print("-_ConcreteClassB_-")
    b = ConcreteClassB()
    b.template_method()


if __name__ == '__main__':
    main()
