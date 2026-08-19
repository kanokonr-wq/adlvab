import paho.mqtt.client as mqtt

broker = "mqtt.thaiappify.com"
port = 1883
topic = "/s000/topic"

# ฟังก์ชัน callback เมื่อมีข้อความใหม่เข้ามา
def on_message(client, userdata, msg):
    print(f"Topic: {msg.topic}, Message: {msg.payload.decode()}")

client = mqtt.Client()
client.username_pw_set("coe", "coe")
client.on_message = on_message

client.connect(broker, port, 60)
client.subscribe(topic)

print("Waiting for messages...")
client.loop_forever()
