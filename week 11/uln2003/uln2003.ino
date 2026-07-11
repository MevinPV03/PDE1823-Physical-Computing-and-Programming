#include <Stepper.h>

const int stepsPerRevolution = 2048;

Stepper myStepper(
  stepsPerRevolution,  8,  10,  9,  11);

void setup()
{
  myStepper.setSpeed(10);
}

void loop()
{
  // Clockwise
  myStepper.step(2048);
  delay(3000);

  // Anti-clockwise
  myStepper.step(-2048);
  delay(3000);
}