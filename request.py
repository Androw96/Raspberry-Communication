import zmq
import time
import sys

port = "1717"
host = "169.254.235.189"
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://169.254.235.189:1717")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print "Received request: ", message
    Input = input()
    time.sleep (1)  
    socket.send(Input)
