import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 8090))
sk.listen()

conn, addr = sk.accept()
conn.send(b"dir")
ret = conn.recv(1024).decode("gbk")
print(ret)

conn.close()
sk.close()
