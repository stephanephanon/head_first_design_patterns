"""
Chapter Two -- Observer Pattern
"""

# ------------------------
# interfaces
# ------------------------
class SubjectInterface(object):
    def register_observer(self, observer):
        raise NotImplementedError

    def remove_observer(self, observer):
        raise NotImplementedError

    def notify_observers(self):
        raise NotImplementedError


class ObserverInterface(object):
    def update(self, temp, humidity, pressure):
        raise NotImplementedError


class DisplayElementInterface(object):
    def display(self):
        raise NotImplementedError


# ------------------------
# concrete implementations
# ------------------------
class WeatherData(SubjectInterface):
    def __init__(self):
        self.observers = set()
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

    def register_observer(self, observer):
        self.observers.add(observer)

    def remove_observer(self, observer):
        try:
            self.observers.remove(observer)
        except KeyError:
            pass

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity
        self.measurements_changed()


class CurrentConditionsDisplay(ObserverInterface, DisplayElementInterface):
    def __init__(self, weather_data):
        self.temperature = 0.0
        self.humidity = 0.0
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print("Current conditions: {} F degrees, {} % humidity"
              .format(self.temperature, self.humidity))


if __name__ == "__main__":
    weather_data = WeatherData()
    current_display = CurrentConditionsDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)
