# Progetto Data flow

In questo progetto, raccoglieremo dati da un sensore collegato ad un Arduino. I dati raccolti verranno inviati tramite un modulo Bluetooth HC-05 al Raspberry Pi. Il Raspberry Pi riceverà i dati, li pubblicherà su un broker MQTT. Un altro software si sottoscrive a un topic MQTT per ricevere i dati, aggiornerà il suo stato e li renderà disponibili tramite un'API REST.
I dati sono trasmessi in formato JSON con questa struttura: `{“type”: “data_type”, “value”: value}`.
Ad esempio per la misura di una distanza potrebbe essere inviata nel formato: `{“type”: “distance”, “value”: 3.5}`.

## Obiettivi

Raccolta dati su arduino: Raccogliere periodicamente i dati da un sensore, es. HC-SR04, collegato ad un Arduino. Si può utilizzare un qualunque sensore l’obiettivo è solo quello di poter raccogliere dati.
Trasmettere i dati da Arduino a Raspberry Pi tramite un modulo Bluetooth HC-05.
Pubblicare i dati ricevuti su un broker MQTT.
Sottoscrivere un topic MQTT per ricevere i dati e aggiornare lo stato del sistema.
Esporre un'API REST per visualizzare i dati ricevuti.

## Sviluppo

Si possono utilizzare le architetture di controllo che si ritengono più adatte. Il consiglio è di costruire un sistema ben architettato ma non eccessivamente.
Libera scelta per i linguaggi e le librerie, l’importante è utilizzare i protocolli specificati sopra.
Per qualsiasi aspetto non specificato, fare la scelta che si ritiene più appropriata.

## Risultati Attesi

data-collector (Arduino): Raccoglie i dati dal sensore di distanza HC-05 e li invia in formato JSON tramite Bluetooth.
data-publisher (Raspberry): Riceve i dati dal modulo Bluetooth HC-05, li decodifica e li pubblica su un topic MQTT.
data-subscriber: Si sottoscrive al topic MQTT, aggiorna il suo stato con i dati ricevuti e fornisce un'API REST per accedere ai dati.

***

## Analisi e sviluppo arduino

Come base per il progetto siamo partiti dall'esercizio bl-comm fornitoci per creare una connessione bluetooth tramite il sensore HC-05.

Come sensore di raccolta dati abbiamo utilizzato il *Sensore ad ultrasuoni* per prendere ed inviare dati tramite bluetooth al raspberry. Per utilizzarlo abbiamo dovuto modificare il codice sorgente della **ProducerTask**, dandogli come argomento anche il puntatore al *Sonar*. Per semplificare l'invio dei dati tra dispositivi abbiamo optato per formattare il messaggio inviato al raspberry in formato Json, così da poterlo modificare liberamente in seguito.
