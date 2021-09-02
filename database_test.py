import MySQLdb
import sshtunnel

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
    val = ("get_process", "63", "Kiadta a dobozt")
    mycursor.execute(sql, val)
    connection.commit()
    print("done")
    connection.close()