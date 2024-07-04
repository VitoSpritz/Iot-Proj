# Analisi e sviluppo raspberry

In questa fase ci doabbiamo occupare della recezione dati da parte dell'arduino e della successiva pubblicazione su un broker MQTT.

Abbiamo creato uno script unico che comprende la connessione via bluetooth e il caricamento dei dati su MQTT. Come prima cosa abbiamo modificato in buona parte lo script dato come esempio presente nella cartella *bt-comm*, così da avere una base per la comunicazione bluetooth. Una volta acccertata la connessione con l'arduino abbiamo gestito il flusso di dati in entrata e li abbiamo formattati in oggetti Json, così da poterli inviare a un broker MQTT.

## HiveMQ

Inizialmente il prototipo funzionava solo in localhost e, una volta finito il testing e accertati del funzionamento siamo passati ad utilizzare il servizio ***HiveMQ***, creando un cluster e connettendoci gestendo la connessione *tls* al broker. Per fare questo ci siamo basati principalmente sulla guida per la connessione in python reperibile nella documentazione di [HiveMQ](https://www.hivemq.com/blog/mqtt-client-library-paho-python/).

Seguendo la documentazione abbiamo anche creato degli utenti con privilegi diversi per effettuare le varie azioni di *publish e subscribe*. Qui riportati nomi e password dei due utenti creati nel pannello degli accessi di HiveMQ:

| Nome | Password |
| - | - |
| rootUser | rootPass1 |
|subscriber | subPass1 |

## Visualizzazione dati

Una volta accertati del funzionamento abbiamo pensato di creare una piccola pagina prototipo per mostrare i dati in modo *chiaro e più leggibile* di una semplice stringa su una shell, per questo con un po' di ricerca ci siamo imbattuti in [streamlit](https://streamlit.io), una libreria Python che permette di prototipare una pagina web in modo facile e veloce. Inoltre questa libreria supporta moltissimi widget per fare *plotting* di grafici, tabelle e tutto quello che riguarda i dati. La sincornizzazione della pagina è stata una bella sfida, dovendo controllare due theread, ovvero quello di *MQTT* e quello di *Streamlit*, ma alla fine abbiamo fatto due sezioni, una con una tabella e una con un *line chart* per visualizzazre i dati. Per avviare la pagina streamlit bisogna aprire una shell nella cartella `/src/streamlit` e con il comando `streamlit run page.py` verrà avviata la pagina in locale.
