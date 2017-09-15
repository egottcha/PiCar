import RPi.GPIO as GPIO
import time


class DistanceCollector:
    def __init__(self, ECHO, TRIGGER, decpulsetrigger=0.0001, inttimeout=2100):
        self.decpulsetrigger = decpulsetrigger  # Trigger duration
        self.inttimeout = inttimeout  # Number of loop iterations before timeout called
        # Which GPIO's are used [0]=BCM Port Number
        self.arrgpio = [ECHO, TRIGGER]
        # Set GPIO Channels
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.arrgpio[0], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.arrgpio[1], GPIO.OUT)
        GPIO.output(self.arrgpio[1], False)

    def readDistance(self):
        # Trigger high for 0.0001s then low
        GPIO.output(self.arrgpio[1], True)
        time.sleep(self.decpulsetrigger)
        GPIO.output(self.arrgpio[1], False)
        # Wait for echo to go high (or timeout)
        intcountdown = self.inttimeout
        while (GPIO.input(self.arrgpio[0]) == 0 and intcountdown > 0):
            intcountdown = intcountdown - 1
        # If echo is high
        if intcountdown > 0:
            # Start timer and init timeout countdown
            echostart = time.time()
            intcountdown = self.inttimeout
            # Wait for echo to go low (or timeout)
            while (GPIO.input(self.arrgpio[0]) == 1 and intcountdown > 0):
                intcountdown = intcountdown - 1
            # Stop timer
            echoend = time.time()
            # Echo duration
            echoduration = echoend - echostart
        # Display distance
        if intcountdown > 0:
            intdistance = (echoduration * 1000000) / 58
            print("Distance = " + str(intdistance) + "cm")
            return intdistance
        else:
            print("Distance - timeout")
            return 0
