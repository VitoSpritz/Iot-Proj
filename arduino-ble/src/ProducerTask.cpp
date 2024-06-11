#include "ProducerTask.h"
#include "Sonar.h"

ProducerTask::ProducerTask(MsgService* msgService, Sonar* sonar) {
    this->msgService = msgService;
    this->sonar = sonar;
}

void ProducerTask::tick() {
    if (msgService->isConnected()) {
        unsigned long data = millis();
        this->msgService->sendMsg(String("{ \"distance\":") + String(this->sonar->getDistance()) + " }");
    }
}