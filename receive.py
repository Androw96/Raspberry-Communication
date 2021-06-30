import socket
import os
import time
import serial

def send_to_Arduino(data):
    # Sending floor and row to the Arduino
<<<<<<< HEAD
    path = '/dev/ttyACM0'
=======
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
>>>>>>> 0557d6207de593738a8aade88ec63c27bdf93edd

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
    
    
