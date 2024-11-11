class Light:
    def __init__(self, name):
        self._name = name

    def turn_on(self):
        print("Turning on light...")

    def turn_off(self):
        print("Turning off light...")

    def get_name(self):
        return self._name
