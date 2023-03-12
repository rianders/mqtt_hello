import paho.mqtt.client as mqtt

# define a callback function to handle incoming messages
def on_message(client, userdata, message):
    print("Received message:", message.payload.decode())

# create a client instance
client = mqtt.Client()

# set the callback function for incoming messages
client.on_message = on_message

# set username and password
client.username_pw_set("mqtt_user", "151008904")

# connect to the broker and subscribe to a topic
client.connect("192.168.1.176")
# client.subscribe("homeassistant/plants/avocado")
client.subscribe("homeassistant/#")

# start the MQTT client loop to receive incoming messages
client.loop_forever()
