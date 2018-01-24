import socket, time, threading


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


    def sendMessage(self, message):
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

server = 'localhost'
port = 80

clientsocket = serverconnection(server, port)
keepAliveThread = threading.Thread(target=clientsocket.keepAlive)
keepAliveThread.start()

