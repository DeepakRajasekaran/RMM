#define TRIGGER_PIN 5
#define ECHO_PIN 4

void setup() {
  Serial.begin(9600); // Serial monitor for debugging
  pinMode(TRIGGER_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  while (true) {
    if (Serial.available() > 0) {
      char receivedChar = Serial.read();
      if (receivedChar == '#'){
        Serial.println("Connected to Arduino Successfully");
        break;
      }
    }
    delay(10); // Wait for 10ms before checking again
  }
}

void loop() {
  // Measure distance using ultrasonic sensor
  int distance = readDistance();

  // Send distance data to Python script
  Serial.println(distance);

  delay(100); // Delay for stability
}

int readDistance() {
  long duration, distance;

  // Send ultrasonic pulse
  digitalWrite(TRIGGER_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIGGER_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGGER_PIN, LOW);

  // Read echo pulse
  duration = pulseIn(ECHO_PIN, HIGH);

  // Calculate distance
  distance = duration * 0.034 / 2; // Speed of sound in air is approximately 0.034 cm/µs

  return distance;
}
