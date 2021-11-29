import socket
# import sys
from binascii import hexlify

HOST, PORT = "localhost", 9999
# data = " ".join(sys.argv[1:])
MSJ = 0x00AA
data = bytearray(MSJ.to_bytes(4, 'big'))


# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    # sock.sendall(bytes(data + "\n", "utf-8"))
    sock.sendall(data)

    # Receive data from the server and shut down
    # received = str(sock.recv(1024), "utf-8")
    received = sock.recvfrom(1024)
    print("Lo enviado: ", hexlify(data).decode("utf-8"))
    print("Lo recibido: ", hexlify(received[0]).decode("utf-8"))

# print("Sent:     {}".format(data))
# print("Received: {}".format(received))
