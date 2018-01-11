from awsMQTT import AWSconnect
import time

# init
awsMQTTClient = AWSconnect("testPub")
awsMQTTClient.connect()
print("AWS Client connected")

i = 0

while True:
    awsMQTTClient.publish("piCar/nodeShortCode-1/dist", "test" + str(i), 1)
    print(i)
    i = i+1
    time.sleep(10)
