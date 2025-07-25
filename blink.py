from gpiozero import PWMLED
from time import sleep

led = PWMLED(18, initial_value=0, frequency=1000)

def loop():
    while True:
        for b in range(0, 101, 1):
            led.value = b / 100.0
            sleep(0.01)
        sleep(1)
        for b in range(100, -1, -1):
            led.value = b / 100.0
            sleep(0.01)
        sleep(1)

def destroy():
    led.close()

if __name__ == '__main__':
    print('Starting Program...')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        print('Ending Program.')

