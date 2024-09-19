#include <Servo.h>

String delimiter = ",";

Servo myservo;
const int sensor = A0;

int angle_1;
int angle_2;
long sensor_reading;

void setup() {
  Serial.begin(9600);
  myservo.attach(9);
}

void loop() {
  // put your main code here, to run repeatedly:
  //sensor_reading = analogRead(sensor);
  angle_1 = random(0, 180);
  angle_2 = random(0, 180);
  sensor_reading = random(5, 24);
  
  String print_to_serial = angle_1 + delimiter + angle_2 + delimiter + sensor_reading;
  Serial.print(print_to_serial);

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
