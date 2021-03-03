import zmq
import time
import os
import sys

while True:

    msg = '/home/pi/Raspberry-Communication/input.txt'

    # Preparing context
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind("tcp://*:2002")
    time.sleep(1)

    curFile = '/home/pi/Raspberry-Communication/input.txt'
    size = os.stat(curFile).st_size
    print('File size: '.format(size))

    target = open(curFile, 'rb')
    file = target.read(size)
    if file:
        publisher.send(file)

    publisher.close()
    context.term()
    target.close()
    time.sleep(1)
    