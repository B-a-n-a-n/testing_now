import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT, initial = GPIO.LOW)

p = GPIO.PWM(22,1000)

p.start(0)
try:
	while True:
		s = input("Set duty from 0 to 100: ")
		if (not s.isdigit()):
			continue
		value = int(s)
		if (value > 100):
			print("Too big ")
			continue
		elif value < 0:
			print("Should be more pozitive ")
			continue
		p.ChangeDutyCycle(value)
except KeyboardInterrupt:
	print("Stopped")
	pass
finally:
	p.stop()
	GPIO.cleanup()
	print("this is the end")


