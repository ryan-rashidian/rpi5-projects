from time import sleep
from ADCDevice import ADCDevice, ADS7830
from gpiozero import PWMLED

led = PWMLED(17, frequency=1000)
adc = ADCDevice()
ADC_MAX = 255.0 # 8-bit ADC: 0-255

def loop():
    while True:
        adc = ADS7830()
        value = adc.analogRead(0)
        led.value = value / ADC_MAX
        voltage = (value / ADC_MAX) * 3.3 # 3.3V pin
        print('ADC Value : %d, Voltage : %.2f' %(value, voltage))
        sleep(0.1)

def end_prog():
    adc.close()

if __name__ == '__main__':
    print('Starting...')
    try:
        loop()
    except KeyboardInterrupt:
        end_prog()
