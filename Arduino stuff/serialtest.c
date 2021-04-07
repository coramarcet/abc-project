void setup() {
  Serial.begin(9600);
}
void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    sleep(5);
    Serial.print("You sent me: ");
    Serial.println(data);
  }
}
