#ifndef __SONARIMPL__
#define __SONARIMPL__

#include "Sonar.h"

class SonarImpl : public Sonar{

    public:
        SonarImpl(int pinEcho, int pinTrigger);
        float getDistance();
        float getPulse();
    
    private:
        int pinEcho;
        int pinTrigger;
};

#endif