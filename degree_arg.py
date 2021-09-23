import time
import RPi.GPIO as GPIO

from RpiMotorLib import RpiMotorLib

GPIO_PINS = [17, 18, 27, 22]
FULL_DEG_ONE_STEP = 1.8

mymotor = RpiMotorLib.BYJMotor("mymotor", "Nema")
time.sleep(0.5)

print("degree: ", end="")
move_deg = float(input())

while move_deg >= 0.0:
    full_step_num = move_deg / FULL_DEG_ONE_STEP // 4
    print("full step x ", full_step_num)

    mymotor.motor_run(GPIO_PINS, 0.1, full_step_num, False, False, "full", .05)

    print("degree: ", end="")
    move_deg = float(input())

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
