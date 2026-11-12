class Thermostat():
    def __init__(self, temperature : float) :
        self._temperature = temperature  # Protected Storage

    # This acts like a variable : thermostat.temperature (getter)
    @property
    def temperature(self):
        return self._temperature

    # This runs automatically when you assign : thermostat.temperature = 24 (setter)

    @temperature.setter
    def temperature(self,value):
        if value < -273.15:
            raise ValueError(" Temp can't be below absolute zero")
        self._temperature = value


t = Thermostat(20)
print(t.temperature) # Accessed like a normal attribute (calls getter)
t.temperature = 22 # Assigned like a normal atribute (calls setter)
print(t.temperature)
