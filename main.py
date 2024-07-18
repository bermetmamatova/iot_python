from home_gui import create_gui
from automation import AutomationSystem
from smart_light import SmartLight
from thermostat import Thermostat
from security_camera import SecurityCamera

with open("sensor_data.txt", "w") as file:
    file.truncate(0)


automation_system = AutomationSystem()


automation_system.add_device(SmartLight(1))
automation_system.add_device(Thermostat(2))
automation_system.add_device(SecurityCamera(3))


create_gui(automation_system)
