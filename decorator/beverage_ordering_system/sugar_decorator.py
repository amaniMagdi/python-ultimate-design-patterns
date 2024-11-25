from condiment_decorator import CondimentDecorator

class SugarDecorator(CondimentDecorator):

    def prepare(self) -> str:
        return super().prepare() + " with Sugar"
