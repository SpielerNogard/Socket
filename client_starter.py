from socket_system import Message_Client

Client = Message_Client("192.168.10.20",6000)
Client.connect_to_server()

for a in range(100):
    Client.send_data_to_server("Datensatz nummer: "+str(a))
    Client.recieve_data()
    Client.send_data_to_server("Close Connection")

Client.close_connection()