const int ldrPin = A0;

const int trigPin = 9;
const int echoPin = 10;

void setup()
{
  Serial.begin(9600);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop()
{
  int ldrValue = analogRead(ldrPin);

  // Ultrasonic Sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);

  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH);

  float distance = duration * 0.0343 / 2.0;

  Serial.print(ldrValue);
  Serial.print(",");
  Serial.println(distance);

  delay(1000);
}