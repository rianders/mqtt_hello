import paho.mqtt.client as mqtt

# MQTT details
mqtt_server = "192.168.1.176"
mqtt_port = 1883
mqtt_user = "mqtt_user"
mqtt_pass = "151008904"

# MQTT topics
hello_topic = "knocklight/knock_detected"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

    # Subscribe to MQTT topics
    client.subscribe(hello_topic)

def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode('utf-8')}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(mqtt_user, mqtt_pass)
client.connect(mqtt_server, mqtt_port, 60)

# Keep the script running and listening for messages
client.loop_forever()
