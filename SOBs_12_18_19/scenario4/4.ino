const int button1 = 2;
const int button2 = 3;

const int internalLED = 13;
const int externalLED = 8;

void setup() {

  pinMode(button1, INPUT_PULLUP);
  pinMode(button2, INPUT_PULLUP);

  pinMode(internalLED, OUTPUT);
  pinMode(externalLED, OUTPUT);
}

void loop() {

  // Button1 pressed
  if (digitalRead(button1) == LOW) {

    digitalWrite(internalLED, HIGH);
    digitalWrite(externalLED, HIGH);

    delay(200);
  }

  // Button2 pressed
  if (digitalRead(button2) == LOW) {

    digitalWrite(internalLED, LOW);
    digitalWrite(externalLED, LOW);

    delay(200);
  }
}