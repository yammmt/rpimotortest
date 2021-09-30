# Move motor to a user inputted angle (degree)
# For example:
#     degree: 90
#       step:  50
#       now:  90.0
#     degree: 270
#       step:  100
#       now:  270.0
#     degree: 180
#       step:  50
#       now:  180.0 # => CCW
#     degree: 360
#       step:  100
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
    move_deg %= 360.0
    deg_diff_cw = move_deg - cur_deg
    if deg_diff_cw < 0.0:
        deg_diff_cw += 360.0
    deg_diff_ccw = 360.0 - deg_diff_cw
    deg_diff = min(deg_diff_cw, deg_diff_ccw)
    is_cw = deg_diff_cw <= deg_diff_ccw

    required_step_num = round(deg_diff / DEG_PER_ONE_STEP)
    print("  step: ", required_step_num)
    if is_cw:
        for _ in range(required_step_num):
            GPIO.output(GPIO_PINS[(next_hi-1+GPIO_LEN) % GPIO_LEN], False)
            GPIO.output(GPIO_PINS[next_hi], True)
            next_hi = (next_hi + 1) % GPIO_LEN
            time.sleep(SLEEP_SEC_BETWEEN_STEPS)
    else:
        for _ in range(required_step_num):
            GPIO.output(GPIO_PINS[(next_hi+1) % GPIO_LEN], False)
            GPIO.output(GPIO_PINS[next_hi], True)
            next_hi = (next_hi + GPIO_LEN - 1) % GPIO_LEN
            time.sleep(SLEEP_SEC_BETWEEN_STEPS)

    moved_deg_sum = required_step_num * DEG_PER_ONE_STEP
    if not is_cw:
        moved_deg_sum *= -1.0
    cur_deg = (cur_deg + moved_deg_sum + 360.0) % 360.0
    print("  now: ", cur_deg)

    print("degree: ", end="")
    move_deg = float(input())

GPIO.cleanup()
