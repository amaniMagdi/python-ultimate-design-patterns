from beverage import Beverage

class CondimentDecorator(Beverage):
    def __init__(self, beverage):
        self._beverage = beverage

    def prepare(self):
        return self._beverage.prepare()