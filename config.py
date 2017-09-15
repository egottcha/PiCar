class sleepTimers:

    operate_sleep = 3
    switch_sleep = 0.5

class awsAuth:

    MQTT_ENDPOINT_URL = "a2frvvtba0aflq.iot.eu-central-1.amazonaws.com"
    MQTT_ENDPOINT_PORT = 8883
    AWS_ROOT_CERT = "cert/root-CA.crt"

    PICAR_CERT = "cert/e37875b3ad-certificate.pem.crt"
    PICAR_CERT_PRIVATE_KEY = "cert/e37875b3ad-private.pem.key"


class piCarMovementGPIO:
    # 0 it runs, 1 stays still
    GPIO_MOVE = 19
    # 0 it goes backwards, 1 goes forward
    GPIO_FWD = 26
    # 0 it turns right, 1 it doesn't turn
    GPIO_TURN = 6
    # 0 it turns left (only if PIN_TURN = 0), 1 it turns right (only if PIN_TURN = 0)
    GPIO_LEFT = 13

class piCarDistanceGPIO:
    FRONT_TRIGGER = 2
    FRONT_ECHO = 3

    FRONT_LEFT_TRIGGER = ""
    FRONT_LEFT_ECHO = ""

    FRONT_RIGHT_TRIGGER = ""
    FRONT_RIGHT_ECHO = ""

    BACK_TRIGGER = ""
    BACK_ECHO = ""

    BACK_LEFT_TRIGGER = ""
    BACK_LEFT_ECHO = ""

    BACK_RIGHT_TRIGGER = ""
    BACK_RIGHT_ECHO = ""

    LEFT_TRIGGER = ""
    LEFT_ECHO = ""

    RIGHT_TRIGGER = ""
    RIGHT_ECHO = ""