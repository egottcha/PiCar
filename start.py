from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import RPi.GPIO as GPIO
from config import move_pins, aws_mqtt
import time

# def __init__():
# AWS MQTT
myMQTTClient = AWSIoTMQTTClient("PiCar1")
myMQTTClient.configureEndpoint(aws_mqtt.MQTT_ENDPOINT_URL, aws_mqtt.MQTT_ENDPOINT_PORT)
myMQTTClient.configureCredentials(aws_mqtt.AWS_ROOT_CERT, aws_mqtt.PICAR_CERT_PRIVATE_KEY, aws_mqtt.PICAR_CERT)
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

# GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(move_pins.PIN_MOVE, GPIO.OUT)
GPIO.setup(move_pins.PIN_FWD, GPIO.OUT)
GPIO.setup(move_pins.PIN_TURN, GPIO.OUT)
GPIO.setup(move_pins.PIN_LEFT, GPIO.OUT)

GPIO.output(move_pins.PIN_MOVE, 1)
GPIO.output(move_pins.PIN_FWD, 1)
GPIO.output(move_pins.PIN_TURN, 1)
GPIO.output(move_pins.PIN_LEFT, 1)


# Custom MQTT message callback
def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")


# def main():
# __init__()
myMQTTClient.connect()
myMQTTClient.subscribe("MOVE", 1, customCallback)

myMQTTClient.publish("MOVE", "ON", 0)
GPIO.output(move_pins.PIN_MOVE, 0)
time.sleep(move_pins.operate_sleep)
time.sleep(move_pins.operate_sleep)
myMQTTClient.publish("MOVE", "OFF", 0)
GPIO.output(move_pins.PIN_MOVE, 1)

# stop everything
time.sleep(move_pins.switch_sleep)
GPIO.output(move_pins.PIN_MOVE, 1)
GPIO.output(move_pins.PIN_FWD, 1)
GPIO.output(move_pins.PIN_TURN, 1)
GPIO.output(move_pins.PIN_LEFT, 1)

myMQTTClient.unsubscribe("MOVE")
myMQTTClient.disconnect()
