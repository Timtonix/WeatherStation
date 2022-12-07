from machine import *
import time
p13 = Pin(13, Pin.IN)


def get_dry() -> bool:
    for i in range(1, 100):
        print(i)
        print(p13.value())
        if p13.value() == 1:
            return True
        time.sleep(0.01)

"""
    Example :
    time.sleep(5)
    print("Go")
    time.sleep(1)
    if get_dry():
         print("It's raining !")
"""