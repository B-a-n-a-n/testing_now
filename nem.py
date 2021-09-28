import time
import RPi.GPIO as GPIO

def decimal_bibary(decimal):
	return [int(el) for el in bin(decimal)[2:].zfill(bits)]

def dac_bin(value):
	signal = decimal_bibary(value)
	GPIO.output(dac, signal)
	return signal

dac = [26,19,13,6,5,11,9,10]
bits = len(dac)
levels = 2**bits
max_V = 3.3
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

try:
	while True:
		s = input("Select number from 0 to 255: ")
		if (not s.isdigit()):
			continue
		value = int(s)
		if (value >= levels):
			print("Too big ")
			continue
		elif value < 0:
			print("Should be more pozitive ")
			continue
		signal = dac_bin(value)
		voltage = max_V*value/levels
		print("Inputing value: ",value,"Voltage on the thing: ", int(100*voltage)/100,"Pattern: ", *signal)
except KeyboardInterrupt:
	print("Stopped")
	pass
finally:
	GPIO.output(dac,GPIO.LOW)
	GPIO.cleanup()
	print("this is the end")
