import zmq
import time
import os
import sys

curMsg = 0

def zmq_pub():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind('tcp://127.0.0.1:2000')
    global floor
    global row
    floor = 6
    row = 5
    sendString = "{}{}".format(floor, row)
    message = [floor, row]
    global curMsg

    while(True):
        time.sleep(1)
        socket.send_pyobj({message[curMsg]})
        if(curMsg == 1):
            print(message[curMsg])
            curMsg = 0
            break
        else:
            print(message[curMsg])
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
    zmq_pub()
    print("End of Publish...\n Starting again...")
    time.sleep(1)