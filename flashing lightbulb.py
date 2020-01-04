import RPi.GPIO as GPIO, time
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
def blinkOnce(pin):
    GPIO.output(pin,True)
    time.sleep(2)
    GPIO.output(pin,False)
    time.sleep(2)
for i in range(10):
    blinkOnce(27)
GPIO.cleanup()
        
