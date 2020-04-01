#!/usr/bin/env python

class OddNumbers(object):
    "An interable object represtation."

    def __init__(self, maximum):
        self.maximum = maximum

    def __iter__(self):
        # This link is how you call the
        # maxiumum method below!
        return IteratorMethod(self)
        
class IteratorMethod(object):
    "Example of an iterator."

    # Instantiate the container.
    # Instantiate the n-value.
    def __init__(self, container):
        self.container = container
        self.n = -1

    # This is the iterator itself.
    def __next__(self):
        self.n += 2
        if self.n > self.container.maximum:
            raise StopIteration
        return self.n

    # Returns the `n` value
    # on each iteration.
    def __iter__(self):
        return self.__next__

if __name__ == '__main__':
    numbers = OddNumbers(42)

    for nn in numbers:
        print(nn)