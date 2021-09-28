import smtplib #importing the module

sender_add="okosraktar@dentarttechnik.hu" #storing the sender's mail id
receiver_add="csilla@dentarttechnik.hu" #storing the receiver's mail id
password="!w3aexZ!RJqp" #storing the password to log in
 #creating the SMTP server object by giving SMPT server address and port number
smtp_server=smtplib.SMTP("mail.dentarttechnik.hu",587)
smtp_server.ehlo() #setting the ESMTP protocol
smtp_server.starttls() #setting up to TLS connection
smtp_server.ehlo() #calling the ehlo() again as encryption happens on calling startttls()
smtp_server.login(sender_add,password) #logging into out email id
msg_header = '''From: {sender_address}
To: {receiver_address}
Subject: {subject}
'''.format(sender_address=sender_add, receiver_address=receiver_add, subject="Okosraktar Udvozol")

msg_body = '''
Teszt Uzenet az Okosraktartol!
'''
msg_to_be_sent = msg_header + msg_body
#sending the mail by specifying the from and to address and the message
smtp_server.sendmail(sender_add,receiver_add,msg_to_be_sent)
print('Sent!') #priting a message on sending the mail
smtp_server.quit()#terminating the server