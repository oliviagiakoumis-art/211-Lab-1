from utils.brick import reset_brick, wait_ready_sensors, Motor, time, EV3ultrasonicsensor

# Initialize sensors and motors (Update ports 'A' and 'D' to match your build)
us_sensor = EV3ultrasonicsensor()
left_motor = Motor("A")
right_motor = Motor("D")

# Lab 1 Bang-Bang Parameters
BAND_CENTER = 20  # Target distance in cm
BAND_WIDTH = 3    # Acceptable tolerance in cm[cite: 1]
BASE_SPEED = 200  # Nominal driving speed (Degrees Per Second)

LOWER_THRESHOLD = BAND_CENTER - BAND_WIDTH  # 17 cm
UPPER_THRESHOLD = BAND_CENTER + BAND_WIDTH  # 23 cm

if __name__ == "__main__":
    wait_ready_sensors()
    
    try:
        print("Running Bang-Bang Controller...")
        while True:
            distance = us_sensor.get_cm()
            
            if distance is not None:
                print(f"Distance: {distance} cm")
                
                if distance < LOWER_THRESHOLD:
                    # Too close to the wall: steer away (slow inner wheel, fast outer wheel)
                    left_motor.set_dps(120)
                    right_motor.set_dps(250)
                elif distance > UPPER_THRESHOLD:
                    # Too far from the wall: steer towards (fast inner wheel, slow outer wheel)
                    left_motor.set_dps(250)
                    right_motor.set_dps(120)
                else:
                    # Within the band width: drive straight
                    left_motor.set_dps(BASE_SPEED)
                    right_motor.set_dps(BASE_SPEED)
                
                left_motor.start()
                right_motor.start()
                
            time.sleep(0.05)
            
    except BaseException:
        reset_brick()
        exit()