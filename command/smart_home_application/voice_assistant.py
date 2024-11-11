class VoiceAssistant:
    def __init__(self):
        self._commands = {}

    def set_command(self, talking_command, command):
        self._commands[talking_command] = command

    def say(self, talking_command):
        command = self._commands.get(talking_command)
        if command:
            command.execute()
        else:
            print(f"No command found for: {talking_command}")
