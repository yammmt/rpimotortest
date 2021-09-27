# Move motor to a user inputted angle (degree)
# For example:
#     degree: 90
#       step:  50
#       now:  90.0
#     degree: 130
#       step:  22
#       now:  129.6
#     degree: 270
#       step:  78
#       now:  270.0
#     degree: 360
#       step:  50
#       now:  0.0
#     degree: -1

import time
import RPi.GPIO as GPIO

GPIO_PINS = [17, 18, 27, 22]
GPIO_LEN = len(GPIO_PINS)
DEG_PER_ONE_STEP = 1.8
SLEEP_SEC_BETWEEN_STEPS = 0.01

# init
GPIO.setmode(GPIO.BCM)
for p in GPIO_PINS:
    GPIO.setup(p, GPIO.OUT)
    GPIO.output(p, False)
next_hi = 0

cur_deg = 0.0
print("degree: ", end="")
move_deg = float(input())
while move_deg >= 0.0:
    deg_diff = move_deg - cur_deg
    if deg_diff < 0.0:
        # always turn in clockwise
        deg_diff += 360.0

    required_step_num = round(deg_diff / DEG_PER_ONE_STEP)
    print("  step: ", required_step_num)
    for _ in range(required_step_num):
        GPIO.output(GPIO_PINS[(next_hi-1+GPIO_LEN) % GPIO_LEN], False)
        GPIO.output(GPIO_PINS[next_hi], True)
        next_hi = (next_hi + 1) % GPIO_LEN
        time.sleep(SLEEP_SEC_BETWEEN_STEPS)
    cur_deg = (cur_deg + required_step_num * DEG_PER_ONE_STEP) % 360.0
    print("  now: ", cur_deg)

    print("degree: ", end="")
    move_deg = float(input())

GPIO.cleanup()
