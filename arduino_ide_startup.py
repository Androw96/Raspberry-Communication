import socket
import os
import time
import serial

global baud
path = '/dev/ttyS0'  
baud = 9600
print("Serial megtortent")
ser = serial.Serial(path, baud)

def send_to_Arduino(send_String):
    # Sending floor and row to the Arduino 
    send_String = "1"
    print("Kuldom")
    try:
        ser.write(send_String)
        data = ser.read()
        print(data)
    except:
        try:
            path = '/dev/ttyUSB1'
            ser = serial.Serial(path, 9600)
            ser.write(send_String.encode())
        except:
            try:
                path = '/dev/ttyUSB2'
                ser = serial.Serial(path, 9600)
                ser.write(send_String.encode())
            except:
                print("No Serial Connection")
                
    time.sleep(10)

send_String = "105\n0\n0\n0\n0\n"
while True:
    send_to_Arduino(send_String)
    data = 0
    
    

