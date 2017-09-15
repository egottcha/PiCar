from numpy.core.defchararray import rfind
from awsMQTT import awsMQTT
from distanceReader import DistanceCollector
from config import piCarMovementGPIO, piCarDistanceGPIO
import RPi.GPIO as GPIO
import time

# init
awsMQTTClient = awsMQTT.create("self")
GPIO.setmode(GPIO.BCM)
GPIO.setup(piCarMovementGPIO.GPIO_MOVE, GPIO.OUT)
GPIO.setup(piCarMovementGPIO.GPIO_FWD, GPIO.OUT)
GPIO.setup(piCarMovementGPIO.GPIO_TURN, GPIO.OUT)
GPIO.setup(piCarMovementGPIO.GPIO_LEFT, GPIO.OUT)

GPIO.output(piCarMovementGPIO.GPIO_MOVE, 1)
GPIO.output(piCarMovementGPIO.GPIO_FWD, 1)
GPIO.output(piCarMovementGPIO.GPIO_TURN, 1)
GPIO.output(piCarMovementGPIO.GPIO_LEFT, 1)


# distanceFront = DistanceCollector(ECHO=piCarDistanceGPIO.FRONT_ECHO,
#                                   TRIGGER=piCarDistanceGPIO.FRONT_TRIGGER)
# distanceFrontLeft = DistanceCollector(ECHO=piCarDistanceGPIO.FRONT_LEFT_ECHO,
#                                       TRIGGER=piCarDistanceGPIO.FRONT_LEFT_TRIGGER)
# distanceFrontRight = DistanceCollector(ECHO=piCarDistanceGPIO.FRONT_RIGHT_ECHO,
#                                        TRIGGER=piCarDistanceGPIO.FRONT_RIGHT_TRIGGER)
# distanceBack = DistanceCollector(ECHO=piCarDistanceGPIO.BACK_ECHO,
#                                  TRIGGER=piCarDistanceGPIO.BACK_TRIGGER)
# distanceBackLeft = DistanceCollector(ECHO=piCarDistanceGPIO.BACK_LEFT_ECHO,
#                                      TRIGGER=piCarDistanceGPIO.BACK_LEFT_TRIGGER)
# distanceBackRight = DistanceCollector(ECHO=piCarDistanceGPIO.BACK_RIGHT_ECHO,
#                                       TRIGGER=piCarDistanceGPIO.BACK_RIGHT_TRIGGER)
# distanceLeft = DistanceCollector(ECHO=piCarDistanceGPIO.LEFT_ECHO,
#                                  TRIGGER=piCarDistanceGPIO.BACK_TRIGGER)
# distanceRight = DistanceCollector(ECHO=piCarDistanceGPIO.RIGHT_ECHO,
#                                   TRIGGER=piCarDistanceGPIO.RIGHT_TRIGGER)


def setGPIO(gpio, value):
    print(gpio, value)
    if (value == "b'ON'"):
        GPIO.output(gpio, 0)
    elif (value == "b'OFF'"):
        GPIO.output(gpio, 1)


def readGPIO(gpio):
    print('comming soon...')


# MQTT message callback: SET GPIO
def gpioSetter(client, userdata, message):
    print("SET DEVICE:", message.topic, "TO", message.payload)
    print("--------------\n\n")
    setGPIO(message.topic[rfind(message.topic, "-") + 1:], message.payload)


# MQTT message callback: READ GPIO
def gpioReader(client, userdata, message):
    print("READING DEVICE:", message.topic)
    print("--------------\n\n")
    readGPIO(message.topic[rfind(message.topic, "-") + 1:])


# device registration
# TODO: build up
# thisDevice = {
#     "relay-" + piCarMovementGPIO.GPIO_MOVE: {
#         "Name": "device1",
#         "Purpose": "doing xy"
#     },
#     "relay-" + piCarMovementGPIO.GPIO_FWD: {
#         "Name": "device2",
#         "Purpose": "doing xy"
#     },
#     "relay-" + piCarMovementGPIO.GPIO_TURN: {
#         "Name": "device3",
#         "Purpose": "doing xy"
#     },
#     "relay-" + piCarMovementGPIO.GPIO_LEFT: {
#         "Name": "device4",
#         "Purpose": "doing xy"
#     }
# }

awsMQTTClient.connect()
print("AWS IoT Client is connected.")
# awsMQTTClient.publish("piCar/nodeShortCode-1", thisDevice, 1)

# listener
awsMQTTClient.subscribe("piCar/nodeShortCode-1/#", 1, gpioSetter)
while True:
    i = 1
    # dist = distanceFront.readDistance()
    # if (dist < 20 and dist > 10):
    #     awsMQTTClient.publish("piCar/node1/dist", "{'Distance': " + str(round(dist, 2)) + "}", 0)
    # time.sleep(0.5)
