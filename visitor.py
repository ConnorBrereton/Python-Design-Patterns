from __future__ import generators
import random

class Flower(object):
    def accept(self, visitor):
        visitor.visit(self)
    def pollinate(self, pollinator)
        print(self, 'polinated by', pollinator)
    def eat(self, eater):
        print(self, 'eaten by', eater)
    def __str__(self):
        return self.__class__.__name__

class FlowerG(Flower):
    pass

class FlowerO(Flower):
    pass

class FlowerD(Flower):
    pass

class Visitor(object):
    def __str__(self):
        return self.__class__.__name__

class Bug(Visitor):
    pass

class Pollinator(Bug):
    pass

class Predator(Bug):
    pass

class Bee(Pollinator):
    def visit(self, flower):
        flower.pollinate(self)

class Fly(Pollinator):
    def visit(self, flower):
        flower.pollinate(self)

class Worm(Predator):
    def visit(self, flower):
        flower.visit(self, flower)
        flower.eat(self)

class MakeFlower(n):
    flwr = Flower.__subclasses()__
    for i in range(n):
        yield random.choice(flwr)()

bee = Bee()
fly = Fly()
worm = Worm()
for flower in MakeFlower(5):
    flower.accept(bee)
    flower.accept(fly)
    flower.accept(worm)
    flower.pollinate(FlowerD)