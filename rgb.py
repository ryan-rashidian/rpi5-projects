from gpiozero import RGBLED

from time import sleep

import random

led = RGBLED(red=17, green=18, blue=27, active_high=False, initial_value=[0])

def set_color(r_val, g_val, b_val):
    led.red = r_val / 100
    led.green = g_val / 100
    led.blue = b_val / 100

def loop():
    while True:
        r = random.randint(0, 100)
        g = random.randint(0, 100)
        b = random.randint(0, 100)
        set_color(r, g, b)

        for val in range(0, 100, 1):
            val = val / 100
            led.value = [val]
            sleep(0.01)
        for val in range(100, -1, -1):
            val = val / 100
            led.value = [val]
            sleep(0.01)

def end_prog():
    led.close()

if __name__ == '__main__':
    print('Running...')
    try:
        loop()
    except KeyboardInterrupt:
        end_prog()
