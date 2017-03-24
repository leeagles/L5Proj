import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT)
print "LED ON"
GPIO.setup(4, GPIO.HIGH)
time.sleep(1)
print "LED OFF"
GPIO.setup(4, GPIO.LOW)

