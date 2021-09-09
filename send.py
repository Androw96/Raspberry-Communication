#Sending
import socket

global floor, row, in_out

def read_file():
    global floor
    global row
    global in_out
    count_while = 1
    count = 1
    input = "input.txt"
# File reading
    while(count_while < 3):
        file1 = open(input, 'r')
        if(file1 == 0):
            print("Nem tudtam megnyitni a file-t")
        elif(file1 != 0):
            Lines = file1.readlines()
# Reading line by line
        for line in Lines:
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
        count_while = count_while + 1
    file1.close()
    
unique_num = 3
read_file()
UDP_IP = "169.254.129.26"
UDP_PORT = 5005
MESSAGE = []
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))