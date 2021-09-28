import time
import RPi.GPIO as GPIO

def decimal_bibary(decimal):
	return [int(el) for el in bin(decimal)[2:].zfill(bits)]

def dac_bin(value):
	signal = decimal_bibary(value)
	GPIO.output(dac, signal)
	return signal

def next_num(num,stat):
    if num == 255:
        dac_bin(num)
        return 254, -1
    elif num == 0:
        dac_bin(num)
        return 1, 1
    else:
        return num+stat, stat

dac = [26,19,13,6,5,11,9,10]
bits = len(dac)
levels = 2**bits
max_V = 3.3
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

stat = 1
curr_num = 0
dac_bin(curr_num)
try:
	while True:
		curr_num, stat = next_num(curr_num, stat)
		dac_bin(curr_num)
		time.sleep(0.03)
		print(*dac_bin(curr_num), curr_num)
except KeyboardInterrupt:
	print("Stopped")
	pass
finally:
	GPIO.output(dac,GPIO.LOW)
	GPIO.cleanup()
	print("this is the end")

