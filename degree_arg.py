import time
import RPi.GPIO as GPIO

from RpiMotorLib import RpiMotorLib

GPIO_PINS = [17, 18, 27, 22]
MOVE_DEG = 90.0
FULL_DEG_ONE_STEP = 1.8

mymotor = RpiMotorLib.BYJMotor("mymotor", "Nema")
time.sleep(0.5)

full_step_num = MOVE_DEG / FULL_DEG_ONE_STEP // 4
print("full step x ", full_step_num)

mymotor.motor_run(GPIO_PINS, 0.1, full_step_num, False, False, "full", .05)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
