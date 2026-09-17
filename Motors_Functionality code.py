from utils.brick import reset_brick, wait_ready_sensors, Motor, time

# Initialize motor on port C (adjust port letter if needed, e.g., 'A', 'B', 'C', 'D')
motor = Motor("C")

if __name__ == "__main__":
    # Wait for sensors/motors to start up properly
    wait_ready_sensors()
    
    try:
        print("Starting motor encoder test...")
        
        # Get starting encoder position
        initial_encoder = motor.get_encoder()
        final_encoder = initial_encoder + 90
        
        # Set motor speed in degrees per second
        motor.set_dps(90)
        
        # Run until the target encoder count is reached
        while motor.get_encoder() < final_encoder:
            time.sleep(0.01)
            
        # Stop the motor once done
        motor.set_dps(0)
        print("Motor test completed successfully!")
        
    except BaseException:
        reset_brick()
        exit()