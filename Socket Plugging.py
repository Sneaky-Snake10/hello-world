import socket
from datetime import datetime

PORT = int(input('Port to block: '))
EXIT = input('Enter IP of exit connection')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), PORT))
now = datetime.now()
print(f'Beginning socket plugging at {now} on port {PORT}')

while True:
    try:
        sock.listen()
        connected, address = sock.accept()
        if address[1] == EXIT:
            print(f'{EXIT} connected, socket plugging stopped.')
            break
        connected.close()
        HOST = address[0]
        PORT = address[1]
        now = datetime.now()
        print(f'Blocked connection from {HOST}:{PORT} at {now}')

    except Exception as Problem:
        print(f'Exception raised at {now}. {Problem}')

now = datetime.now()
print(f'Terminated socket plugging at {now} on port {PORT}')
sock.close()
    
