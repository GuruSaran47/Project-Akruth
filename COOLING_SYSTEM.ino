#include<Servo.h>
/*========================== all definations below =============================*/
#define isDEBUG_MODES 1

#ifdef printDebugLog 
#define isDEBUG 1 
#define DEBUG_NORMAL_MODE 1
#endif

#define MIN_THROTTLE 1000
#define MAX_THROTTLE 2000
#define BAUD_RATE 9600 /* Base Baud Rate set to 9600 */
#define DIGITAL_CONTROL_PIN 4 /* Not Decided yet */
#define ESC_CONTROL_PIN 5 /* for ESC Control */
#define FULL_SPEED_INTERRUPT_PIN 2 /* btn 1 */
#define KILL_OPS_INTERRUPT_PIN 3 /* btn 2 */
#define NORMAL_OPS 8 /* btn 3 */
#define ANALOG_PIN A0 /* for analog Mapping */
#define FULL_SPEED_TIME 8000 /* fill later */
/*================================= all definations above ===================*/
/*
*   variables are below
*   measure_voltage : from voltage divider.
*   measured_temperature: corelation between resistance, the voltage and temperature.
*   
*/
Servo ESC;
int measuredVoltage, measureTemprature,voltageMap,normalRequestCounter=0;
unsigned int fullSpeedOpCounter =0, measureESC,percentageMap, throttle;//finish later
bool fullSpeedFlag = false, killOpFlag = false, normalOpFlag = false;
/*
* Name : setFullSpeedOp()
* desc : function is used to set the fullSpeedOpFlag as true and rest all flags as false
*/
void setFullSpeedOp(){
  killOpFlag = false;
  normalOpFlag = false;
  fullSpeedFlag = true;
#ifdef isDEBUG
  Serial.println("FULL");
#endif
}
/*
* Name : setNormalOp()
* desc : function is used to set the normalOpFlag as true and rest all flags as false
*/
void setNormalOp(){
  killOpFlag = false;
  normalOpFlag = true;
  fullSpeedFlag = false;

  fullSpeedOpCounter = 0;

#ifdef isDEBUG
  Serial.println("NORMAL");
#endif
}
/*
* Name :: killAllOp()
* desc  : function is used for stopping all the operations till the normalOp flag is triggered, this function sets on the killOpFlag and clears the other two flags
*/
void killAllOp(){
  killOpFlag = true;
  normalOpFlag = false;
  fullSpeedFlag = false;

  fullSpeedOpCounter = 0;
#ifdef isDEBUG
  Serial.println("KILL");
#endif
}
/*
*   Name :: checkFlags() : look for triggers of the three buttons
*   desc :: we look for any of the three buttons that are pressed to look for triggers
*   working :: btn1 will trigger fullSpeedFlag, btn2 will trigger killOpFlag, btn3 will trigger normalOpFlag. where normalOpFlag is naturally true at setup 
*/
void checkFlag(){
  if (digitalRead(NORMAL_OPS) == 1){
    /* Set normalOp flag as true*/
    if((normalRequestCounter >=150) && (!(fullSpeedFlag) || !(killOpFlag))){
      setNormalOp();
      normalRequestCounter = 0;
    }
    else{
      normalRequestCounter++;
      
    }
  }
}

/*
*   Name :: measureVoltage(): read analog signal from Analog Pin
*   Desc :: Function measures the voltage level and maps it on the 5V ADC, this is later modded to 600 considering the tropical climate in mind. 
*   working :: at 7 to 15 range of mapping as a sample range and the throttle percentage will be mapped against it. 
*/
void measureVoltage(){
  voltageMap = ((int)analogRead(ANALOG_PIN))%600;
#ifdef DEBUG_NORMAL_MODE
  Serial.print("VoltageMap :");
  Serial.println(voltageMap);
#endif
}

/*
*   Name : mapThrottle() 
*   Desc : function is used to map the voltageMap value to the throttle percentage, this value is with the base of 100
*/
void throttleMap(){
  percentageMap = map(voltageMap,5,15,0,100);

#ifdef DEBUG_NORMAL_MODE
  Serial.print("PercentageMap: ");
  Serial.println(percentageMap);
#endif
}
/*
* Name: runESC()
* desc: runs ESC based on the flags set.
*/
void runESC(){
  if(normalOpFlag){
    throttle = map(percentageMap,0,100,0,180);
    ESC.write(throttle);

#ifdef isDEBUG_MODES
  Serial.println("Normal Mode");
  // Serial.print("Throttle: ");
  // Serial.println(throttle);
#endif

  }
  else if(killOpFlag){
    throttle = 0;
    ESC.write(throttle);
#ifdef isDEBUG_MODES
  Serial.println("KILL Mode");
#endif
  }
  else if(fullSpeedFlag){
    if(fullSpeedOpCounter<=FULL_SPEED_TIME){
      fullSpeedOpCounter++;
      ESC.write(180);
    }
    else{
      fullSpeedOpCounter = 0;
    }
#ifdef isDEBUG_MODES
  Serial.println("FULL SPEED Mode");
#endif
  }
  else{
    /* Do Nothing */
  }
}
void setup() {
  // put your setup code here, to run once:
  Serial.begin(BAUD_RATE);
  ESC.attach(5,MIN_THROTTLE, MAX_THROTTLE);
  /* Normal lPins are defined below */
  pinMode(ANALOG_PIN,INPUT);
  pinMode(DIGITAL_CONTROL_PIN,INPUT);
  pinMode(FULL_SPEED_INTERRUPT_PIN,INPUT);

  pinMode(NORMAL_OPS,INPUT);
  pinMode(KILL_OPS_INTERRUPT_PIN,OUTPUT);
  
  /* Interrupts are defined below  */
  attachInterrupt(digitalPinToInterrupt(FULL_SPEED_INTERRUPT_PIN),setFullSpeedOp,HIGH);
  attachInterrupt(digitalPinToInterrupt(KILL_OPS_INTERRUPT_PIN),killAllOp,HIGH);
  // normalOpFlag = true;
  setNormalOp();
}

void loop() {
  // put your main code here, to run repeatedly:
  checkFlag();
  measureVoltage();
  throttleMap();
  runESC();

}
