const int RED = 11;
const int GREEN = 10;
const int BLUE = 9;

void setup() {
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
}

void breathe(int colorPin) {

  for (int i = 0; i <= 255; i++) {
    analogWrite(colorPin, i);
    delay(10);
  }

  for (int i = 255; i >= 0; i--) {
    analogWrite(colorPin, i);
    delay(10);
  }
}

void loop() {
  breathe(RED);
  breathe(GREEN);
  breathe(BLUE);
}

/*
Observation:
The RGB LED performs a breathing effect on the red colour,
then green, then blue. Each colour slowly brightens and dims
before the next colour starts, producing a smooth colour-changing
breathing effect.
*/