import serial

ser = serial.Serial('COM3', 9600)

while True:
    data = ser.readline().decode().strip()

    values = data.split(",")

    if len(values) == 2:

        ldr_value = int(values[0])
        distance = float(values[1])

        print("LDR Value:", ldr_value)
        print("Distance:", distance, "cm")
        print("-------------------")