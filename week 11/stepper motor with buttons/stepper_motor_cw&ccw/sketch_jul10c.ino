#define BLYNK_TEMPLATE_ID "TMPL2ssMBXBF7"
#define BLYNK_TEMPLATE_NAME "uln driver"
#define BLYNK_AUTH_TOKEN "atFdCuYSHeXaqtLcyWKUK-4qhSZpGuXT"

#include <WiFiNINA.h>
#include <BlynkSimpleWiFiNINA.h>
#include <Stepper.h>

char ssid[] = "MDX Student";
char pass[] = "M!ddle$ex";

const int stepsPerRevolution = 2048;

Stepper motor(
  stepsPerRevolution,  2,  4,  3,  5);

BLYNK_WRITE(V0)
{
  if(param.asInt())
  {
    motor.step(512);   // clockwise
  }
}

BLYNK_WRITE(V1)
{
  if(param.asInt())
  {
    motor.step(-512);  // counter-clockwise
  }
}

void setup()
{
  motor.setSpeed(10);

  Serial.begin(115200);

  Blynk.begin(
    BLYNK_AUTH_TOKEN,
    ssid,
    pass
  );
}

void loop()
{
  Blynk.run();
}