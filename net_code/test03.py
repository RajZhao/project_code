import socket
import subprocess

sk = socket.socket()
sk.connect(("127.0.0.1", 8090))

cmd = sk.recv(1024).decode("utf-8")
ret = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

sk.send()
