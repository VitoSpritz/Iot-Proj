#ifndef __PRODUCER_TASK__
#define __PRODUCER_TASK__

#include "MsgService.h"
#include "Task.h"
#include "Sonar.h"

class ProducerTask : public Task {
   private:
    MsgService* msgService;
    Sonar* sonar;

   public:
    ProducerTask(MsgService* msgService, Sonar* sonar);
    void tick();
};

#endif
