int inputPin=4; // signal Rx pin ECHO to D4
int outputPin=5; // signal tTx pin TRIG to D5
void setup()

{

Serial.begin(9600);
pinMode(inputPin, INPUT);
pinMode(outputPin, OUTPUT);

}

void loop()

{

digitalWrite(outputPin, LOW);
delayMicroseconds(2);
digitalWrite(outputPin, HIGH);
delayMicroseconds(10);
digitalWrite(outputPin, LOW);
int distance = pulseIn(inputPin, HIGH); 
distance= distance/58;
Serial.print("Distance = ");  
Serial.print(distance);
Serial.println(" cm");

delay(200);
}