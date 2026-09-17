from utils.brick import reset_brick, wait_ready_sensors, time, EV3UltrasonicSensor

# Initialize the ultrasonic sensor on port 1 (change port number if needed)
us_sensor = EV3UltrasonicSensor(1)

if __name__ == "__main__":
    # Wait for sensors to start up properly
    wait_ready_sensors()
    
    try:
        print("Starting ultrasonic sensor test. Press Ctrl+C to stop.")
        while True:
            distance = us_sensor.get_cm()
            print(f"Distance: {distance} cm")
            time.sleep(0.1) # Short delay between readings
            
    except BaseException:
        reset_brick()
        exit()