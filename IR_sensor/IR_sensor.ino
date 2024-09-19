#include <Servo.h>

Servo myservo;
const int sensor = A0;

long sensor_reading;

void setup() {
  Serial.begin(9600);
  myservo.attach(9);
}

void loop() {
  // put your main code here, to run repeatedly:
  //sensor_reading = analogRead(sensor);

  Serial.println("sensor_reading");

  /*
  for (int pos = 0; pos < 180; pos += 1) {
    myservo.write(pos);
    delay(15);
  }
  for (int pos = 180; pos >= 1; pos -= 1) {
    myservo.write(pos);
    delay(15);
  }*/
  delay(1500);
}
