import RPi.GPIO as GPIO
from config import move_pins
import time

def __init__():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(move_pins.PIN_MOVE, GPIO.OUT)
    GPIO.setup(move_pins.PIN_FWD, GPIO.OUT)
    GPIO.setup(move_pins.PIN_TURN, GPIO.OUT)
    GPIO.setup(move_pins.PIN_LEFT, GPIO.OUT)

    GPIO.output(move_pins.PIN_MOVE, 1)
    GPIO.output(move_pins.PIN_FWD, 1)
    GPIO.output(move_pins.PIN_TURN, 1)
    GPIO.output(move_pins.PIN_LEFT, 1)

def main():

    GPIO.output(move_pins.PIN_MOVE, 0)
    time.sleep(move_pins.operate_sleep)
    GPIO.output(move_pins.PIN_TURN, 0)
    time.sleep(move_pins.operate_sleep)
    GPIO.output(move_pins.PIN_MOVE, 1)
    time.sleep(move_pins.switch_sleep)
    GPIO.output(move_pins.PIN_LEFT, 0)
    GPIO.output(move_pins.PIN_FWD, 0)
    GPIO.output(move_pins.PIN_MOVE, 0)
    time.sleep(move_pins.operate_sleep)
    GPIO.output(move_pins.PIN_MOVE, 1)
    GPIO.output(move_pins.PIN_FWD, 1)
    GPIO.output(move_pins.PIN_LEFT, 1)
    GPIO.output(move_pins.PIN_TURN, 1)
    time.sleep(move_pins.switch_sleep)
    GPIO.output(move_pins.PIN_MOVE, 0)
    time.sleep(move_pins.operate_sleep)
    GPIO.output(move_pins.PIN_MOVE, 1)

    # stop everything
    time.sleep(move_pins.switch_sleep)
    GPIO.output(move_pins.PIN_MOVE, 1)
    GPIO.output(move_pins.PIN_FWD, 1)
    GPIO.output(move_pins.PIN_TURN, 1)
    GPIO.output(move_pins.PIN_LEFT, 1)

__init__()
main()
