import machine
import dht


class DHTSensor:
    def __init__(self, pin):
        self.d = dht.DHT11(machine.Pin(pin))
        flag = 0
        while flag == 0:
            try:
                self.d.measure()
                print("It's work !")
                flag = 1
            except OSError:
                flag = 0
                print("Something wrong with d.measure()")

    def get_temperature(self):
        return self.d.temperature()

    def get_humidity(self):
        return self.d.humidity()

