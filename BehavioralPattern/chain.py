class Handler:
    """abstract handeler"""

    def __init__(self, successor):
        self._successor = successor

    def handler(self, request):
        handled = self._handle(request)

        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError("Must provided implementation is subclass")


class ConcreateHandler1(Handler):
    """Concrete handler 1"""

    def _handle(self, request):
        if 0 < request <= 10:
            print("Request {} handled in handler 1".format(request))
        return True


class DefaultHandler(Handler):
    """Default handler"""

    def _handle(self, request):
        """If there is no handler available"""
        print("End of chain, no handler of {} ".format(request))
        return True


class Client:
    def __init__(self):
        self.handler = ConcreateHandler1(None)

    def delegate(self, requests):
        for request in requests:
            self.handler.handler(request)


c = Client()

requests = [2, 4, 16]

c.delegate(requests)
