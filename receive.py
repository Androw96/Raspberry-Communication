import socket
import os
import time
import serial

path = '/dev/ttyS0' 
ser = serial.Serial(path, 9600)

def send_to_Arduino(data):
    # Sending floor and row to the Arduin  
    send_String = data
    
    try:
        ser.write(send_String.encode())
    except:
        print("NO SERIAL")
            
UDP_IP = "0.0.0.0"
UDP_PORT = 5005
print("waiting")
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024) #BUFFERSIZE
    send_to_Arduino(data)
    data = 0
    
    
