import machine
import dht


class DHTSensor:
    def __init__(self):
        pass

    def init(self):
        self.d = dht.DHT11(machine.Pin(4))
        flag = 0
        while flag == 0:
            try:
                self.d.measure()
                flag = 1
            except OSError:
                flag = 0
                print("Something wrong with d.measure()")

    def get_temperature(self):
        self.init()
        return self.d.temperature()

    def get_humidity(self):
        self.init()
        return self.d.humidity()