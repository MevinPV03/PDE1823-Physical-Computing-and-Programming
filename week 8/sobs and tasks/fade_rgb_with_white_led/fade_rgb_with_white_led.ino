const int RED = 11;
const int GREEN = 10;
const int BLUE = 9;
const int LED = 3;

void setup() {
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
  pinMode(LED, OUTPUT);
}

void loop() {

  // Fade in
  for (int i = 0; i <= 255; i++) {
    analogWrite(RED, i);
    analogWrite(GREEN, i);
    analogWrite(BLUE, i);

    analogWrite(LED, i);

    delay(10);
  }

  // Fade out
  for (int i = 255; i >= 0; i--) {
    analogWrite(RED, i);
    analogWrite(GREEN, i);
    analogWrite(BLUE, i);

    analogWrite(LED, i);

    delay(10);
  }
}