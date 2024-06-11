# Analisi e sviluppo raspberry

In questa fase ci doabbiamo occupare della recezione dati da parte dell'arduino e della successiva pubblicazione su un broker MQTT.

Creato script unico che comprende la connessione via bluetooth e il caricamento dei dati su MQTT, funzionanete in localhost per il momento. Opzionalmente da implementarlo con server HiveMQ, utilizzando la guida a questo [link](https://www.hivemq.com/blog/implementing-mqtt-in-python/).

Creare un servizione che permetta la lettura e il subscribe al topic per poter leggere i dati e fare un forward verso una pagina HTML. Questo è possibile con il subscribe fatto in node che andrà a popolare una pagina/tabella con i dati ricevuti.
