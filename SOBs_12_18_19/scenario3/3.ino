const int buttonPin = 2;
const int ledPin = 13;

bool ledState = false;
bool lastButton = HIGH;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
}

void loop() {

  bool currentButton = digitalRead(buttonPin);

  // Detect button press
  if (lastButton == HIGH && currentButton == LOW) {

    ledState = !ledState;

    digitalWrite(ledPin, ledState);

    delay(200); // debounce
  }

  lastButton = currentButton;
}