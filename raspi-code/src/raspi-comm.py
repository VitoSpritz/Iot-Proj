import bluetooth
import asyncio
import time
import json
import time
import ssl
from paho import mqtt
import paho.mqtt.client as paho
import paho.mqtt.publish as publish

def onSubscribe(payload):
    
    client = paho.Client(client_id = "", userdata = None, protocol = paho.MQTTv5)
    # Abilita tls
    client.tls_set(tls_version = mqtt.client.ssl.PROTOCOL_TLS)
    # Impostare username e password
    client.username_pw_set("rootUser", "rootPass1")
    #Insert url here
    client.connect("", 8883)

    client.loop_start()
    
    try:
        # Pubblicazione dei dati sul topic MQTT
        client.publish("data", payload = payload, qos = 1)
        print(f"Dati pubblicati: {payload}")

    except KeyboardInterrupt:
        print("Interruzione del programma")
    finally:
        # Disconnessione dal broker MQTT
        client.loop_stop()
        client.disconnect()


def find_device(device_name):
    print("Scanning for Bluetooth devices...")
    devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)

    if devices:
        print(f"Found {len(devices)} devices:")
        for addr, name in devices:
            print(f"  {name} - {addr}")
            if name == device_name:
                print(f"Device {device_name} found with address {addr}")
                return addr
    else:
        print("No devices found.")
    return None

def connect_bluetooth(address):
    port = 1
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    try:
        print(f"Connecting to {address}...")
        sock.connect((address, port))
        print("Connected successfully!")
        return sock
    except bluetooth.btcommon.BluetoothError as err:
        print(f"Failed to connect: {err}")
        return None

class DataReceiver:
    def __init__(self, sock):
        self.buffer: str = ""
        self.sock = sock

    async def receive_data(self):
        data = self.sock.recv(1024).decode('utf-8')
        self.buffer += data

        while '\n' in self.buffer:
            line, self.buffer = self.buffer.split('\n', 1)
            if line:
                data = line.strip()
                #print(f"Received from arduino {data}")
                return data

async def send_data(sock):
    await asyncio.sleep(5) # wait 5 seconds

async def main():
    device_name = 'HC-05'
    address = find_device(device_name)
    if address:
        sock = connect_bluetooth('98:D3:31:F6:44:5D')
        if sock:
            try:
                receiver = DataReceiver(sock)
                while True:
                    await send_data(sock)
                    toJson = await receiver.receive_data()
                    try:
                        json_object = json.loads(toJson)
                        sock.send(f"Recieved {toJson}\n")
                        onSubscribe(json.dumps(json_object))
                    except json.JSONDecodeError as e:
                        print(f"Errore nel parsing del JSON: {e}")
            except KeyboardInterrupt:
                print("Disconnected")
            finally:
                sock.close()
        else:
            print("Could not connect to the device.")
    else:
        print(f"Device {device_name} not found.")

if __name__ == "__main__":
    asyncio.run(main())
