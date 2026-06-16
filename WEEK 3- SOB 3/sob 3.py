'''
#SOB 3 submitted on 08.05.2026

# Sequential Programming: Traffic Light Controller
# ================================================
# This program steps through traffic light states one by one,
# waiting a fixed time at each step before moving to the next.

import time

def run_traffic_light():
    print('Traffic light starting...')

    # STATE MACHINE NOTE: In a state machine this would be the RED state.
    # The machine would remain in RED until a timer event triggers a
    # transition to the GREEN state.
    print('RED   - Stop')
    time.sleep(5)

    # STATE MACHINE NOTE: This would be the GREEN state.
    # Entry: vehicles may proceed.
    # Transition trigger: timer expires -> move to YELLOW state.
    print('GREEN - Go')
    time.sleep(4)

    # STATE MACHINE NOTE: This would be the YELLOW state.
    # Entry: warn drivers to slow down.
    # Transition trigger: timer expires -> move back to RED state.
    print('YELLOW - Slow down')
    time.sleep(2)

    print('Cycle complete.')

# Run a single cycle (sequential: fixed order, top-to-bottom execution)
run_traffic_light()

'''

'''

# Finite State Machine: Traffic Light Controller
# ==============================================
# This program uses states and transitions to control
# the traffic light system continuously.

import time

# Define initial state
state = "RED"

def run_traffic_light ():
    global state
    print("Traffic light starting...")

    while True:  # FSM runs continuously
        if state == "RED":
            print("RED - Stop")
            time.sleep(5)

            # Transition: RED -> GREEN
            state = "GREEN"

        elif state == "GREEN":
            print("GREEN - Go")
            time.sleep(4)

            # Transition: GREEN -> YELLOW
            state = "YELLOW"

        elif state == "YELLOW":
            print("YELLOW - Slow down")
            time.sleep(2)

            # Transition: YELLOW -> RED
            state = "RED"

# Run FSM
run_traffic_light_fsm()

'''



#Sob 3 submitted on 15.05.2026

# Smart Irrigation Monitoring System
# ==================================
# This program simulates an automatic irrigation system
# using soil moisture, rain conditions and time checks.

# -----------------------------
# CONSTANTS
# -----------------------------

MOISTURE_THRESHOLD = 70
MAX_WATERING_MINUTES = 5
MOISTURE_GAIN_PER_MINUTE = 10

HEAT_START = 12
HEAT_END = 15

# -----------------------------
# SENSOR READINGS
# -----------------------------
# Each reading contains:
# soil moisture (%), raining status, current hour

sensor_readings = [
    {"moisture": 45, "rain": False, "hour": 9},
    {"moisture": 80, "rain": False, "hour": 10},
    {"moisture": 40, "rain": True, "hour": 11},
    {"moisture": 35, "rain": False, "hour": 13},
    {"moisture": 50, "rain": False, "hour": 17}
]

# -----------------------------
# FUNCTION: WATERING CYCLE
# -----------------------------

def simulate_watering_cycle(current_moisture):

    watering_minutes = 0

    while (
        current_moisture < MOISTURE_THRESHOLD
        and watering_minutes < MAX_WATERING_MINUTES
    ):

        print("Watering plants...")

        current_moisture += MOISTURE_GAIN_PER_MINUTE
        watering_minutes += 1

        print(f"Moisture Level: {current_moisture}%")

    print("Watering stopped.\n")

    return watering_minutes, current_moisture


# -----------------------------
# FUNCTION: EVALUATE READING
# -----------------------------

def evaluate_reading(reading):

    moisture = reading["moisture"]
    raining = reading["rain"]
    current_hour = reading["hour"]

    print("--------------------------------")
    print(f"Moisture: {moisture}%")
    print(f"Rain detected: {raining}")
    print(f"Hour: {current_hour}")

    # Condition 1:
    # Soil already moist enough
    if moisture >= MOISTURE_THRESHOLD:
        print("Soil moisture sufficient.")
        print("No watering needed.\n")
        return 0

    # Condition 2:
    # Rain detected
    elif raining:
        print("Rain detected.")
        print("Watering skipped.\n")
        return 0

    # Condition 3:
    # Avoid watering during hot hours
    elif HEAT_START <= current_hour <= HEAT_END:
        print("Heat restriction period.")
        print("Watering delayed.\n")
        return 0

    # Otherwise:
    # Start watering
    else:
        print("Conditions suitable.")
        print("Starting irrigation...\n")

        minutes_used, final_moisture = simulate_watering_cycle(
            moisture
        )

        return minutes_used


# -----------------------------
# MAIN PROGRAM
# -----------------------------

def run_irrigation_system():

    total_minutes = 0
    total_readings = len(sensor_readings)

    print("SMART IRRIGATION SYSTEM")
    print("=======================\n")

    # FOR LOOP:
    # Process every sensor reading
    for reading in sensor_readings:

        minutes = evaluate_reading(reading)

        total_minutes += minutes

    # SUMMARY
    print("SYSTEM SUMMARY")
    print("=======================")
    print(f"Total readings processed: {total_readings}")
    print(f"Total watering minutes: {total_minutes}")


# Run the system
run_irrigation_system()
