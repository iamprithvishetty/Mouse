int pushPin = 6;         // potentiometer wiper (middle terminal) connected to analog pin 3
int xPin = 0;
int yPin = 1;
      // outside leads to ground and +5V
int valPush = HIGH;     // variable to store the value read
int valX = 0;
int valY = 0;
void setup()
{
  pinMode(pushPin,INPUT);
  Serial.begin(115200);         //  setup serial
  digitalWrite(pushPin,HIGH);
}

void loop()
{
  valX = analogRead(xPin);    // read the x input pin
  valY = analogRead(yPin);    // read the y input pin
  valPush = digitalRead(pushPin); // read the push button input pin
  Serial.println(String(valX)+"-"+String(valY)+"-"+String(valPush));
  delay(15);
 }
  
