from command import Command

class TurnLightOnCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_on()
