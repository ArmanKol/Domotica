import RPi.GPIO as GPIO
import time
import os
import socket
import threading

kamerid = "1"
noodknoopstatus = "1"
hardwareid = "4"


class serverconnection:
    def __init__(self, server, port):
        while True:
            try:
                self.s = socket.socket(
                    socket.AF_INET, socket.SOCK_STREAM)
                self.s.connect((server, port))
            except ConnectionRefusedError:
                print('Geen verbinding met centrale')
                time.sleep(10)
                continue
            break

    def receiveMessage(self):
        return self.s.recv(2).decode()

    def sendMessage(self, hardwareID, status):
        message = '{0:>02}'.format(kamerid) + ';' + '{0:>03}'.format(str(hardwareID)) + ';' + str(status)
        self.s.send(message.encode())

    def keepAlive(self):
        while True:
            try:
                self.sendMessage('OK')
                time.sleep(5)
            except:
                self.shutdown()

    def shutdown(self):
        keepAliveThread._stop()
        self.s.shutdown(socket.SHUT_RDWR)
        self.s.close()

    def keepAlive(self):
        while True:
            try:
                self.sendMessage('OK')
                time.sleep(5)
            except:
                self.shutdown()

    def shutdown(self):
        keepAliveThread._stop()
        self.s.shutdown(socket.SHUT_RDWR)
        self.s.close()


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(True)
    GPIO.cleanup()
    for buttonPin in buttonPins:
        GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print('GPIO.IN ' + str(buttonPin) + ' SETUP COMPLETED')
    GPIO.setup(ledPin, GPIO.OUT)
    print('SETUP GPIO COMPLETED...')


buttonPins = (5, 12, 23, 21)
ledPin = 20
ledOn = False
setup()

server = 'localhost'
port = 80

clientsocket = serverconnection(server, port)

keepAliveThread = threading.Thread(target=clientsocket.keepAlive)
keepAliveThread.start()

while True:
    button1 = GPIO.input(5)
    button2 = GPIO.input(12)
    button3 = GPIO.input(23)
    button4 = GPIO.input(21)
    if button1 == False:
        print('BUTTON 1 PRESSED!')
        clientsocket.sendMessage(hardwareid)
        time.sleep(0.3)
    elif button2 == False:
        print('BUTTON 2 PRESSED!')
        clientsocket.sendMessage(noodknoopstatus)
        time.sleep(0.3)
    elif button3 == False:
        print('BUTTON 3 PRESSED!')
        if ledOn == False:
            GPIO.output(ledPin, 1)
            ledOn = True
            print('LAMP AAN!')
        else:
            GPIO.output(ledPin, 0)
            ledOn = False
            print('LAMP UIT!')
        time.sleep(0.3)
    elif button4 == False:
        print('BUTTON 4 PRESSED!')
        print('Checking if Motion is running...')
        motion = os.popen('pgrep motion')
        pid = motion.readline()
        motion.close()
        sudoPass = 'raspberry'
        if pid:
            print('Motion already running...')
            print('Stopping motion...')
            command = 'sudo systemctl stop motion'
            os.system('echo %s|sudo -S %s' % (sudoPass, command))
            print('\nMotion stopped!')
        else:
            print('Starting motion...')
            command = 'sudo systemctl start motion'
            os.system('echo %s|sudo -S %s' % (sudoPass, command))
            print('\nMotion started!')
        time.sleep(0.3)
