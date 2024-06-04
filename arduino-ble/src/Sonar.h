#ifndef __SONAR__
#define __SONAR__

class Sonar{

    public:
        virtual float getDistance() = 0;
        virtual float getPulse() = 0;
};

#endif