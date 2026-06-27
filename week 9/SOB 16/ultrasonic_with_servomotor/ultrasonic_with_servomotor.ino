#include <Servo.h>

const int echoPin = 4;
const int trigPin = 5;

Servo myServo;

void setup()
{
  Serial.begin(9600);

  pinMode(echoPin, INPUT);
  pinMode(trigPin, OUTPUT);

  myServo.attach(2);   // Servo signal pin
}

void loop()
{
  // Trigger ultrasonic pulse
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);

  digitalWrite(trigPin, LOW);

  // Read distance
  unsigned long distance = pulseIn(echoPin, HIGH) / 58;

  Serial.print("Distance = ");
  Serial.print(distance);
  Serial.println(" cm");

  // Control servo according to distance
  if (distance < 10)
  {
    myServo.write(0);
  }
  else if (distance < 20)
  {
    myServo.write(90);
  }
  else
  {
    myServo.write(180);
  }

  delay(100);
}