from time import sleep
from ADCDevice import ADCDevice, ADS7830
from gpiozero import PWMLED

led_pin = 17
led = PWMLED(led_pin)
adc = ADCDevice()
ADC_MAX = 255.0 # 8-bit ADC: 0-255

def clamp(x) -> float:
    """Ensure value between 0 and 1"""
    return max(0, min(1, x))

def loop():
    while True:
        adc = ADS7830()
        value = adc.analogRead(0)
        # Photoresistor digital readings range from approximately 100-140
        # value - 100 reduces range to approximately 0-40
        # / 40 range maximum
        # clamp() to ensure 0 and 1 min and max
        led.value = clamp((value - 100) / 40)
        voltage = (value / ADC_MAX) * 3.3
        print('ADC Value: %d, Voltage: %.2f' %(value, voltage))
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
