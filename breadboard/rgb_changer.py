from time import sleep
from ADCDevice import ADCDevice, ADS7830
from gpiozero import RGBLED

led = RGBLED(red=22, green=27, blue=17, active_high=False)
adc = ADCDevice()
ADC_MAX = 255.0 # 8-bit ADC: 0-255

def loop():
    while True:
        adc = ADS7830()
        value_red = adc.analogRead(0)
        value_green = adc.analogRead(1)
        value_blue = adc.analogRead(2)
        led.red = value_red / ADC_MAX
        led.green = value_green / ADC_MAX
        led.blue = value_blue / ADC_MAX
        #print(
        #    'ADC Value : red = %d, green = %d, blue = %d' 
        #    %(value_red, value_green, value_blue)
        #)
        sleep(0.1)

def end_prog():
    led.close()
    adc.close()

if __name__ == '__main__':
    print('Starting...')
    try:
        loop()
    except KeyboardInterrupt:
        end_prog()
