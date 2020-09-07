import time

class Producer:
    """Define the 'resource-intensive' Object to instantiate"""
    def producer(self):
        print("Producer is working hard")

    def meet(self):
        print("Producer has time to meet you now")

class Proxy:
    """Define the 'relatively less resource intensive' proxy to instantiate as middleman"""
    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """Check if the Team Lead is available"""
        print("Artist checking if Team Lead is available ...")

        if self.occupied == 'No':
            # if the Producer is available  , crate a team lead object
            self.producer = Producer()
            time.sleep(2)

            # make the producer the gust
            self.producer.meet()

        else:
            # Otherwise, don't instantiate a Producer
            time.sleep(2)
            print("Producer is busy")


# instantiate a proxy

p = Proxy()

# make the proxy Artist Producer untill Producer is available
p.produce()

# change the state to 'occupied'
p.occupied = 'Yes'

# make the Producer Produce

p.produce()
