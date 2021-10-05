import time
import RPi.GPIO as GPIO

def decimal_bibary(decimal):
	return [int(el) for el in bin(decimal)[2:].zfill(bits)]

def dac_bin(value):
	signal = decimal_bibary(value)
	#GPIO.output(dac, signal)
	return signal


dac = [26,19,13,6,5,11,9,10]
leds = [21,20,16,12,7,8,25,24]
bits = len(dac)
levels= 2**bits
max_V = 3.3
troyka = 17
comparator = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(leds, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comparator, GPIO.IN)

def binary_acd():
    begin, end = 0, 256
    while begin < end:
        #time.sleep(0.01)
        value = (begin + end)//2
        signal = dac_bin(value)
        GPIO.output(dac, signal)
        time.sleep(0.002)
        comparatorValue = GPIO.input(comparator)
        if comparatorValue == 1:
            begin = value + 1
        else:
            end = value
    signal = dac_bin(value)
    GPIO.output(dac, signal)
    return value

def acd():
    for value in range(256):
        signal = dac_bin(value)
        #GPIO.output(dac, signal)
        time.sleep(0.002)
        comparatorValue = GPIO.input(comparator)
        if comparatorValue == 0:
            return value
def volume(value):
    c = int((8*value)/255)
    a = [0]*8
    for i in range(7,c-1,-1):
        a[i] = 1
    GPIO.output(leds, a)
    #time.sleep(0.1)

try:
	while True:
		#GPIO.output(dac,GPIO.LOW)
		value = binary_acd()
		volume(value)
		#voltage = ((max_V*value)/levels)
		#print("ADC value: ",value,"Voltage on the thing: ", int(100*voltage)/100)
		#time.sleep(0.5)
except KeyboardInterrupt:
	print("Stopped")
	pass
finally:
	GPIO.output(dac,GPIO.LOW)
	GPIO.cleanup()
	print("this is the end")