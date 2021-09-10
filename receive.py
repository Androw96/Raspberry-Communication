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

def get_get(msg):
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
        # Do stuff
        mycursor = connection.cursor()
        sql = "INSERT INTO System_App_get (name, code, description) VALUES (%s, %s, %s)"
        val = ("get_process", msg , "")
        mycursor.execute(sql, val)
        connection.commit()
        print("Uploaded")
        connection.close()

def read_from_Arduino():
    message = {}
    start_marker = 130
    end_marker = 131
    
    while (1):
        i = ser.read().hex()
        i = int(i, 16)
        print(i)
        # print(type(i))
        
        # print(type(i))
        if (i == start_marker):
            for j in range(6):
                i = ser.read().hex()
                i = int(i, 16)
                message[j] = i
                print(message[j])
                
            i = ser.read().hex()
            i = int(i, 16)
            if (i != end_marker):
                # Order fail
                print(message)
            else:
                # Right Order
                flush_buffer()
                return message[0]


def send_to_Arduino(data):
    # Sending floor and row to the Arduin
    global ser

    try:
        for i in range(5):
            message = data[i]
            print(message)
            ser.write(message.encode())
    except:
        print("NO SERIAL")


UDP_IP = "0.0.0.0"
UDP_PORT = 5005
print("waiting")
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) #BUFFERSIZE
    new_data = data.replace('\n', ' ').split(' ')

    send_to_Arduino(new_data)
    msg = str(read_from_Arduino())
    get_get(msg)

    while((msg != "64") or (msg != "40")):
        msg = str(read_from_Arduino())
        get_get(msg)
        time.sleep(1)

    data = 0

