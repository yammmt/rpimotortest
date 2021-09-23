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

print("degree: ", end="")
move_deg = float(input())
while move_deg >= 0.0:
    required_step_num = round(move_deg / DEG_PER_ONE_STEP)
    print("  step: ", required_step_num)
    for _ in range(required_step_num):
        GPIO.output(GPIO_PINS[(next_hi-1+GPIO_LEN) % GPIO_LEN], False)
        GPIO.output(GPIO_PINS[next_hi], True)
        next_hi = (next_hi + 1) % GPIO_LEN
        time.sleep(SLEEP_SEC_BETWEEN_STEPS)

    print("degree: ", end="")
    move_deg = float(input())

GPIO.cleanup()
