import serial
import time
import matplotlib.pyplot as plt

ser = serial.Serial('COM3', 9600)
time.sleep(2)

ldr_values = []
distance_values = []
reading_numbers = []

plt.ion()

count = 0

while True:
    try:
        data = ser.readline().decode().strip()

        values = data.split(",")

        if len(values) == 2:

            ldr = int(values[0])
            distance = float(values[1])

            count += 1

            reading_numbers.append(count)
            ldr_values.append(ldr)
            distance_values.append(distance)

            plt.clf()

            plt.plot(reading_numbers,
                     ldr_values,
                     label="LDR")

            plt.plot(reading_numbers,
                     distance_values,
                     label="Distance")

            plt.xlabel("Reading Number")
            plt.ylabel("Sensor Value")
            plt.title("Live Sensor Data")

            plt.legend()

            plt.pause(0.1)

    except Exception as e:
        print("Error:", e)