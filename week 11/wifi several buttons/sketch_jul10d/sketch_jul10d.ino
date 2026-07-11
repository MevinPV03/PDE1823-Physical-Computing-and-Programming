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

int motorSpeed = 10;

void setup()
{
  Serial.begin(115200);

  motor.setSpeed(motorSpeed);

  Blynk.begin(
    BLYNK_AUTH_TOKEN,    ssid,    pass  );

  Serial.println("Connected");
}

BLYNK_WRITE(V0)
{
  if(param.asInt())
  {
    motor.step(100);
  }
}

BLYNK_WRITE(V1)
{
  if(param.asInt())
  {
    motor.step(-100);
  }
}

BLYNK_WRITE(V2)
{
  if(param.asInt())
  {
    motor.step(512);
  }
}

BLYNK_WRITE(V3)
{
  if(param.asInt())
  {
    motor.step(1024);
  }
}

BLYNK_WRITE(V4)
{
  if(param.asInt())
  {
    motor.step(2048);
  }
}

BLYNK_WRITE(V5)
 {
  motorSpeed = param.asInt();

  motor.setSpeed(motorSpeed);

  Serial.print("Speed = ");
  Serial.println(motorSpeed);
 }




void loop()
{
  Blynk.run();
}