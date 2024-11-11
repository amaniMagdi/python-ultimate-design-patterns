class Door:
    def __init__(self, name):
        self._name = name

    def lock(self):
        print("Locking door...")

    def unlock(self):
        print("Unlocking door...")

    def get_name(self):
        return self._name
