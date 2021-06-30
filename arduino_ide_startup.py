import time
import serial
import termios

send_String = "1\n2\n3\n4\n"

path = '/dev/ttyACM0'

# Disable reset after hangup
with open(path) as f:
    attrs = termios.tcgetattr(f)
    attrs[2] = attrs[2] & ~termios.HUPCL
    termios.tcsetattr(f, termios.TCSAFLUSH, attrs)


try:
    ser = serial.Serial(path, 9600)
    ser.write(send_String.encode())
except:
    try:
        path = '/dev/ttyACM1'
        ser = serial.Serial(path, 9600)
        ser.write(send_String.encode())
    except:
        path = '/dev/ttyACM2'
        ser = serial.Serial(path, 9600)
        ser.write(send_String.encode())