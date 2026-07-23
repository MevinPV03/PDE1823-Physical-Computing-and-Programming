import serial
import time
import BlynkLib



# ==========================
# BLYNK SETTINGS
# ==========================

BLYNK_AUTH = "8vzmltlOq-o05F_6vabRQtKM8oL_Ivf0"


blynk = BlynkLib.Blynk(BLYNK_AUTH)



# ==========================
# ARDUINO CONNECTION
# ==========================

arduino = serial.Serial(
    port="COM3",       # Change this if needed
    baudrate=9600,
    timeout=1
)


time.sleep(2)


print("Arduino Connected")
print("Blynk Connected")



# ==========================
# MAIN LOOP
# ==========================

while True:


    # Keep Blynk alive
    blynk.run()



    if arduino.in_waiting > 0:


        try:

            # Read Arduino data

            data = arduino.readline().decode().strip()



            if data:


                print("Received:", data)



                # Arduino format:
                # 500,25.4


                values = data.split(",")



                if len(values) == 2:


                    ldr_value = int(values[0])


                    distance_value = float(values[1])



                    print(
                        "Light:",
                        ldr_value
                    )


                    print(
                        "Distance:",
                        distance_value,
                        "cm"
                    )



                    # ======================
                    # SEND TO BLYNK
                    # ======================


                    # LDR → V0

                    blynk.virtual_write(
                        0,
                        ldr_value
                    )



                    # Distance → V1

                    blynk.virtual_write(
                        1,
                        distance_value
                    )



        except Exception as error:

            print(
                "Error:",
                error
            )



    # Fast refresh
    time.sleep(0.1)