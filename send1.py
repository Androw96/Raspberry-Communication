# Sending
import socket
import time
import os

code = 0
_from = 0
_from2 = 0
_to = 0
_to2 = 0
trueornot = True
filename = '/home/pi/Raspberry-Communication/input.txt'


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


# Level1
UDP_IP = "169.254.129.26"
UDP_PORT = 5005
unique_num = 0

while (1):
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

        print
        "UDP target IP:", UDP_IP
        print
        "UDP target port:", UDP_PORT
        print
        "message:", MESSAGE
        sock = socket.socket(socket.AF_INET,  # Internet
                             socket.SOCK_DGRAM)  # UDP
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        code = 0
        _from = 0
        _from2 = 0
        _to = 0
        _to2 = 0

    time.sleep(1)
