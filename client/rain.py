from machine import *
import time

p13 = Pin(13, Pin.IN)
while True :
    if p13.value() == 1:
        print("dry")