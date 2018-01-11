from awsMQTT import AWSconnect
import time

# init
awsMQTTClient = AWSconnect("testSub")
awsMQTTClient.connect()
print("AWS Client connected")


def gpioSetter(client, userdata, message):
    print("SET DEVICE:", message.topic, "TO", message.payload)
    print("--------------")


awsMQTTClient.subscribe("piCar/nodeShortCode-1/#", 1, gpioSetter)

while True:
    time.sleep(15)
