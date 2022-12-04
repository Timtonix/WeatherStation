import machine
import dht

def setup_dht_sensor(pin):
    d = dht.DHT11(machine.Pin(pin))
    while flag == 0:
        try:
            d.measure()
            print("It's work !")
            flag = 1
        except OSError:
            flag = 0
            print("Something wrong with d.measure()")

def get_temperature():
    return d.temperature()

def get_humidity():
    return d.humidity()


