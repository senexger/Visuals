#!/usr/bin/env python
import time
import RPi.GPIO as GPIO

# RPi.GPIO Layout verwenden (wie Pin-Nummern)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)

clock = 0
set_pins_for_count(pins, var):
    for i,pin in enumerate(pins):
        set_pin(pin, clock & 2**i)

def set_pin(pin, val):
    if val == 1:
        GPIO.output(pin, GPIO.HIGH)
    elif val == 0:
        GPIO.output(pin, GPIO.LOW)
    else:
        raise Exception('invalid value')

# Dauersschleife
while 1:
    if clock == 4:
        clock = 0
    set_pin(3, clock & 1)
    set_pin(8, clock & 2)
    time.sleep(1)

