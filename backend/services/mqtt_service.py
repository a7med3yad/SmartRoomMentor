import paho.mqtt.client as mqtt
import json
from backend.services.supabase_service import insert_sensor_data

# إعداد السيرفر بتاع HiveMQ Cloud
MQTT_SERVER = "c55e6a8f972b49d5ac18ac8547c303ee.s1.eu.hivemq.cloud"
MQTT_PORT = 8883
MQTT_USER = "hivemq.webclient.1756471531545"
MQTT_PASS = "D1o0ZS>g4ifjLa.#@9ON"

# نخلي الـ client والبيانات جلوبال
mqtt_client = None
last_data = None

# Callback لما يوصلك اتصال
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to MQTT broker")
        client.subscribe("servo/control")
        client.subscribe("room/threshold/temp")
        client.subscribe("room/threshold/hum")
        client.subscribe("room/threshold/gas")
        client.subscribe("room/led/control")
        client.subscribe("room/data")
    else:
        print(f"❌ MQTT connection failed with code {rc}")

# Callback لما توصلك رسالة
def on_message(client, userdata, msg):
    global last_data
    payload = msg.payload.decode()
    print(f"📩 MQTT [{msg.topic}]: {payload}")

    if msg.topic == "servo/control":
        print(f"🔧 Servo control => {payload}")
    elif msg.topic == "room/led/control":
        print(f"💡 LED control => {payload}")
    elif msg.topic.startswith("room/threshold/"):
        print(f"📊 Threshold update => {msg.topic}: {payload}")
    elif msg.topic == "room/data":
        print(f"📡 Sensor Data => {payload}")
        last_data = payload  # نخزن آخر بيانات المستشعر
        try:
            data = json.loads(payload)
            insert_sensor_data(
                temperature=data.get("temp", 0),
                humidity=data.get("hum", 0),
                gas_level=data.get("gas", 0),
                object_detected=bool(data.get("ir", 0)),
                user_id=1,
                room="default"
            )
            print("✅ Sensor data saved to Supabase")
        except json.JSONDecodeError:
            print("❌ Failed to parse sensor data")

# تشغيل MQTT client
def start_mqtt():
    global mqtt_client
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set(MQTT_USER, MQTT_PASS)
    mqtt_client.tls_set()  # SSL
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    mqtt_client.connect(MQTT_SERVER, MQTT_PORT, 60)
    mqtt_client.loop_start()
    return mqtt_client

# دوال النشر
def publish_led(state: str):
    if mqtt_client:
        mqtt_client.publish("room/led/control", state)
        print(f"📤 Published LED state: {state}")

def publish_threshold(sensor: str, value: str):
    if mqtt_client:
        topic = f"room/threshold/{sensor}"
        mqtt_client.publish(topic, value)
        print(f"📤 Published threshold => {topic}: {value}")

def get_last_data():
    return last_data