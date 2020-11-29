import time

import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
port = 1883
topic = "testyusuf1998" # If you use global broker, it is best to make it unique


def on_publish(client, userdata, result):  # Create function for callback
    print("data published \n")
    pass


client = mqtt.Client()  # MQTT Client Initilization
client.on_publish = on_publish  # Assign function to callback
client.connect(broker, port, 60)  # Establish connection

client.loop_start()
time.sleep(1)

while True:
    ret = client.publish("testyusuf1998", "oasdasdn")  # Publish
    time.sleep(15)


client.loop_stop()
client.disconnect()
