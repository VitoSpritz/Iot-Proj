#include "src/BluetoothEventCatcher.h"
#include "src/BluetoothMsgService.h"
#include "src/LoggerTask.h"
#include "src/ProducerTask.h"
#include "src/Scheduler.h"
#include "src/SerialMsgService.h"
#include "src/SonarImpl.h"

#define SER_MSG_SERVICE_NAME "OUT"
#define SER_MSG_SERVICE_BAUD_RATE 9600
#define BT_MSG_SERVICE_NAME "BT"
#define BT_MSG_SERVICE_BAUD_RATE 9600
#define BT_TXD_PIN 2
#define BT_RXD_PIN 3
#define BT_STATE_PIN 5
#define ECHO_PIN 11     //da fare
#define TRIGGER_PIN 12  //da fare
#define BT_EVENT_CATCHER_TASK_PERIOD 100
#define LOGGER_TASK_PERIOD 100
#define PRODUCER_TASK_PERIOD 5000
#define SCHED_PERIOD 100

Scheduler sched;
SerialMsgService* serial;

void setup() {
    serial = new SerialMsgService(SER_MSG_SERVICE_NAME, SER_MSG_SERVICE_BAUD_RATE);
    BluetoothMsgService* bt =
        new BluetoothMsgService(BT_MSG_SERVICE_NAME, BT_TXD_PIN, BT_RXD_PIN, BT_STATE_PIN, BT_MSG_SERVICE_BAUD_RATE);

    BluetoothEventCatcher* btEventCatcher = new BluetoothEventCatcher(bt);
    btEventCatcher->init(BT_EVENT_CATCHER_TASK_PERIOD);

    LoggerTask* loggerTask = new LoggerTask(bt, serial);
    loggerTask->init(LOGGER_TASK_PERIOD);

    Sonar *sonar = new SonarImpl(ECHO_PIN, TRIGGER_PIN); 
    /*TODO
    * aggiungere a producerTask il sonar modificando i sorgenti e utilizzandolo come messaggio, aggiungere il convertitore da int a json per
    * farlo funzionare. Da testare con e senza json.
    */

    ProducerTask* producerTask = new ProducerTask(bt);
    producerTask->init(PRODUCER_TASK_PERIOD);

    sched.init(SCHED_PERIOD);
    sched.addTask(btEventCatcher);
    sched.addTask(loggerTask);
    sched.addTask(producerTask);
}

void loop() {
    sched.schedule();
}

void serialEvent() {
    serial->channelEvent();
}