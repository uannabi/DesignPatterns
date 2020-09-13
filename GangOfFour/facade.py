class SubsystemA:
    def method1(self):
        print("SubsystemA Method1")

    def method2(self):
        print("SubsystemA Method2")


class SubsystemB:
    def method1(self):
        print("SubsystemB Method1")

    def method2(self):
        print("SubsystemB Method2")


class Facade:
    def __init__(self):
        self._subsystem_A = SubsystemA()
        self._subsystem_B = SubsystemB()

    def method(self):
        self._subsystem_A.method1()
        self._subsystem_A.method2()

        self._subsystem_B.method1()
        self._subsystem_B.method2()


def main():
    facade = Facade()
    facade.method()


if __name__ == "__main__":
    main()
