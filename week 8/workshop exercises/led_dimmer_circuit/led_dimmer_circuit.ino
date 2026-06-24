int ledPin = 9;
int analogPin = A0;
int val = 0;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  pinMode(analogPin, INPUT);
}
void loop() {
  val = analogRead(analogPin);
  Serial.println(val);
  delay(10);
  analogWrite(ledPin, val/4 );
}