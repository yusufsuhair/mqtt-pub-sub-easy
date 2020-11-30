import paho.mqtt.client as mqtt
import mysql.connector
from datetime import date
import config

# mydb = mysql.connector.connect(   # Connect into DB (OPTIONAL)
#     host="localhost",
#     user="root",
#     password="root",
#     database="iot"
# )


def on_message(client, userdata, msg): # Create function for callback
    payload = str(msg.payload.decode("utf-8"))
    print(payload)

    # mycursor = mydb.cursor()   # Insert into DB (OPTIONAL)
    # val = (mycursor.lastrowid, int(payload), date.today())
    # sql = "INSERT INTO data (id,pts,created_at) VALUES (%s, %s, %s)"
    # mycursor.execute(sql, val)
    # mydb.commit()


mqtt_client = mqtt.Client()  # MQTT Client Initialization
mqtt_client.on_message = on_message  # OnMessage callback
mqtt_client.connect(config.broker, config.port, 60)  # Connect to the broker
mqtt_client.subscribe(config.topic)  # Subscribe to a topic.
mqtt_client.loop_forever()  # Make it nonstop
