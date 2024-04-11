import serial
import time
import requests

def establish_connection(serial_port, baud_rate):
    try:
        ser = serial.Serial(serial_port, baud_rate)
        print("Connected to Arduino successfully.")
        time.sleep(2)  # Wait for 2 seconds for stability
        ser.write(b'#')  # Send '#' to Arduino
        return ser
    except serial.SerialException:
        print("Failed to connect to Arduino. Retrying in 5 seconds...")
        time.sleep(5)
        return None

def read_data(ser):
    try:
        line = ser.readline().decode().strip()
        if line:
            return line
        else:
            print("No data received. Retrying...")
            return None
    except serial.SerialException:
        print("Connection with Arduino lost. Reconnecting...")
        return None

def send_to_server(data):
    url = 'http://127.0.0.1:5000/receive-data'  # Flask server endpoint
    payload = {'data': data}  # Adjust payload format according to Flask server's requirements
    try:
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            return False
        return True
    except requests.exceptions.RequestException as e:
        print("An error occurred while sending data to the server:", e)
        return False

def main():
    serial_port = 'COM6'  # Change this to match your Arduino's port
    baud_rate = 9600
    ser = None
    send_failed_count = 0

    try:
        while True:
            if ser is None:
                ser = establish_connection(serial_port, baud_rate)

            if ser is not None:
                data = read_data(ser)
                if data is not None:
                    print("Received:", data)
                    if not send_to_server(data):
                        send_failed_count += 1
    except KeyboardInterrupt:
        # Print the log before exiting
        print("\nExiting...")
        print(f"Server Transmission failed count: {send_failed_count}")

if __name__ == "__main__":
    main()
