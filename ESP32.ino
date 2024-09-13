#include<WiFi.h>
#include<HTTPClient.h>
#include<ArduinoJson.h>
//Set Connection
String incomingString;


void setup() {
  
  Serial.begin(115200);

}
void loop() {
  if (Serial.available()) {
    // read the incoming byte:
    incomingString = Serial.readStringUntil('l');
}
Serial.print(incomingString);
Serial.write('l');
}

