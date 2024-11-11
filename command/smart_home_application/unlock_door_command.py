from command import Command

class UnlockDoorCommand(Command):
    def __init__(self, door):
        self._door = door

    def execute(self):
        self._door.unlock()
