import time
import random
import paho.mqtt.client as mqtt

# MQTT details
mqtt_server = "192.168.1.176"
mqtt_port = 1883
mqtt_user = "mqtt_user"
mqtt_pass = "151008904"

# MQTT topics
echo_topic = "knocklight/echo"
hello_topic = "knocklight/hello"
set_color_topic = "knocklight/set_color"
get_color_topic = "knocklight/get_color"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

    # Subscribe to MQTT topics
    client.subscribe(echo_topic)
    client.subscribe(hello_topic)
    client.subscribe(get_color_topic)

def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode('utf-8')}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(mqtt_user, mqtt_pass)
client.connect(mqtt_server, mqtt_port, 60)

client.loop_start()

# Test echo feature
print("Testing echo feature...")
client.publish(echo_topic, "Echo this message")
time.sleep(2)

# Test hello world feature
print("Testing hello world feature...")
client.publish(hello_topic, "Requesting hello world")
time.sleep(2)

# Test set color feature
print("Testing set color feature...")
random_color = f"{random.randint(0, 255):02X}{random.randint(0, 255):02X}{random.randint(0, 255):02X}"
print(f"Setting color to {random_color}")
client.publish(set_color_topic, random_color)
time.sleep(2)

# Test get color feature
print("Testing get color feature...")
client.publish(get_color_topic, "Requesting current color")
time.sleep(2)

client.loop_stop()
client.disconnect()
