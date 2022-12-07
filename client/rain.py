from machine import *
import time
p13 = Pin(13, Pin.IN)


def get_rain() -> bool:
    for i in range(1, 100):
        if p13.value() == 1:
            return True
        time.sleep(0.01)
    return False
"""
    Example :
    time.sleep(5)
    print("Go")
    time.sleep(1)
    if get_rain():
         print("It's raining !")
"""