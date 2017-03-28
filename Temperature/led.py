import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT)

print "the LED ON"
GPIO.setup(4, True)
time.sleep(1)
print "the LED OFF"
GPIO.setup(4, False)
GPIO.cleanup()
