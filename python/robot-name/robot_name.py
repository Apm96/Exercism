import string
import random
class Robot:
    def __init__(self):
         self.generate_nameRobot()
    def reset(self):
        self.generate_nameRobot()
    def generate_nameRobot(self):
        random.seed()
        self.name = ''.join(random.choices(string.ascii_uppercase, k=2) + random.choices(string.digits, k=3))
