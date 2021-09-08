import socket
import os
import time
import serial
import sshtunnel
import MySQLdb

path = '/dev/ttyS0' 
ser = serial.Serial(path, 19200)


def flush_buffer():
    print("Deleting the buffer")
    for i in range(64):
        ser.read()


def read_from_Arduino():
    message = {}
    while (1):
        print("olvasnek")
        i = ser.read()
        # print(type(i))
        # i = int(i, 16)
        # print(type(i))
        if (i == -126):
            for j in range(5):
                message[j] = ser.read()
                print(message[j])
            if (ser.read() != -125):
                # Order fail
                print("Order Fail!")
            else:
                # Right Order
                flush_buffer()
                return message[0]


def send_to_Arduino(data):
    # Sending floor and row to the Arduin  
    send_String = data
    
    try:
        ser.write(send_String.encode())
    except:
        print("NO SERIAL")


sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0


with sshtunnel.SSHTunnelForwarder(
    ('ssh.pythonanywhere.com'),
    ssh_username='Ozymandias', ssh_password='Androw96',
    remote_bind_address=('Ozymandias.mysql.pythonanywhere-services.com', 3306)
) as tunnel:
    connection = MySQLdb.connect(
        user='Ozymandias',
        passwd='Androw96',
        host='127.0.0.1', port=tunnel.local_bind_port,
        db='Ozymandias$SmartWarehouseSystem',
    )

UDP_IP = "0.0.0.0"
UDP_PORT = 5005
print("waiting")
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) #BUFFERSIZE
    send_to_Arduino(data)
    msg = str(read_from_Arduino())
    while((msg != "64") or (msg != "40")):
        msg = str(read_from_Arduino())
        mycursor = connection.cursor()
        sql = "INSERT INTO System_App_get (name, code, description) VALUES (%s, %s, %s)"
        val = ("get_process", msg, "Process from Arduino")
        mycursor.execute(sql, val)
        connection.commit()

    data = 0
    
    
