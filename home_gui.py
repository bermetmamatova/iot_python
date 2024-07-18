import tkinter as tk
from automation import AutomationSystem
from smart_light import SmartLight
from thermostat import Thermostat
from security_camera import SecurityCamera
import random

def create_gui(automation_system):
    root = tk.Tk()
    root.title("Smart Home IoT Simulator")

    controls_frame = tk.Frame(root)
    controls_frame.pack(side=tk.LEFT, padx=20, pady=20)

    automation_button = tk.Button(controls_frame, text="Automation OFF", command=lambda: toggle_automation(automation_system, automation_button))
    automation_button.pack()

    light = automation_system.devices[0]
    thermostat = automation_system.devices[1]
    camera = automation_system.devices[2]

    brightness_label = tk.Label(controls_frame, text="Brightness")
    brightness_label.pack()
    brightness_scale = tk.Scale(controls_frame, from_=0, to=100, orient='horizontal')
    brightness_scale.set(light.brightness)
    brightness_scale.pack()
    toggle_light_button = tk.Button(controls_frame, text="Toggle Light", command=lambda: toggle_device(light))
    toggle_light_button.pack()


    temperature_label = tk.Label(controls_frame, text="Temperature")
    temperature_label.pack()
    temperature_scale = tk.Scale(controls_frame, from_=10, to=30, orient='horizontal')
    temperature_scale.set(thermostat.temperature)
    temperature_scale.pack()
    toggle_thermostat_button = tk.Button(controls_frame, text="Toggle Thermostat", command=lambda: toggle_device(thermostat))
    toggle_thermostat_button.pack()


    toggle_camera_button = tk.Button(controls_frame, text="Toggle Camera", command=lambda: toggle_device(camera))
    toggle_camera_button.pack()
    random_motion_button = tk.Button(controls_frame, text="Random Detect Motion", command=lambda: random_detect_motion(camera))
    random_motion_button.pack()

    file_display_frame = tk.Frame(root)
    file_display_frame.pack(side=tk.BOTTOM, padx=40, pady=40)
    file_display_text = tk.Text(file_display_frame, width=70, height=30)
    file_display_text.pack()

    # Function Definitions
    def toggle_device(device):
        if device.status:
            device.turn_off()
            automation_system.log_sensor_data(device, 'Status', 'Off')
        else:
            device.turn_on()
            automation_system.log_sensor_data(device, 'Status', 'On')
        update_file_display()

    def set_brightness(device, brightness):
        device.set_brightness(brightness)
        automation_system.log_sensor_data(device, 'Brightness', brightness)
        update_file_display()

    def set_temperature(device, temperature):
        device.set_temperature(temperature)
        automation_system.log_sensor_data(device, 'Temperature', temperature)
        update_file_display()

    def random_detect_motion(device):
        device.detect_motion(random.choice([True, False]))
        automation_system.log_sensor_data(device, 'Motion Detected', 'Yes' if device.motion_detected else 'No')
        update_file_display()

    def toggle_automation(system, button):
        system.toggle_automation()
        button.config(text=f"Automation {'ON' if system.automation_enabled else 'OFF'}")
        update_file_display()

    def update_file_display():
        with open("sensor_data.txt", "r") as file:
            file_contents = file.read()
        file_display_text.delete(1.0, tk.END)
        file_display_text.insert(tk.END, file_contents)


    brightness_scale.config(command=lambda v: set_brightness(light, int(v)))
    temperature_scale.config(command=lambda v: set_temperature(thermostat, int(v)))


    update_file_display()


    root.mainloop()


if __name__ == "__main__":
    automation_system = AutomationSystem()
    automation_system.add_device(SmartLight(1))
    automation_system.add_device(Thermostat(2))
    automation_system.add_device(SecurityCamera(3))
    create_gui(automation_system)
