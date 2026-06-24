const int POT = 2;
const int RGB_RED = 11;
const int RGB_GREEN = 10;
const int RGB_BLUE = 9;

int val = 0;

void setup() {
  Serial.begin(115200);

  pinMode(POT, INPUT);
  pinMode(RGB_RED, OUTPUT);
  pinMode(RGB_GREEN, OUTPUT);
  pinMode(RGB_BLUE, OUTPUT);
}

void loop() {

  val = analogRead(POT);

  Serial.println(val);

  if (val >= 0 && val < 320) {          // Threshold 1
    digitalWrite(RGB_RED, HIGH);
    digitalWrite(RGB_GREEN, LOW);
    digitalWrite(RGB_BLUE, LOW);
  }
  else if (val >= 320 && val < 900) {   // Threshold 2
    digitalWrite(RGB_RED, LOW);
    digitalWrite(RGB_GREEN, HIGH);
    digitalWrite(RGB_BLUE, LOW);
  }
  else if (val >= 900 && val <= 1023) { // Threshold 3
    digitalWrite(RGB_RED, LOW);
    digitalWrite(RGB_GREEN, LOW);
    digitalWrite(RGB_BLUE, HIGH);
  }

  delay(100);
}