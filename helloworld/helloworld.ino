// Arduino Serial Example
// Open Serial Monitor (Tools/Serial Monitor)
// github.com/pigetArduino/helloworld

// the setup function runs once when you press reset or power the board
void setup() {
  Serial.begin(9600); //Start serial communication at 9600
}

// the loop function runs over and over again forever
void loop() {
  Serial.println("Hello World"); //Print hello World
  delay(2000); //Wait 2 seconds
}
