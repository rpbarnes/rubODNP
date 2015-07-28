import threading
import time
import subprocess
import socket
import os
import csv


### Various Functions
def setAtten(attenuation,*args):#{{{
    print "I receive ", attenuation
#}}}

def ampOnOff(state,*args):#{{{
    print "I receive ", state
#}}}

#{{{ # Actual server part
host = '134.147.66.2'
port = 7000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port)) 
s.listen(10)
try:
    while True:
        print 'Ready for command. \n\n\nListening on %s port %d\n\n'%(host,port)
        s.settimeout(1e6)
        conn, addr = s.accept()
        print 'created connection at ' , addr
        incoming = ''
        command_buffer = []
        while 1:
            conn.settimeout(1e6) # set the timeout large enough so we don't need to worry about breaking the script
            try: # if this faults out lets remake the connection with the host machine
                temp = conn.recv(1024) 
            except:
                conn.close()
                conn, addr = s.accept()
                conn.settimeout(1e6) # set the timeout large enough so we don't need to worry about breaking the script
                temp = conn.recv(1024) # if nothing received the script hangs

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
            print "about to try to run the command buffer:",repr(command_buffer)
            for mycommand in command_buffer:
                if len(mycommand) == 0:
                    pass
                else:
                    mycommand = mycommand.split(' ')
                    if mycommand[0] == 'SETATTEN':
                        try:
                            attenuation = float(mycommand[1])
                            attenThread = threading.Thread(target = setAtten,args = (attenuation,1))
                            attenThread.start()
                        except Exception as errtxt:
                            print errtxt
                    elif mycommand[0] == 'AMPON':
                        try:
                            ampThread = threading.Thread(target = ampOnOff,args = ('0xFF',1))
                            ampThread.start()
                        except Exception as errtxt:
                            print errtxt
                    elif mycommand[0] == 'AMPOFF':
                        try:
                            ampThread = threading.Thread(target = ampOnOff,args = ('0x00',1))
                            ampThread.start()
                        except Exception as errtxt:
                            print errtxt
except KeyboardInterrupt:
    print "closing gracefully...\n"
    s.close()
    print "Closed socket connection.\n"
    print "\nGoodbye Dave\n\n"
#}}}
            
