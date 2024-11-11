from command import Command

class TurnTvOnCommand(Command):
    def __init__(self, tv):
        self._tv = tv

    def execute(self):
        self._tv.turn_on()
