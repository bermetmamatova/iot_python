from device import Device

class SmartLight(Device):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.brightness = 0

    def set_brightness(self, brightness):
        if self.status:
            self.brightness = brightness
