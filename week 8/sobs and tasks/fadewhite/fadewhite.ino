const int RED = 11;
const int GREEN = 10;
const int BLUE = 9;

void setup() {
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
}

void loop() {

  // Fade in
  for (int i = 0; i <= 255; i++) {
    analogWrite(RED, i);
    analogWrite(GREEN, i);
    analogWrite(BLUE, i);
    delay(10);
  }

  // Fade out
  for (int i = 255; i >= 0; i--) {
    analogWrite(RED, i);
    analogWrite(GREEN, i);
    analogWrite(BLUE, i);
    delay(10);
  }
}

/*
Observation:
All three colours increase and decrease in brightness together.
Since red, green and blue are ON at the same intensity, the RGB LED
appears white (or near-white) and produces a smooth breathing effect.
*/