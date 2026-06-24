/*
 * SerialReceive sketch
 *Blink the LED at a rate proportional to the received digit value
*/
int blinkDelay = 0; // blink delay stored in this variable
void setup()
{
  Serial.begin(9600); // Initialize serial port to send and receive at 9600 baud
  pinMode(LED_BUILTIN, OUTPUT); // set this pin as output //constant variable name for ledbuiltin
}
void loop()
{
  if (Serial.available()) // Check to see if at least one character is available
  {
  
    int ch = Serial.read(); // Reads the input (e.g., character '7' is read as ASCII 55)

if (isDigit(ch)) 
{
  // SUBTRACTION: This converts the ASCII code (55) into the math integer (7)
  int trueInteger = ch - '0'; 

  // Print both values to see the subtraction result
  Serial.print("ASCII code received: ");
  Serial.print(ch);                 // Prints 55
  Serial.print(" -> Subtracted Integer: ");
  Serial.println(trueInteger);     // Prints 7

  // Apply your blink delay formula using the true integer
  blinkDelay = trueInteger * 100;  // 7 * 100 = 700 ms
}

  }

  blink();  //using compiler here. the next function is used in order to read the function blink
}
// blink the LED with the on and off times determined by blinkDelay
void blink() //function
{
  digitalWrite(LED_BUILTIN, HIGH);
  delay(blinkDelay); // delay depends on blinkDelay value
  digitalWrite(LED_BUILTIN, LOW);
  delay (blinkDelay);
}