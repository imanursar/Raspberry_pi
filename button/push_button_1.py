#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_UP)

while(True):
    input_value = GPIO.input(16)
    if (input_value == False):
        print("tombol ditekan")
        time.sleep(1)
    elif(input_value == True):
        print("tombol tidak ditekan")
        time.sleep(1)

#pin 16 > resistor > button > pin 9

GPIO.cleanup()
