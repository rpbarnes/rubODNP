import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#serverAddress = ('134.147.66.2',7000) # address to the xepr computer
serverAddress = ('localhost',7000) # address to the xepr computer
sock.connect(serverAddress)
print sock.recv(1024)
sock.close()

