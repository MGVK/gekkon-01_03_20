from socket import *

host = '127.0.0.1'
port = 9999
addr = (host, port)

udp_socket = socket(AF_INET, SOCK_DGRAM)

udp_socket.sendto(b'hello', addr)
udp_socket.close()


