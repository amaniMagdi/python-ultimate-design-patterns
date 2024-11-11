from command import Command

class TurnTvOffCommand(Command):
    def __init__(self, tv):
        self._tv = tv

    def execute(self):
        self._tv.turn_off()
