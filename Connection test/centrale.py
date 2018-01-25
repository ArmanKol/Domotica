import socket, threading, time, psycopg2

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

class kamer:
    def __init__(self, kamerid):
        self.kamerid = kamerid
        cur.execute('''SELECT voornaam, tussenvoegsel, achternaam FROM persoon WHERE persoonsid = (SELECT persoonsid FROM kamer WHERE kamerid = %s)''', (self.kamerid,))
        self.bewoner = cur.fetchall()[0]


def acceptIncomingConnections():
    while 1:
        (clientsocket, address) = serversocket.accept()
        ct = client_thread(clientsocket)
        ct.run()


conn = psycopg2.connect("dbname='idp_domotica' user='idpgroep' host='37.97.193.131' password='S67asbiMQA'")
cur = conn.cursor()

cur.execute('''SELECT kamerid FROM kamer''')
kamers = dict()
for kmr in cur.fetchall():
    kamers[kmr[0]] = kamer(kmr[0])

for kmr in kamers:
    print(kamers[kmr].bewoner)

'''
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', 80))
serversocket.listen(5)

incomingConnectionsThread = threading.Thread(target=acceptIncomingConnections)
incomingConnectionsThread.start()
'''