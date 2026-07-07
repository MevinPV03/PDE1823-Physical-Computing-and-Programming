#include <SoftwareSerial.h>

SoftwareSerial HM10(10, 11); // RX, TX

void setup()
{
  pinMode(13, OUTPUT);
  pinMode(7, OUTPUT);

  Serial.begin(9600);
  HM10.begin(9600);

  Serial.println("HM10 Ready");
}

void loop()
{
  if (HM10.available())
  {
    String cmd = HM10.readStringUntil('\n');
    cmd.trim();

    Serial.print("Received: ");
    Serial.println(cmd);

    if(cmd == "LEDON")
    {
      digitalWrite(13, HIGH);
      digitalWrite(7, HIGH);

      HM10.println("LED ON");
    }

    else if(cmd == "LEDOFF")
    {
      digitalWrite(13, LOW);
      digitalWrite(7, LOW);

      HM10.println("LED OFF");
    }

    else if(cmd == "BLINK")
    {
      for(int i = 0; i < 5; i++)
      {
        digitalWrite(13, HIGH);
        digitalWrite(7, HIGH);
        delay(500);

        digitalWrite(13, LOW);
        digitalWrite(7, LOW);
        delay(500);
      }

      HM10.println("BLINK DONE");
    }
  }
}
