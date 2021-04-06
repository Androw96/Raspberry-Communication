import serial
import os
import time
import zmq

answer = "0"
floor = 0
row = 0
count = 1
input = "input.txt"
curMsg = 0

# reading the file
def read_file():
    global answer
    global floor
    global row
    global count
    global input
    count_while = 1
# File reading
    while(count_while < 2):
        file1 = open(input, 'r')
        if(file1 == 0):
            print("Nem tudtam megnyitni a file-t")
        elif(file1 != 0):
            Lines = file1.readlines()
# Reading line by line
        for line in Lines:
            if(count == 1):
                floor = line
            elif(count == 2):
                row = line
            count = count+1
        print(floor, row)
        count_while = count_while + 1
    #send_to_Arduino(floor, row)
    answer = "0"
    file1.close()

# Deleting the file
def deletingFile():
    if os.path.exists(input):
        print("deleted")
        os.remove(input)
    else:
        print("The file does not exist")

def send_to_Arduino():
    # Sending floor and row to the Arduino
    global answer
    global floor
    global row
    send_String = "{}{}\n".format(floor, row)
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
                    break
                
def zmq_pub():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind('tcp://127.0.0.1:2000')
    global floor
    global row
    message = [floor, row]
    curMsg = 0

    while(True):
        time.sleep(1)
        if(curMsg == 1):
            socket.send_pyobj(row)
            curMsg = 0
            break
        else:
            socket.send_pyobj(floor)
            curMsg = curMsg + 1

def zmq_sub():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect('tcp://127.0.0.1:2000')
    socket.setsockopt(zmq.SUBSCRIBE, b'')
    print("belepek a whileba")
    global curMsg
    global floor
    global row
    while(1):
        print("Fogadnam az adatot")
        message = socket.recv_pyobj()
        print("Megkapja")
        if(curMsg == 1):
            print(message)
            row = message
            curMsg = 0
            break
        else:
            floor = message
            print(floor)
            curMsg = curMsg + 1
            


while(1):
    zmq_sub();
    print("End of Subscription...\n Starting again... ")
    print("Value of Floor is: {},\n Value of Row is: {}".format(floor, row))
    
    time.sleep(1)