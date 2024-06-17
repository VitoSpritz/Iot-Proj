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

client.connect("dfc1c3b30c4849f6bb3033da09ca3625.s1.eu.hivemq.cloud", 8883)

client.loop_forever()

try:
    # Pubblicazione dei dati sul topic MQTT
    client.subscribe("data", qos=1)

except KeyboardInterrupt:
    print("Interruzione del programma")
finally:
    # Disconnessione dal broker MQTT
    client.loop_stop()
    client.disconnect()
