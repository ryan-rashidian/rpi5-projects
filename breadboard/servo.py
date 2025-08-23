from gpiozero import AngularServo
from time import sleep

GP_PIN = 18
SERVO_DELAY = 0.001
CORRECTION = 0.0

max_pw = (2.5+CORRECTION)/1000
min_pw = (0.5-CORRECTION)/1000
servo = AngularServo(
    GP_PIN,
    initial_angle=0,
    min_angle=0,
    max_angle=180,
    min_pulse_width=min_pw,
    max_pulse_width=max_pw
)

def loop():
    while True:
        for angle in range(0, 181, 1):
            servo.angle = angle
            sleep(SERVO_DELAY)
        sleep(0.5)
        for angle in range(180, -1, -1):
            servo.angle = angle
            sleep(SERVO_DELAY)
        sleep(0.5)

if __name__ == '__main__':
    try:
        print('Starting Program.')
        loop()
    except KeyboardInterrupt:
        print('Ending Program.')
