from condiment_decorator import CondimentDecorator

class MilkDecorator(CondimentDecorator):

    def prepare(self) -> str:
        return super().prepare() + " with Milk"
