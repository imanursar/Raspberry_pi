#!/usr/bin/python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15,GPIO.IN, pull_up_down=GPIO.PUD_UP)

while(True):
    GPIO.wait_for_edge(11, GPIO.RISING)
    print('Black button was pushed')
    GPIO.wait_for_edge(11, GPIO.FALLING)
    print('Black button was not pushed')
    GPIO.wait_for_edge(15, GPIO.RISING)
    print('Red button was pushed')
    GPIO.wait_for_edge(15, GPIO.FALLING)
    print('Red button was not pushed')
    
#pin 16 > resistor > button > pin 9

GPIO.cleanup()

