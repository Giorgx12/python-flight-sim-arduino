void setup() {
  Serial.begin(9600);
}

void loop() {
  int x = analogRead(A0);
  int y = analogRead(A1);
  int throttle = analogRead(A2);

  Serial.print(x); Serial.print(",");
  Serial.print(y); Serial.print(",");
  Serial.println(throttle);

  delay(50);
}

