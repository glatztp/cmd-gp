import paho.mqtt.client as mqtt

user = "glatz"
broker = "mqtt.eclipseprojects.io"
topico = "chat/grupo"

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    if not message.startswith(user):
        print(f"\n{message}")

def on_connect(client, userdata, flags, rc):
    client.subscribe(topico)


def send_message(client):
    while True:
        msg = input()
        if msg:
            full_message = f"{user}: {msg}"
            client.publish(topico, full_message)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, 1883, 60)
client.loop_start()
send_message(client)