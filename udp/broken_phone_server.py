from socket import *

host = '127.0.0.1'
port = 9999
addr = (host, port)

udp_socket = socket(AF_INET, SOCK_DGRAM)

udp_socket.bind(addr)
data , addr = udp_socket.recvfrom(1024)
print(str(data))
udp_socket.close()


