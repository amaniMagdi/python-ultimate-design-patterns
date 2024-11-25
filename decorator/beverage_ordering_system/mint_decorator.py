from condiment_decorator import CondimentDecorator

class MintDecorator(CondimentDecorator):

    def prepare(self) -> str:
        return super().prepare() + " with Mint"
