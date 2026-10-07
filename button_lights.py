from machine import Pin
import time

red = Pin(15, Pin.OUT)
green = Pin(10, Pin.OUT)
yellow = Pin(13, Pin.OUT)

button_green = Pin(18, Pin.IN, Pin.PULL_UP)
button_red = Pin(16, Pin.IN, Pin.PULL_UP)
button_yellow = Pin(21, Pin.IN, Pin.PULL_UP)

while True:
    if button_red.value() == 0:
        red.value(1)
        yellow.value(0)
        green.value(0)
    elif button_green.value() == 0:
        red.value(0)
        yellow.value(0)
        green.value(1)
    elif button_yellow.value() == 0:
        red.value(0)
        yellow.value(1)
        green.value(0)
    else:
        red.value(0)
        yellow.value(0)
        green.value(0)
    time.sleep(0.05)
