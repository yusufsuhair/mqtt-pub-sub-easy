import paho.mqtt.client as mqtt
import mysql.connector
from datetime import date

# mydb = mysql.connector.connect(   # Connect into DB (OPTIONAL)
#     host="localhost",
#     user="root",
#     password="root",
#     database="iot"
# )


broker = "broker.hivemq.com"
port = 1883
topic = "testyusuf1998" # If you use global broker, it is best to make it unique


def on_message(client, userdata, msg): # Create function for callback
    payload = str(msg.payload)

    # Removing "b" and "'' from message from the publisher.
    # Idk, its auto generated ...
    payload = payload.translate({ord("'"): None})
    payload = payload.translate({ord("b"): None})
    payload = payload.replace(' ', '')
    payload.translate({ord("'"): None})

    print(payload)

    # mycursor = mydb.cursor()   # Insert into DB (OPTIONAL)
    # val = (mycursor.lastrowid, int(payload), date.today())
    # sql = "INSERT INTO data (id,pts,created_at) VALUES (%s, %s, %s)"
    # mycursor.execute(sql, val)
    # mydb.commit()


mqtt_client = mqtt.Client()  # MQTT Client Initialization
mqtt_client.on_message = on_message  # OnMessage callback
mqtt_client.connect(broker, port, 60)  # Connect to the broker
mqtt_client.subscribe(topic)  # Subscribe to a topic.
mqtt_client.loop_forever()  # Make it nonstop
