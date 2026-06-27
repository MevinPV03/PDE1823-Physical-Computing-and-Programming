#include <Servo.h>

const int echoPin = 4;
const int trigPin = 5;

const int redPin = 10;
const int greenPin = 11;
const int bluePin = 12;

Servo myServo;

void setup() {
  Serial.begin(9600);

  pinMode(echoPin, INPUT);
  pinMode(trigPin, OUTPUT);

  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

  myServo.attach(2);
}

void loop() {

  // Trigger ultrasonic sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);

  digitalWrite(trigPin, LOW);

  unsigned long distance = pulseIn(echoPin, HIGH) / 58;

  Serial.print("Distance = ");
  Serial.print(distance);
  Serial.println(" cm");

  if (distance > 30) {
    // Green
    digitalWrite(redPin, LOW);
    digitalWrite(greenPin, HIGH);
    digitalWrite(bluePin, LOW);

    myServo.write(180);
  }
  else if (distance > 15) {
    // Yellow (Red + Green)
    digitalWrite(redPin, HIGH);
    digitalWrite(greenPin, HIGH);
    digitalWrite(bluePin, LOW);

    myServo.write(90);
  }
  else {
    // Red
    digitalWrite(redPin, HIGH);
    digitalWrite(greenPin, LOW);
    digitalWrite(bluePin, LOW);

    myServo.write(0);
  }

  delay(50);
}