import socket
import os
import time
import serial
import sshtunnel
import MySQLdb
import smtplib

path = '/dev/ttyS0' 
ser = serial.Serial(path, 19200)

def email_send(receiver_add,subject, msg_body):

    sender_add="okosraktar@dentarttechnik.hu" #storing the sender's mail id
    receiver_add="" #storing the receiver's mail id
    password="!w3aexZ!RJqp" #storing the password to log in
    subject = "Okosraktar Teszt"
     #creating the SMTP server object by giving SMPT server address and port number
    smtp_server=smtplib.SMTP("mail.dentarttechnik.hu",587)
    smtp_server.ehlo() #setting the ESMTP protocol
    smtp_server.starttls() #setting up to TLS connection
    smtp_server.ehlo() #calling the ehlo() again as encryption happens on calling startttls()
    smtp_server.login(sender_add,password) #logging into out email id
    msg_header = '''From: {sender_address}
    To: {receiver_address}
    Subject: {subject}
    '''.format(sender_address=sender_add, receiver_address=receiver_add, subject=subject)
    
    msg_to_be_sent = msg_header + msg_body
    #sending the mail by specifying the from and to address and the message
    smtp_server.sendmail(sender_add,receiver_add,msg_to_be_sent)
    print('Sent!') #priting a message on sending the mail
    smtp_server.quit()#terminating the server


def flush_buffer():
    print("Deleting the buffer")
    ser.read_all()

def get_get(msg):
    try:
        
        sshtunnel.SSH_TIMEOUT = 10.0
        sshtunnel.TUNNEL_TIMEOUT = 10.0

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
            sql = "INSERT INTO System_App_get_process (name, code, description) VALUES (%s, %s, %s)"
            val = ("get_process", msg , "")
            mycursor.execute(sql, val)
            connection.commit()
            print("Uploaded")
            connection.close()
    except MySQLdb.OperationalError as error:
            print("Operational error!")
            get_get(msg)
            
    except MySQLdb.IntegrityError as error:
            print("IntegrityError")
            
    except Exception as x:
            receiver_add = "konyaandras96@gmail.com" 
            subject = "Hiba: {hiba}".format(hiba = x)
            msg_body = '''
            Kedves András,
            Hiba történt az Okosraktár Motherbox rendszerében! A hibakód a következő: {hiba}
            Kérlek nézd meg mi okozhatja!
            Üdvözlettel,
            Okosraktár
            '''.format(hiba = x)
            msg_body = msg_body.encode('latin-1','replace').decode('latin-1')
            email_send(receiver_add, subject, msg_body)
            

def read_from_Arduino():
    message = {}
    start_marker = 130
    end_marker = 131
    trigger_codes = [23, 28, 30, 31, 40, 41, 42, 43, 46, 47, 51, 55, 57, 58, 63, 64]
    flush_buffer()
    while (1):
        print("Olvasok: ")
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
                
            i = ser.read().hex()
            i = int(i, 16)
            if (i != end_marker):
                print("Not the Endmarker I am looking for!")
            else:
                # Right Order
                if message[0] in trigger_codes:
                    #flush_buffer()
                    return message[0]


def send_to_Arduino(data):
    # Sending floor and row to the Arduin
    global ser
    message = data
    for i in range(0, len(data)):
        print(message[i])
        message[i] = int(data[i])
        
    message.insert(0, 130)
    message.append(0)
    message.append(131)
    message = bytes(message)
    for i in range(20):
        ser.write(message)
        print("{}. message: {}".format(i,message))

try:
    UDP_IP = "0.0.0.0"
    UDP_PORT = 5005
    print("waiting")
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        print("Ready")
        data, addr = sock.recvfrom(1024) #BUFFERSIZE
        data = data.decode('utf-8')
        new_data = data.replace('\n', ' ').split(' ')
        
        print(new_data)
        
        send_to_Arduino(new_data)
        
        msg = str(read_from_Arduino())
        get_get(msg)
        pre_msg = msg

        while(True):
            print("Checking")
            if((msg == "64") or (msg == "40") or (msg == "55")):
                break
            msg = str(read_from_Arduino())
            if(pre_msg != msg):
                print("pre_msg: {}".format(pre_msg))
                pre_msg = msg
                print("msg: {}".format(msg))
                get_get(msg)
                
            time.sleep(1)

        data = 0
        
except Exception as x:
            receiver_add = "konyaandras96@gmail.com" 
            subject = "Hiba: {hiba}".format(hiba = x)
            msg_body = '''
            Kedves András,
            Hiba történt az Okosraktár Motherbox rendszerében! A hibakód a következő: {hiba}
            Kérlek nézd meg mi okozhatja!
            Üdvözlettel,
            Okosraktár
            '''.format(hiba = x)
            msg_body = msg_body.encode('latin-1','replace').decode('latin-1')
            email_send(receiver_add, subject, msg_body)

