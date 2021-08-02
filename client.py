import zmq
import sys

code = 0
_from = 0
_from2 = 0
_to = 0
_to2 = 0
trueornot = True
filename = '/home/pi/Raspberry-Communication/input.txt'

port = "1717"
    
print "Connecting to server..."
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect ("tcp://169.254.235.189:1717")

def read_file():
    global code
    global _from
    global _from2
    global _to
    global _to2
    count = 1
    global filename
    global trueornot
    # File reading
    try:
        print("Keres!")
        print(filename)
        file1 = open(filename, 'r')
        if (file1 == 0):
            print("Nem tudtam megnyitni a file-t")
        elif (file1 != 0):
            print("olvasok")
            Lines = file1.readlines()
        # Reading line by line
        for line in Lines:
            print("for olvasok")
            if (count == 1):
                line = line.rstrip()
                code = line
            elif (count == 2):
                line = line.rstrip()
                _from = line
            elif (count == 3):
                line = line.rstrip()
                _from2 = line
            elif (count == 4):
                line = line.rstrip()
                _to = line
            elif (count == 5):
                line = line.rstrip()
                _to2 = line

            count = count + 1
        print("Torolnek")
        trueornot = True
        file1.close()
        deletingFile()


    except:
        print("Nincs file!")
        trueornot = False


def deletingFile():
    print("deletingben")
    if os.path.exists(filename):
        print("deleted")
        os.remove(filename)
    else:
        print("The file does not exist")

#  Do 10 requests, waiting each time for a response
def Send_recv(MESSAGE):
    
    while True:
        read_file()
        print("Sending request ")
        socket.send (MESSAGE)
        #  Get the reply.
        message = socket.recv()
        createGet(message)

def createGet(message):
    file_path = '/home/pi/Raspberry-Communication/get.txt'
    with open(file_path, 'w') as f:
    f.write(message)
    
    
def main():
    global trueornot
    
    read_file()
    if (trueornot == True):
        if (code == "102"):
            _from = unique_num
            MESSAGE = "{}\n{}\n{}\n{}\n{}\n".format(code, _from, _from2, _to, _to2)
        if (code == "103"):
            _to = unique_num
            MESSAGE = "{}\n{}\n{}\n{}\n{}\n".format(code, _from, _from2, _to, _to2)
        if (code == "104"):
            _to = unique_num
            MESSAGE = "{}\n{}\n{}\n{}\n{}\n".format(code, _from, _from2, _to, _to2)
        if (code == "105"):
            MESSAGE = "{}\n{}\n{}\n{}\n{}\n".format(code, _from, _from2, _to, _to2)
        if (code == "106"):
            MESSAGE = "{}\n{}\n{}\n{}\n{}\n".format(code, _from, _from2, _to, _to2)
        if (code == "107"):
            _from = unique_num
            MESSAGE = "{}\n{}\n{}\n{}\n{}\n".format(code, _from, _from2, _to, _to2)
        if (code == "108"):
            _from = unique_num
            MESSAGE = "{}\n{}\n{}\n{}\n{}\n".format(code, _from, _from2, _to, _to2)
        
        Send_recv(MESSAGE)
        code = 0
        _from = 0
        _from2 = 0
        _to = 0
        _to2 = 0
        
while(1):
    main()
    