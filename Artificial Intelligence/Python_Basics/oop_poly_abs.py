'''class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

class Robot:
    def make_sound(self):
        return "Beep boop!"

# A single function that doesn't care WHAT the object is, 
# as long as it has a 'make_sound' method.
def animal_concert(creature):
    print(creature.make_sound())

animal_concert(Dog())    # Output: Woof!
animal_concert(Cat())    # Output: Meow!
animal_concert(Robot())  # Output: Beep boop!'''

from abc import ABC , abstractmethod

#abstract base class

class SmartDevice(ABC):

    @abstractmethod
    def turn_on(self):
        """Every smart device must implement its own way of turning on"""
    pass

class SmartLight(SmartDevice):
    def turn_on(self):
        print("Light bulb glows softly")

#light = SmartDevice()
device = SmartLight()
device.turn_on()
