import serial
import time
import random

# Configure the serial port
ser = serial.Serial('COM6', 9600, timeout=1)

def send_distance(distance_cm):
    # Convert distance to string and encode it to bytes
    distance_str = str(distance_cm).encode('utf-8')
    # Write the bytes to the serial port
    ser.write(distance_str)
    # Wait for a short moment before sending the next value
    time.sleep(0.1)

try:
    while True:
        # Send distances from 100 to 500 centimeters (1 to 5 meters)
        for distance_cm in range(100, 501, 100):
            send_distance(distance_cm)
        
        # Generate and send some random distances within the range
        for _ in range(5):
            random_distance_cm = random.randint(100, 500)
            send_distance(random_distance_cm)
        
except KeyboardInterrupt:
    # Handle keyboard interrupt (Ctrl+C)
    print("Keyboard Interrupt. Closing serial connection.")
    ser.close()
