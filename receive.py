import socket
import os
import time
import serial

def send_to_Arduino(data):
    # Sending floor and row to the Arduino
    path = '/dev/ttyAMA0'   
    send_String = data
    
    if __name__ == '__main__':
        try:
            ser = serial.Serial(path, 9600)
            ser.write(send_String.encode())
        except:
            try:
                path = '/dev/ttyAMA1'
                ser = serial.Serial(path, 9600)
                    ser.write(send_String.encode())
            except:
                path = '/dev/ttyAMA2'
                ser = serial.Serial(path, 9600)
                ser.write(send_String.encode())
            
            
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
    
    
