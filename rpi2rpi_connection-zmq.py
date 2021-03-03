import zmq
import time
import os
import sys

curMsg = 0
floor = 0
row = 0
count = 0
# reading the file
def read_file():
    global answer
    global floor
    global row
    global count
    count_while = 1
    input = "input.txt"
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
def zmq_pub():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind('tcp://127.0.0.1:2000')
    global floor
    global row
    global curMsg

    while(1):
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
    global curMsg
    while(True):
        message = socket.recv_pyobj()
        if(curMsg == 1):
            print(message)
            curMsg = 0
            break
        else:
            curMsg = curMsg + 1
while(1):
    read_file()
    zmq_pub()
    print("End of Publish...\n Starting again...")
    time.sleep(1)