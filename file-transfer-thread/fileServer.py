#! /usr/bin/env python3


import sys,re, socket, os
sys.path.append("../lib")       # for params
import params

switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50001),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )

progname = "echoserver"
paramMap = params.parseParams(switchesVarDefaults)

debug, listenPort = paramMap['debug'], paramMap['listenPort']

if paramMap['usage']:
    params.usage()

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # listener socket
bindAddr = ("127.0.0.1", listenPort)
lsock.bind(bindAddr)
lsock.listen(5)
print("listening on:", bindAddr)

#class ServerThread(Thread):
 #   def __init__(self, sock, debug):
  #      Thread.__init__(self, daemon=True)
        #self.fsock, self.debug = FramedStreamSock(sock, debug), debug #study this line
   #     self.start()


while True:
    
    sock, addr = lsock.accept()

    print("connection rec'd from", addr)

    from labSocket import framedSend, framedReceive
    if not os.fork():
        print("Recieving file name... \n")
        fileName = framedReceive(sock,debug).decode()
        print("Received name!")
        serverFile = open("serverFiles/"+fileName,"w")
        line = framedReceive(sock,debug)

        print("Writing to file... \n")
        
        while line:
            line = line.decode('ascii')
            
            if line == '/end':
                print("End of file!")
                sock.close()
                break
            serverFile.write(line)
            line = framedReceive(sock,debug)
                
        print("File recieved!")
