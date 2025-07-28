from time import sleep
from math import log
from ADCDevice import ADS7830

adc = ADS7830()
ADC_MAX = 255.0 # 8-bit ADC

def loop():
    while True:
        value = adc.analogRead(0)
        voltage = value / ADC_MAX * 3.3
        resistance = 10 * voltage / (3.3 - voltage)
        temp_k = 1 / (1 / (273.15 + 25) + log(resistance / 10) / 3950.0)
        temp_c = temp_k - 273.15
        print('ADC Value : %d, Voltage : %.2f, Temp : %.2f'%(value, voltage, temp_c))
        sleep(0.1)

def destroy():
    adc.close()

if __name__ == '__main__':
    try:
        print('Starting...')
        loop()
    except KeyboardInterrupt:
        destroy()
        print('Ending.')

