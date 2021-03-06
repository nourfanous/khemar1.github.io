import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

def init():
	gpio.setmode(gpio.BOARD)
    	gpio.setup(7, gpio.OUT)
	gpio.setup(11, gpio.OUT)
	gpio.setup(13, gpio.OUT)
	gpio.setup(15, gpio.OUT)

def forward(tf):
	gpio.output(7, False)
	gpio.output(11, True)
	gpio.output(13, True)
	gpio.output(15, False)
	time.sleep(tf)
	gpio.cleanup()

forward(2)
