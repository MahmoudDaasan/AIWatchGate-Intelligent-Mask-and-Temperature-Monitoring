import RPi.GPIO as GPIO
import time

servoPIN = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setwarnings(False)
pwm = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
pwm.start(2.5) # Initialization
def openGate():
    pwm.ChangeDutyCycle(2.0)
    #pigpio.set_PWM_dutycycle(2.0)
    sleep(0.5)
try:
  while True:
      openGate()
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
