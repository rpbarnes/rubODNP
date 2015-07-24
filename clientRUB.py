"""
This will create a connection to the Elexsys computer such as to issue commands to xepr.
"""
import socket
import threading
import time
import subprocess
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverAddress = ('134.147.66.2',7000) # address to the xepr computer
print >>sys.stderr,'connecting to %s on port %s'% serverAddress
sock.connect(serverAddress)

message = 'Hello out there'

sock.sendall(message)


# Look for the response
amount_received = 0
amount_expected = len(message)

while amount_received < amount_expected:
    data = sock.recv(16)
    amount_received += len(data)
    print >>sys.stderr, 'received "%s"' % data
    
print >>sys.stderr, 'closing socket'
sock.close()

