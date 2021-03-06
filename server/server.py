import socket
from _thread import *
import sys

server = "172.20.21.196"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)
    print(str(e))

s.listen(2)
print("Waiting for connection, server started")

def threaded_client(conn):
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)
            
            conn.sendall(str.encode(reply))
        except error as e:
            print(e)
            break
    print("Lost Connection")
    conn.close()
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))

