#adding to github- steps:
'''
go into terminal:

git init

git add file1.py

git add file2.py
git commit -m "Initial commit"

git branch -M main
git remote add origin https://github.com/your-username/your-repo-name.git

git push -u origin main --> for the first time only,,after that : git push


--> for me: git remote add origin https://github.com/oliviagiakoumis-art/211-Lab-1.git

'''




from utils.brick import reset_brick, wait_ready_sensors, Motor, time, EV3ultrasonicsensor

# Initialize sensors and motors (Update ports 'A' and 'D' to match your build)
us_sensor = EV3ultrasonicsensor()
left_motor = Motor("A")
right_motor = Motor("D")

# Lab 1 P-Type Parameters
BAND_CENTER = 20  # Target distance in cm[cite: 1]
BASE_SPEED = 200  # Nominal driving speed
KP = 6.0          # Proportional gain constant (tune this value in lab)

if __name__ == "__main__":
    wait_ready_sensors()
    
    try:
        print("Running P-Type Controller...")
        while True:
            distance = us_sensor.get_cm()
            
            if distance is not None:
                # Calculate error
                error = distance - BAND_CENTER
                
                # Proportional correction magnitude
                correction = int(KP * abs(error))
                
                # Cap the maximum correction to prevent motor saturation
                if correction > 150:
                    correction = 150
                
                if error < 0:
                    # Too close: scale wheel speeds to steer away smoothly
                    left_motor.set_dps(max(50, BASE_SPEED - correction))
                    right_motor.set_dps(BASE_SPEED + correction)
                elif error > 0:
                    # Too far: scale wheel speeds to steer towards smoothly
                    left_motor.set_dps(BASE_SPEED + correction)
                    right_motor.set_dps(max(50, BASE_SPEED - correction))
                else:
                    # Exactly at band center
                    left_motor.set_dps(BASE_SPEED)
                    right_motor.set_dps(BASE_SPEED)
                
                left_motor.start()
                right_motor.start()
                
            time.sleep(0.05)
            
    except BaseException:
        reset_brick()
        exit()