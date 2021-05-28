import socket
import os
import time
import serial

def send_to_Arduino(data):
    # Sending floor and row to the Arduino
    send_String = data
    print data
    print type(data)
    if __name__ == '__main__':
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        ser.flush()
    while answer == "0":
        ser.write(send_String.encode())
        while True:
            if ser.in_waiting > 0:
                answer = ser.readline().decode('utf-8').rstrip()
                print(answer)
                #time.sleep(1)
                if(answer == "fin"):
                    print("bennt")
                    break*/

UDP_IP = "0.0.0.0"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024) #BUFFERSIZE
    print "received message:", data
    send_to_Arduino(data)
    
    
