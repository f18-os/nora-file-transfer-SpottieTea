
       filename = input("Enter the name of the file you want to send: \n")
       theFile = open(filename,'rb')
       #fs.sendmsg(filename.encode())
       for l in theFile:
           fs.sendmsg(l)
           print("received:", fs.receivemsg())

           #fs.sendmsg(b"hello world")
           #print("received:", fs.receivemsg())

