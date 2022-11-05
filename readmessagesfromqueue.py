import paho.mqtt.client as mqtt
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Smartphone")
client.connect(mqttBroker)

client.loop_start()
client.subscribe("TEMPERATURE")

#call the function to read the topic
client.on_message = on_message

time.sleep(30)
client.loop_end()

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))
    #TODO Add the logic to insert the messages into InfluxDB