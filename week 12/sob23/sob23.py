import serial
import csv
import time
from datetime import datetime

# Replace COM3 with your Arduino port if needed
ser = serial.Serial('COM3', 9600)

# Wait for Arduino to reset
time.sleep(2)

filename = "sensor_data.csv"

with open(filename, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Timestamp", "LDR", "Distance"])

    print("Receiving data...")

    while True:

        try:

            data = ser.readline().decode().strip()

            if not data:
                continue

            print("Received:", data)

            values = data.split(",")

            if len(values) != 2:
                continue

            ldr = int(values[0])
            distance = float(values[1])

            timestamp = datetime.now()

            writer.writerow([
                timestamp,
                ldr,
                distance
            ])

            file.flush()

            print(
                f"Time: {timestamp}"
            )

            print(
                f"LDR Value: {ldr}"
            )

            print(
                f"Distance: {distance:.2f} cm"
            )

            print("----------------------")

        except Exception as e:
            print("Error:", e)