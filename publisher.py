import time

import paho.mqtt.client as mqtt
import config


def on_publish(client, userdata, result):  # Create function for callback
    print("Data published \n")
    pass


client = mqtt.Client()  # MQTT Client Initilization
client.on_publish = on_publish  # Assign function to callback
client.connect(config.broker, config.port, 60)  # Establish connection

client.loop_start()

while True:
    client.publish(config.topic, "oasdasdn")  # Publish
    time.sleep(2)

client.loop_stop()
client.disconnect()
