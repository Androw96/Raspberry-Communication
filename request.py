import zmq
import time
import sys
import serial

global socket

path = '/dev/ttyS0'
ser = serial.Serial(path, 19200)



def send_to_Arduino(data):
    # Sending floor and row to the Arduin  
    send_String = data
    
    try:
        ser.write(send_String.encode())
    except:
        print("NO SERIAL")

def flush_buffer():
    print("Deleting the buffer")
    for i in range(64):
        ser.read()
        
def read_from_Arduino():
    flush_buffer()
    message = {}
    while(1):
        print("olvasnek")
        i = ser.read()
        #print(type(i))
        #i = int(i, 16)
        #print(type(i))
        if(i == -126):
            for j in range(5):
                message[j] = ser.read()
                print(message[j])
            if(ser.read() != -125):
                #Order fail
                print("Order Fail!")
            else:
                #Right Order
                flush_buffer()
                return message[0]


                
                
def communicate():

        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://169.254.129.26:1717")
        
        Input = ""
        #  Wait for next request from client
        message = socket.recv_pyobj()
        print("Received request: ", message)
        print("communicate")
        time.sleep (1)
        send_to_Arduino(message)
        while((Input != "64") or (Input != "40")):
            Input = read_from_Arduino()
            Input = "64"
            print(Input)
            socket.send(Input)

while(1):
    communicate()