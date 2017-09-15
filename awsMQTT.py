class awsMQTT:
    def create(self):
        from config import awsAuth as aws
        from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

        # Credentials
        myMQTTClient = AWSIoTMQTTClient("piCarNode")
        myMQTTClient.configureEndpoint(aws.MQTT_ENDPOINT_URL, aws.MQTT_ENDPOINT_PORT)
        myMQTTClient.configureCredentials(aws.AWS_ROOT_CERT, aws.PICAR_CERT_PRIVATE_KEY, aws.PICAR_CERT)

        # MQTT config
        myMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
        myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
        myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
        myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
        myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

        return myMQTTClient
