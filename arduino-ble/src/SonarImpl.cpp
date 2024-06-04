#include "SonarImpl.h"
#include "Arduino.h"

SonarImpl::SonarImpl(int pinEcho, int pinTrigger){

    this->pinEcho = pinEcho;
    this->pinTrigger = pinTrigger;
}

float SonarImpl::getDistance(){
    
    float distance = getPulse() / 29 / 2 ;
    return distance;
}

float SonarImpl::getPulse(){

    pinMode(this->pinTrigger, OUTPUT);

    digitalWrite(this->pinTrigger, LOW);
    delayMicroseconds(2);
    digitalWrite(this->pinTrigger, HIGH);
    delayMicroseconds(10);
    digitalWrite(this->pinTrigger, LOW);

    pinMode(this->pinEcho, INPUT);

    float pulse = pulseIn(this->pinEcho, HIGH);
    return pulse;
}