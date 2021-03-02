import zmq
import time
import os
import sys

def zmq_pub():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind('tcp://127.0.0.1:2000')
    global floor
    global row
    floor = 6
    row = 5
    message = [floor, row]
    curMsg = 0

    while(True):
        time.sleep(1)
        socket.send_pyobj({curMsg:message[curMsg]})
        if(curMsg == 2):
            break
        else:
            curMsg = curMsg + 1

def zmq_sub():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect('tcp://127.0.0.1:2000')
    socket.setsockopt(zmq.SUBSCRIBE, '')
    curMsg = 0;
    while(True):
        message = socket.recv_pyobj()
        if(curMsg == 1):
            print(message)
            break

while(1):
    zmq_pub()
    print("End of Publish...\n Starting again...")
    time.sleep(1)