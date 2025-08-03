from gpiozero import LED, Button
import time

led = LED(17)
button = Button(18)
button.hold_time = 1

def main():
    while True:
        if button.is_active:
            led.toggle()
            if led.is_active:
                print("On")
            else:
                print("Off")
            time.sleep(0.25)

if __name__ == '__main__':
    print("Program starting...")
    try:
        main()
    except KeyboardInterrupt:
        print("Ending Program.")
