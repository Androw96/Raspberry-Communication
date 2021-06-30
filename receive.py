import socket
import os
import time
import serial

def send_to_Arduino(data):
    # Sending floor and row to the Arduino
    path = '/dev/ttyACM0'

    # Disable reset after hangup
    with open(path) as f:
    attrs = termios.tcgetattr(f)
    attrs[2] = attrs[2] & ~termios.HUPCL
    termios.tcsetattr(f, termios.TCSAFLUSH, attrs)
    
    send_String = data
    
    if __name__ == '__main__':
        try:
            ser = serial.Serial(path, 9600)
            ser.write(send_String.encode())
        except:
            try:
                path = '/dev/ttyACM1'
                ser = serial.Serial(path, 9600)
                ser.write(send_String.encode())
        except:
            path = '/dev/ttyACM2'
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
    
    
