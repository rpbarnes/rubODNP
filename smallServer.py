import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('127.0.0.1',9000)) # this will work if coming from computer but I think this will need to be changed to the outside address for functionality with the specman comp.
### Outside facing ip is 128.111.114.94
sock.listen(5)
print "Server is live"
while True:
    conn,addr = sock.accept()
    print 'Got connection from ', addr
    incoming = ''
    command_buffer = []
    try: # if this faults out lets remake the connection with the host machine
        temp = conn.recv(128) 
        print temp
    except:
        conn.close()
        conn, addr = sock.accept()
        temp = conn.recv(128) # if nothing received the script hangs

    if not temp: break
    incoming = incoming + temp
    if incoming[-1] != '\n':
        if incoming.find('\n'):
            temp = incoming.split('\n')
            command_buffer.extend(temp[:-1])
            incoming = temp[-1]
        else:
            break
    else:
        command_buffer.extend(incoming.split('\n'))
        incoming = ''
    print command_buffer
    conn.send('Thank you for connecting')
    conn.close()
