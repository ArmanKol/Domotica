import socket, threading, time

class client_thread(threading.Thread):
    def __init__(self, clientsocket):
        super().__init__()
        self.clientsocket = clientsocket

    def run(self):
        while 1:
            time.sleep(2)
            try:
                self.clientsocket.send(b'KA')
                message = self.clientsocket.recv(2).decode()
            except ConnectionResetError:
                self.clientsocket.close()
                break
            if message == 'OK':
                continue
        self._stop()


serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', 80))
serversocket.listen(5)

while 1:
    (clientsocket, address) = serversocket.accept()
    ct = client_thread(clientsocket)
    ct.run()





