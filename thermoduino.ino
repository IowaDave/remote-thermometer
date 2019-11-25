// This code borrows heavily from an example
// provided by Miles Burton, whose generous
// contributions to the community
// are gratefully acknowledged.

// Include the libraries we need
#include <OneWire.h>
#include <DallasTemperature.h>

// Data wire connects to port A0 on the Hyperduino
#define ONE_WIRE_PIN A0

// Setup a oneWire instance to communicate with the DS18B20, which is a onewire device
OneWire sensorWire(ONE_WIRE_PIN);

// Pass our oneWire reference to Dallas Temperature.
// This creates an object named dTemp through which we will talk to the thermometer
DallasTemperature dTemp(&sensorWire);

// arrays to hold device address - not needed?
DeviceAddress insideThermometer;

// variables for scheduling and storing
// temperature readings
unsigned long runTime;
unsigned long previousTime;
double theTemp;

void setup() {
  // enable pull-up on the thermometer pin in the Arduino
  pinMode(ONE_WIRE_PIN, INPUT_PULLUP);
  digitalWrite(ONE_WIRE_PIN, INPUT_PULLUP);
  // open the serial port on the Arduino 
  Serial.begin(9600);
}

void loop() {
   // get time elapsed since start
   runTime = millis();
   // Has 10 seconds passed since the last reading?
   if (runTime - previousTime > 10000) {
      // No? Skip to end and start loop over
      // Yes? Do the following:
      dTemp.requestTemperatures();
      theTemp = dTemp.getTempFByIndex(0);
      Serial.println(theTemp);
      previousTime = runTime;
   }
}
