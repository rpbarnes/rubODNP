import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('134.147.66.2',7000))
sock.listen(5)
while True:
    conn,addr = sock.accept()
    print 'Got connection from ', addr
    conn.send('Thank you for connecting')
    conn.close()
