import paho.mqtt.client as mqtt

user = "glatz"
broker = "mqtt.eclipseprojects.io"
topico = "chat/grupo"

def mensg(client, userdata, msg):
    message = msg.payload.decode()
    if not message.startswith(user):
        print(f"{message}")

def c(client, userdata, flags, rc):
    client.subscribe(topico)
    
def env_m(client):
    while True:
        msg = input()
        if msg:
            full_message = f"{user}: {msg}"
            client.publish(topico, full_message)

client = mqtt.Client()
client.c = c
client.mensg = mensg
client.connect(broker, 1883, 60)
client.loop_start()
env_m(client)