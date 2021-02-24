import serial
import os
import time

# reading the file
def read_file():
    floor = 0
    row = 0
    count = 1
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
    send_to_Arduino(floor, row)
    file1.close()
# Deleting the file
    if os.path.exists(input):
        os.remove(input)
    else:
        print("The file does not exist")

def send_to_Arduino(floor, row):
    # Sending floor and row to the Arduino
    if __name__ == '__main__':
        ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
        ser.flush()
    while True:
        ser.write(floor)
        ser.write(row)
        time.sleep(1)

while(1):
    read_file()