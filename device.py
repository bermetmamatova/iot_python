class Device:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = False  # Default to off for all devices

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False
