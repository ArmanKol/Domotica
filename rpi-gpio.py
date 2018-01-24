import RPi.GPIO as GPIO
import time


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(True)
    for buttonPin in buttonPins:
        GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print('GPIO PIN ' + str(buttonPin) + ' SETUP COMPLETED')
    print('SETUP GPIO COMPLETED...')


buttonPins = (5, 12, 23, 21)
setup()

while True:
    button1 = GPIO.input(5)
    button2 = GPIO.input(12)
    button3 = GPIO.input(23)
    button4 = GPIO.input(21)
    if button1 == False:
        print('BUTTON 1 PRESSED!')
        time.sleep(0.3)
    elif button2 == False:
        print('BUTTON 2 PRESSED!')
        time.sleep(0.3)
    elif button3 == False:
        print('BUTTON 3 PRESSED!')
        time.sleep(0.3)
    elif button4 == False:
        print('BUTTON 4 PRESSED!')
        time.sleep(0.3)