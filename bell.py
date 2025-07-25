from gpiozero import Buzzer, Button

from signal import pause


buzzer = Buzzer(17)
button = Button(18)

def button_press():
    buzzer.blink(on_time=1)

def button_release():
    buzzer.off()

def loop():
    button.when_activated = button_press
    button.when_deactivated = button_release
    pause()

def deactivate():
    buzzer.close()
    button.close()

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        deactivate()
