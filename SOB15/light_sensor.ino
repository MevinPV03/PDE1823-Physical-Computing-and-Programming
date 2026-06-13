const int analogInPin = A2;
const int ledPin = 13;
const int buzzerPin = 8;

int sensorValue = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  // read the analog in value:
  sensorValue = analogRead(analogInPin);

  Serial.print("sensor= ");
  Serial.println(sensorValue);

 
  if (sensorValue < 100) {
   
    digitalWrite(buzzerPin, HIGH); 
    digitalWrite(ledPin, LOW);
  } 
  else if (sensorValue < 300) {
    
    digitalWrite(buzzerPin, LOW);
    digitalWrite(ledPin, LOW);   
  } 
  else {
    
    digitalWrite(ledPin, HIGH);    
    digitalWrite(buzzerPin, LOW);
  }

  
  delay(100);
}
