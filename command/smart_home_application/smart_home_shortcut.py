class SmartHomeShortcut:
    def __init__(self):
        self._commands = {}

    def set_command(self, shortcut_command, command):
        self._commands[shortcut_command] = command

    def open_shortcut(self, shortcut_command):
        command = self._commands.get(shortcut_command)
        if command:
            command.execute()
        else:
            print(f"No command found for shortcut: {shortcut_command}")
