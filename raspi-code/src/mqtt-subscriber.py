import paho.mqtt.client as paho
from paho import mqtt

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))   
    
client = paho.Client(client_id = "", userdata = None, protocol = paho.MQTTv5)
# Abilita tls
client.tls_set(tls_version = mqtt.client.ssl.PROTOCOL_TLS)
# Impostare username e password
client.username_pw_set("subscriber", "subPass1")

client.on_message = on_message

client.connect("", 8883)
client.subscribe("encyclopedia/#", qos=1)
client.loop_forever()

