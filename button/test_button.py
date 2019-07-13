#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(false)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_UP)

while(True):
	input_value = GPIO.input(16)
	if (input_value = False):
		print("tombol ditekan")
		time.sleep(1)
	elif(input_value = True):
		print("tombol tidak ditekan")
		time.sleep(1)
		
GPIO.cleanup()


#tombol harus ditekan terus sehingga bisa terbaca ditekan
#rangkaian sesuai dengan yang ada dibuku
#dari pin 9 > tombol > resistor 300 Ohm > pin 16