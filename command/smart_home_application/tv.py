class Tv:
    def __init__(self, name):
        self._name = name

    def turn_on(self):
        print("Turning on TV")

    def turn_off(self):
        print("Turning off TV")

    def get_name(self):
        return self._name
