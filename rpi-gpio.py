import time, os, socket, threading
#import RPi.GPIO as GPIO


kamerid = 1
status = "1"
hardwareid = "4"


class serversocket:
    def __init__(self, server, port):
        while True:
            try:
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.connect((server, port))
                self.s.send(str(kamerid).encode())
            except ConnectionRefusedError:
                print('Geen verbinding met centrale')
                time.sleep(10)
                continue
            break

    def receiveMessage(self):
        return self.s.recv(2).decode()

    def sendMessage(self, hardwareID, status):
        message = '{0:>03}'.format(hardwareID) + ';' + str(status)
        try:
            self.s.send(message.encode())
        except:
            self.shutdown()

    def keepAlive(self):
        while True:
            self.sendMessage(0, 1)
            time.sleep(5)

    def shutdown(self):
        keepAliveThread._stop()
        self.s.shutdown(socket.SHUT_RDWR)
        self.s.close()


class hardwareButton:
    def __init__(self, hardwareID, gpioPin):
        self.hardwareID = hardwareID
        self.gpioPin = gpioPin
        self.state = 0


    def isButtonPressed(self):
        return #GPIO.input(self.gpioPin) == False


    def turnOn(self):
        self.state = 1
        self.updateCentrale()


    def turnOff(self):
        self.state = 0
        self.updateCentrale()


    def updateCentrale(self):
        serverconnection.sendMessage(self.hardwareID, self.state)


def setup():
    """"setup GPIO related things"""
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(True)
    #GPIO.cleanup()
    #for buttonPin in buttonPins:
    #    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #    print('GPIO.IN ' + str(buttonPin) + ' SETUP COMPLETED')
    #GPIO.setup(ledPin, GPIO.OUT)
    print('SETUP GPIO COMPLETED...')


def turnCameraOff():
    print('Motion already running...')
    print('Stopping motion...')
    command = 'sudo systemctl stop motion'
    os.system('echo %s|sudo -S %s' % ('raspberry', command))
    print('\nMotion stopped!')


def turnCameraOn():
    print('Starting motion...')
    command = 'sudo systemctl start motion'
    os.system('echo %s|sudo -S %s' % ('raspberry', command))
    print('\nMotion started!')


def checkCAMstatus():
    """"check status of motion daemon, return true/false"""
    motion = os.popen('pgrep motion')
    pid = motion.readline()
    motion.close()
    if pid:
        return True
    else:
        return False


# Setup all hardware Objects
cameraButton = hardwareButton(2, 21)
lightButton = hardwareButton(1, 23)
resetNoodButton = hardwareButton(4, 5)
noodButton = hardwareButton(4, 12)


# Global variables
ledOn = False
buttonPins = (5, 12, 23, 21)
ledPin = 20
# Run setup
setup()


# Socket variables
server = 'localhost'
port = 80
serverconnection = serversocket(server, port)

keepAliveThread = threading.Thread(target=serverconnection.keepAlive, daemon=True)
keepAliveThread.start()


while True:
    # Check if button has been pressed
    print('1 = Reset Noodknop/n2 = Noodknop/n3 = Lichtknop/n 4=Cameraknop/n/n)')
    button = eval(input(''))
    if button == 1 and noodButton.state:
        print('Resetknop is ingedrukt, EN de noodknop is ingedrukt op het moment!')
        print('Het noodalarm wordt gereset')

        """             ACTIES HIER             """

        time.sleep(0.3)
    elif button == 2:
        print('Noodknop is ingedrukt!!!')
        # if led is off it must be enabled
        if lightButton.state == False:
            """             ACTIES HIER             """

        # if camera is off it must me enabled
        if cameraButton.state == False:
            """             ACTIES HIER             """

        time.sleep(0.3)
    elif button == 3:
        print('Lichtknop is ingedrukt!')
        # switch led on/off according to its last state
        if lightButton.state:
            lightButton.turnOff()
        elif lightButton.state == False:
            lightButton.turnOn()

        # GPIO.output(lightButton.gpioPin, lightButton.state)
        time.sleep(0.3)
    elif button == 4:
        print('Cameraknop is ingedrukt!!')
        # switch camera on/off according to its last state
        if cameraButton.state:
            cameraButton.turnOff()
        if cameraButton.state == False:
            cameraButton.turnOn()

        camStatus = checkCAMstatus()
        # switchCAM(camStatus)
        time.sleep(0.3)

'''
    if resetNoodButton.isButtonPressed() and noodButton.state:
        print('Resetknop is ingedrukt, EN de noodknop is ingedrukt op het moment!')
        print('Het noodalarm wordt gereset')

        """             ACTIES HIER             """

        time.sleep(0.3)
    elif noodButton.isButtonPressed():
        print('Noodknop is ingedrukt!!!')
        # if led is off it must be enabled
        if lightButton.state == False:

            """             ACTIES HIER             """

        # if camera is off it must me enabled
        if cameraButton.state == False:

            """             ACTIES HIER             """

        time.sleep(0.3)
    elif lightButton.isButtonPressed():
        print('Lichtknop is ingedrukt!')
        # switch led on/off according to its last state
        if lightButton.state:
            lightButton.turnOff()
        elif lightButton.state == False:
            lightButton.turnOn()

        #GPIO.output(lightButton.gpioPin, lightButton.state)
        time.sleep(0.3)
    elif cameraButton.isButtonPressed():
        print('Cameraknop is ingedrukt!!')
        # switch camera on/off according to its last state
        if cameraButton.state:
            cameraButton.turnOff()
        if cameraButton.state == False:
            cameraButton.turnOn()

        camStatus = checkCAMstatus()
        #switchCAM(camStatus)
        time.sleep(0.3)
    '''
