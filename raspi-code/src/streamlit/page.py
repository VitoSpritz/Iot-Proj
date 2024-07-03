import paho.mqtt.client as paho
from paho import mqtt
import streamlit as st
from datetime import datetime
import pandas as pd
import json
import queue
import time

data_queue = queue.Queue()

def on_message(client, userdata, msg):
    current_time = datetime.now().strftime('%H:%M:%S')
    payload = msg.payload.decode('utf-8')
    data = json.loads(payload)
    
    distance = data.get('distance')
    
    new_entry = {'Time': current_time, 'Distance': distance}
    
    data_queue.put(new_entry)

def subscribe():
    client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
    client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
    client.username_pw_set("subscriber", "subPass1")
    client.on_message = on_message
    client.connect("8ea59180f82845dda5325bc4b3beadf4.s1.eu.hivemq.cloud", 8883)
    client.subscribe("data", qos=1)
    client.loop_start()
    st.session_state.client = client

# Inizializza il DataFrame vuoto nel session state
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=['Time', 'Distance'])

# Funzione per aggiornare la tabella e il grafico in Streamlit
def update_data():
    while not data_queue.empty():
        new_entry = data_queue.get()
        new_entry_df = pd.DataFrame([new_entry])
        st.session_state.df = pd.concat([st.session_state.df, new_entry_df], ignore_index=True)

    table_placeholder.table(st.session_state.df)
    chart_placeholder.line_chart(st.session_state.df.set_index('Time'))

if __name__ == "__main__":
    st.title('MOQUITTO DALLA PARTITA')
    st.subheader('Dati raccolti da HiveMQ')

    st.markdown("Una bella prova di **Markdown**")
    st.sidebar.markdown("# Main page 🎈")

    if 'client' not in st.session_state and st.button('Subscribe'):
        subscribe()
        
    with st.expander("Tabella"):
        table_placeholder = st.empty()

    with st.expander("Grafico"):
        chart_placeholder = st.empty()

    # Aggiorna periodicamente la tabella e il grafico ogni 5 secondi
    while True:
        update_data()
        time.sleep(5)
