from time import sleep
from ADCDevice import ADS7830
from gpiozero import Button

z_pin = 18
button = Button(z_pin)
adc = ADS7830()

def loop():
    while True:
        val_z = not button.value
        val_y = adc.analogRead(0)
        val_x = adc.analogRead(1)
        print('X: %d, Y: %d, Z: %d'%(val_x, val_y, val_z))
        sleep(0.1)

def destroy():
    adc.close()
    button.close()

if __name__ == '__main__':
    try:
        print('Starting...')
        loop()
    except KeyboardInterrupt:
        destroy()
        print('Ending.')

