String name; // prepare a var string called name
void setup() {
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  Serial.println("Enter your name: ");
}
void loop() {
  while (Serial.available()) {   // Serial.available() checks if any data has been sent from your computer to the Arduino and is waiting to be read. It returns the number of characters (bytes) currently stored in the Arduino's temporary memory buffer.
    name = Serial.readString(); // read the incoming data as string
    Serial.print("Hello ");
    Serial.println(name);
    Serial.println("Enter your name again: ");
  }
}

