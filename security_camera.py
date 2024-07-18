from device import Device
import random

class SecurityCamera(Device):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.motion_detected = False

    def detect_motion(self):
        if self.status:
            self.motion_detected = random.choice([True, False])
        else:
            self.motion_detected = False  # No motion detected if the camera is off
