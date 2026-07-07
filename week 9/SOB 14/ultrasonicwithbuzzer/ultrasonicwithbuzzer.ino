#include <Servo.h>

const int echoPin = 4;
const int trigPin = 5;

const int redPin = 10;
const int greenPin = 11;
const int bluePin = 12;

const int buzzerPin = 7;

Servo myServo;

void setup()
{
  Serial.begin(9600);

  pinMode(echoPin, INPUT);
  pinMode(trigPin, OUTPUT);

  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

  pinMode(buzzerPin, OUTPUT);

  myServo.attach(9);
}

void loop()
{
  // Trigger HC-SR04
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);

  digitalWrite(trigPin, LOW);

  unsigned long distance = pulseIn(echoPin, HIGH) / 58;

  Serial.print("Distance = ");
  Serial.print(distance);
  Serial.println(" cm");

  if (distance > 30)
  {
    // Green
    digitalWrite(redPin, LOW);
    digitalWrite(greenPin, HIGH);
    digitalWrite(bluePin, LOW);

    digitalWrite(buzzerPin, LOW);

    myServo.write(180);
  }
  else if (distance > 15)
  {
    // Yellow
    digitalWrite(redPin, HIGH);
    digitalWrite(greenPin, HIGH);
    digitalWrite(bluePin, LOW);

    digitalWrite(buzzerPin, LOW);

    myServo.write(90);
  }
  else
  {
    // Red + Buzzer ON
    digitalWrite(redPin, HIGH);
    digitalWrite(greenPin, LOW);
    digitalWrite(bluePin, LOW);

    digitalWrite(buzzerPin, HIGH);

    myServo.write(0);
  }

  delay(50);
}u