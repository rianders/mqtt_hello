# Getting Started with MQTT and Home Assistant

This repository contains a simple example of how to use MQTT with Python and Home Assistant.

## Requirements

- Python 3.x
- Paho MQTT client library (`paho-mqtt`)

## Installation

1. Install the required Python packages:

`!pip install poetry paho-mqtt


2. Clone this repository:

git clone https://github.com/rianders/mqtt_hello.git



## Running the Example

1. Start the Mosquitto broker with authentication enabled:

mosquitto -c /path/to/mosquitto.conf -v

markdown
Copy code

2. Run the MQTT message publisher:

poetry run python mqtt_hello/mqtt_publisher.py

markdown
Copy code

3. Run the MQTT message subscriber:

poetry run python mqtt_hello/mqtt_subscriber.py

yaml
Copy code

4. Verify that the message publisher and subscriber are working correctly by checking the output.

5. Configure Home Assistant to use your Mosquitto broker by adding a MQTT broker configuration to your `configuration.yaml` file. For example:

```yaml
mqtt:
  broker: 192.168.1.176
  port: 1883
  username: mqtt_user
  password: password
Create a sensor using the mqtt platform to subscribe to the desired topic and display the message payload as a sensor value. For example:

yaml
Copy code
sensor:
  - platform: mqtt
    name: "Avocado Plant Moisture"
    state_topic: "homeassistant/plants/avocado"
    unit_of_measurement: "%"