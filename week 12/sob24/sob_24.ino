#define TRIG_PIN 9
#define ECHO_PIN 10

#define LDR_PIN A0


void setup()
{
  Serial.begin(9600);

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}


void loop()
{

  // =====================
  // Read LDR Sensor
  // =====================

  int lightValue = analogRead(LDR_PIN);



  // =====================
  // Read Ultrasonic Sensor
  // =====================

  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);


  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);


  digitalWrite(TRIG_PIN, LOW);


  long duration = pulseIn(ECHO_PIN, HIGH);


  float distance = duration * 0.034 / 2;



  // =====================
  // Send data to Python
  // =====================

  Serial.print("LDR:");
  Serial.print(lightValue);


  Serial.print(",Distance:");
  Serial.println(distance);



  delay(1000);

}