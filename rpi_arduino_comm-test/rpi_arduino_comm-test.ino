void setup() {
  Serial.begin(115200);
}
void loop() {
  while (1) {
    if (Serial.available() > 0) {
      String data = Serial.readStringUntil('\n');
      Serial.print("You sent me: ");
      Serial.println(data);
      break;
    }
  }
  //elküldi ha befejezte a szállítást!
  Serial.println("finished");
}
