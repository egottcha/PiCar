from awsMQTT import awsMQTT
import time

# init
awsMQTTClient = awsMQTT.create("self")
awsMQTTClient.connect()
print("AWS Client connected")


def gpioSetter(client, userdata, message):
    print("SET DEVICE:", message.topic, "TO", message.payload)
    print("--------------\n\n")

awsMQTTClient.subscribe("piCar/nodeShortCode-1/#", 0, gpioSetter)

while True:
    i = 1
