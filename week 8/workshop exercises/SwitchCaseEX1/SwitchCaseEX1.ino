int selection; // prepare an integer variable called selection

void setup() {

  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
    Serial.println("Enter your selection 1 or 2: ");
}

void loop() {
  while(Serial.available()) {
    selection = Serial.readString().toInt();
      switch (selection) {
      case 1:
          Serial.println("1. Cappucino");
          //break;
      case 2:
          Serial.println("2. Latte");
          //break;
        default:
          Serial.println("Sorry, invalid selection");
        }
        Serial.println("Enter your selection again, 1 or 2:");
  }
}