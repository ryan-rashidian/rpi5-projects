from time import sleep
from ADCDevice import ADS7830
from gpiozero import DigitalOutputDevice, PWMOutputDevice

motor_pin1 = DigitalOutputDevice(27)
motor_pin2 = DigitalOutputDevice(17)
enable_pin = PWMOutputDevice(22, frequency=1000)
adc = ADS7830()

def map_num(value, from_low, from_high, to_low, to_high):
    return (
        (to_high - to_low) 
        * (value - from_low) 
        / (from_high - from_low) 
        + to_low
    )

def motor(adc_value):
    value = adc_value - 128
    if (value > 0):
        motor_pin1.on()
        motor_pin2.off()
        print('Turn forward...')
    elif (value < 0):
        motor_pin1.off()
        motor_pin2.on()
        print('Turn backward...')
    else:
        motor_pin1.off()
        motor_pin2.off()
        print('Motor Stop.')

    b = map_num(abs(value),0,128,0,100)
    enable_pin.value = b / 100.0
    print('The PWM duty cycle is %d%%\n'%(abs(value) * 100 / 127))

def loop():
    while True:
        value = adc.analogRead(0)
        print('ADC Value : %d'%(value))
        motor(value)
        sleep(0.2)

def destroy():
    motor_pin1.close()
    motor_pin2.close()
    enable_pin.close()
    adc.close()

if __name__ == '__main__':
    try:
        print('Starting...')
        loop()
    except KeyboardInterrupt:
        destroy()
        print('Ending.')

