# Analisi e sviluppo raspberry

In questa fase ci doabbiamo occupare della recezione dati da parte dell'arduino e della successiva pubblicazione su un broker MQTT.

Bisogna creare un file unico per la recezione e sottoscrizione dei dati, a meno di voler provare a fare una pipe in `multiprocessing` con la libreria di python.

Prendere la stringa ricevuta e trasformarla in Json, cambiando anche il formato di invio dei dati del broker in modo statico.

Creare un servizione che permetta la lettura e il subscribe al topic per poter leggere i dati e fare un forward verso una pagina HTML.