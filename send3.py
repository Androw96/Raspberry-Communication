#Sending
import socket
import time
import os

floor = 0
row = 0
in_out = 0
trueornot = True
filename = "input.txt"
        
def read_file():
    global floor
    global row
    global in_out
    count = 1
    global filename
    filename = "input.txt"
    global trueornot
# File reading
    try:
            
        file1 = open(filename, 'r')
        if(file1 == 0):
            print("Nem tudtam megnyitni a file-t")
        elif(file1 != 0):
            print("olvasok")
            Lines = file1.readlines()
# Reading line by line
        for line in Lines:
            print("for olvasok")
            if(count == 1):
                line = line.rstrip()
                floor = line
            elif(count == 2):
                line = line.rstrip()
                row = line
            elif(count == 3):
                line = line.rstrip()
                in_out = line
            count = count+1
        print("Torolnek")
        trueornot = True
        file1.close()
        deletingFile()
        
        
    except:
        print("Nincs file!")
        trueornot = False

def deletingFile():
    print("deletingben")
    if os.path.exists(filename):
        print("deleted")
        os.remove(filename)
    else:
        print("The file does not exist")
        
        
UDP_IP = "169.254.129.26"
UDP_PORT = 5005
unique_num = 3
    
while(1):
    read_file()
    print(floor)
    if(trueornot == True):
        MESSAGE = "{}\n{}\n{}\n{}\n".format(floor, row, in_out, unique_num)
        print "UDP target IP:", UDP_IP
        print "UDP target port:", UDP_PORT
        print "message:", MESSAGE
        sock = socket.socket(socket.AF_INET, # Internet
                             socket.SOCK_DGRAM) # UDP
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        floor = 0
        row = 0
        in_out = 0
    time.sleep(1)
