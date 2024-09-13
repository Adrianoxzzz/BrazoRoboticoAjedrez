#include <HardwareSerial.h>
HardwareSerial SerialPort(1);

void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
SerialPort.begin(9600,SERIAL_8N1,16,17);
}

void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available()){
  String fen = Serial.readStringUntil('\n');
  SerialPort.println(fen)
}
if(SerialPort.available()){
  String response = SerialPort.readStringUntil('\n');
  Serial.println(response);
}
}
