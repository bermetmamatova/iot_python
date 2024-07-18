import unittest
from automation import AutomationSystem
from smart_light import SmartLight
from thermostat import Thermostat
from security_camera import SecurityCamera

class TestAutomationSystem(unittest.TestCase):

    def setUp(self):
        self.automation_system = AutomationSystem()
        self.light = SmartLight(1)
        self.thermostat = Thermostat(2)
        self.camera = SecurityCamera(3)
        self.automation_system.add_device(self.light)
        self.automation_system.add_device(self.thermostat)
        self.automation_system.add_device(self.camera)

    def test_add_device(self):
        self.assertEqual(len(self.automation_system.devices), 3)

    def test_turn_on_device(self):
        self.light.turn_on()
        self.assertTrue(self.light.status)

    def test_set_brightness(self):
        self.light.turn_on()
        self.light.set_brightness(50)
        self.assertEqual(self.light.brightness, 50)

    def test_set_temperature(self):
        self.thermostat.turn_on()
        self.thermostat.set_temperature(25)
        self.assertEqual(self.thermostat.temperature, 25)

    def test_detect_motion(self):
        self.camera.turn_on()
        self.camera.detect_motion()
        self.assertIn(self.camera.motion_detected, [True, False])

if __name__ == '__main__':
    unittest.main()
