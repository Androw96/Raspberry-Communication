import serial
import os
import time

answer = "0"
# reading the file
def read_file():
    global answer
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
    answer = "0"
    file1.close()
# Deleting the file
    #if os.path.exists(input):
        #print("deleted")
        #os.remove(input)
    #else:
        #print("The file does not exist")

def send_to_Arduino(floor, row):
    # Sending floor and row to the Arduino
    global answer
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
<<<<<<< Updated upstream
                #time.sleep(1)
                if(answer == "y"):
                    print("bennt")
=======
                # Arduino has sent the "finished" answer
                if(answer == "finished"):
>>>>>>> Stashed changes
                    break


while(1):
    read_file()
    print("End")