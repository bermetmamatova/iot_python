from device import Device

class Thermostat(Device):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.temperature = 15

    def set_temperature(self, temperature):
        if self.status:
            self.temperature = temperature
