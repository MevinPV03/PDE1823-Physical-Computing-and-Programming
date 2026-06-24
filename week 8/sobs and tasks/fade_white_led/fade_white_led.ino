
const int LED = 3;

void setup() {
    pinMode(LED, OUTPUT);
}

void loop() {

  // Fade in
  for (int i = 0; i <= 255; i++) {
    
    analogWrite(LED, i);

    delay(10);
  }

  // Fade out
  for (int i = 255; i >= 0; i--) {
   
    analogWrite(LED, i);

    delay(10);
  }
}