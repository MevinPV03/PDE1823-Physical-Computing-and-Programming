#define BLYNK_TEMPLATE_ID "TMPL2L-I1fg_r"
#define BLYNK_TEMPLATE_NAME "MKR LED 1"
#define BLYNK_AUTH_TOKEN "Cjxd-Hidncix3ub5V0rOGSY15wJAFkTk"


#define BLYNK_PRINT Serial
#include <WiFiNINA.h>
#include <BlynkSimpleWiFiNINA.h>

// You should get Auth Token in the Blynk App-
char auth[] = "Cjxd-Hidncix3ub5V0rOGSY15wJAFkTk";

// Your WiFi credentials.
char ssid[] = "MDX Student";
char pass[] = "M!ddle$ex";

void setup ()
{
 Serial.begin (9600);
 Blynk.begin(auth, ssid, pass);
}

void loop ()
{
 Blynk.run();
}
BLYNK_WRITE(V0) //read a value from cloud
{
int value = param.asInt(); // Get value as integer
analogWrite(6, value); //INBUILTLED
Serial.println(value);
}