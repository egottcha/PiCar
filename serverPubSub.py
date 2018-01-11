from awsMQTT import AWSconnect
from getkeys import key_check
import time

# init
awsMQTTClient = AWSconnect("serverNode")
awsMQTTClient.connect()
print("AWS Client connected")


# device registration
def deviceRegister(client, userdata, message):
    print('comming soon...')

# awsMQTTClient.subscribe("piCar/#", 1, deviceRegister)

# piCar control
# static yet TODO: set dynamic topics from device registration
MOVE_ON = False
FWD_ON = False
TURN_ON = False
LEFT_ON = False

while True:
    keys = key_check()
    # print(keys)
    # '{"set": "ON"}'
    if ('W' in keys and MOVE_ON is False):
        awsMQTTClient.publish("piCar/nodeShortCode-1/relay-19", 0, 1)
        MOVE_ON = True
    elif ('W' not in keys and MOVE_ON is True):
        awsMQTTClient.publish("piCar/nodeShortCode-1/relay-19", 1, 1)
        MOVE_ON = False
    elif ('S' in keys and FWD_ON is False):
        awsMQTTClient.publish("piCar/nodeShortCode-1/relay-26", 0, 1)
        awsMQTTClient.publish("piCar/nodeShortCode-1/relay-19", 0, 1)
        FWD_ON = True
    elif ('S' not in keys and FWD_ON is True):
        awsMQTTClient.publish("piCar/nodeShortCode-1/relay-26", 1, 1)
        awsMQTTClient.publish("piCar/nodeShortCode-1/relay-19", 1, 1)
        FWD_ON = False
    elif ('A' in keys and LEFT_ON is False):
        awsMQTTClient.publish("piCar/nodeShortCode-1/relay-13", 0, 1)
        awsMQTTClient.publish("piCar/nodeShortCode-1/relay-6", 0, 1)
        LEFT_ON = True
    elif ('A' not in keys and LEFT_ON is True):
        awsMQTTClient.publish("piCar/nodeShortCode-1/relay-13", 1, 1)
        awsMQTTClient.publish("piCar/nodeShortCode-1/relay-6", 1, 1)
        LEFT_ON = False
    elif ('D' in keys and TURN_ON is False):
        awsMQTTClient.publish("piCar/nodeShortCode-1/relay-6", 0, 1)
        TURN_ON = True
    elif ('D' not in keys and TURN_ON is True):
        awsMQTTClient.publish("piCar/nodeShortCode-1/relay-6", 1, 1)
        TURN_ON = False
