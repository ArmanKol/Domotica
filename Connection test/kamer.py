import socket, time


while 1:
    try:
        s = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("localhost", 80))
    except ConnectionRefusedError:
        print('Geen verbinding met centrale')
        time.sleep(10)
        continue

    while 1:
        try:
            message = s.recv(2).decode()
        except ConnectionResetError:
            print('Verbinding verbroken')
            s.shutdown(socket.SHUT_RDWR)
            s.close()
            break
        print(message + ' ontvangen')
        if message == 'KA':
            s.send(b'OK')
            continue
        elif message == '':
            s.shutdown(socket.SHUT_RDWR)
            s.close()
            break


    print('Verbinding was gesloten')
    print('Bezig nieuwe verbinding te maken...')
    time.sleep(30)