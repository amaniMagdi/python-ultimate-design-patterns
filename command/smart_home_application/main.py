from light import Light
from tv import Tv
from door import Door
from lock_door_command import LockDoorCommand
from turn_light_on_command import TurnLightOnCommand
from turn_tv_on_command import TurnTvOnCommand
from voice_assistant import VoiceAssistant
from smart_home_mobile_application import SmartHomeMobileApplication
from smart_home_shortcut import SmartHomeShortcut   

# Create instances of the devices
light = Light("Living Room Light")
tv = Tv("Living Room TV")
door = Door("Front Door")

# Create command instances
turn_light_on = TurnLightOnCommand(light)
turn_tv_on = TurnTvOnCommand(tv)
lock_door = LockDoorCommand(door)

# Create instances of other objects for testing
smart_home_app = SmartHomeMobileApplication()
shortcut = SmartHomeShortcut()
voice_assistant = VoiceAssistant()

# Set up commands in the smart home app
smart_home_app.execute(turn_light_on)
smart_home_app.execute(turn_tv_on)

# Set commands for shortcuts
shortcut.set_command("light_on", turn_light_on)
shortcut.set_command("tv_on", turn_tv_on)
shortcut.open_shortcut("light_on")
shortcut.open_shortcut("tv_on")

# Set commands for voice assistant
voice_assistant.set_command("turn on the light", turn_light_on)
voice_assistant.set_command("turn on the tv", turn_tv_on)
voice_assistant.say("turn on the light")
voice_assistant.say("turn on the tv")

# Set up a shortcut to lock the door
shortcut.set_command("lock_door", lock_door)
shortcut.open_shortcut("lock_door")

