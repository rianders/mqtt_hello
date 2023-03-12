import paho.mqtt.client as mqtt

# create a client instance
client = mqtt.Client()


# set username and password
client.username_pw_set("mqtt_user", "151008904")

# connect to the broker
client.connect("192.168.1.176")

# publish a message to a topic
client.publish("homeassistant/plants/avocado", "Hello, MQTT!")
client.publish("homeassistant/plants/tomato", "Hello, From Tomator!")

# disconnect from the broker
client.disconnect()
