from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Action(object):

    def __init__(self, action):
        self._action = action

    @property
    def strategy(self)
        return self._action

    @strategy.setter
    def strategy(self, action):
        self._action = action

    def algorithm(self):
        print("We're going to print out a series of characters!")
        result = self._action.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))

class Strategy(ABC):

    @abstractmethod
    def do_algorithm(self, data):
        pass

class ConcreteStrategyOne(Strategy):
    def do_algorithm(self, data):
        return sorted(data)

class ConcreteStrategyTwo(Strategy):
    def do_algorithm(self, data):
        return reversed(sorted(data))

if __name__ == "__main__":
    action = Action(ConcreteStrategyOne())
    print("We will print the numbers in regular order.")
    action.algorithm()

    action = Action(ConcreteStrategyTwo())
    print("We will print the numbers in reverse order.")
    action.algorithm()