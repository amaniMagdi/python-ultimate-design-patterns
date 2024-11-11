from command import Command

class LockDoorCommand(Command):
    def __init__(self, door):
        self._door = door

    def execute(self):
        self._door.lock()
