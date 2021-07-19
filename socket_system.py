import socket


class Message_Server():
    def __init__(self,adress,port):
        self.port = port
        self.host = adress
        self.Socket = socket.socket()
    
    def start_server(self):
        self.Socket.bind((self.host,self.port))
        self.Socket.listen()
        print("Server started")
        while True:
            try:
                self.conn,self.adress = self.Socket.accept()
                while True:
                    print("Connected to: ",self.adress)
                    nachricht = self.conn.recv(1024)
                    ende = "Close Connection"
                    Schließnachricht = ende.encode
                    if nachricht == Schließnachricht:
                        self.close_connection()
                    print("["+str(self.adress)+"]: "+str(nachricht))

                    st = "Thank you for connecting"
                    byt = st.encode()
                    self.conn.send(byt)
            except Exception as e:
                print(e)
                break

    def close_connection(self):
        self.conn.close()

class Message_Client():
    def __init__(self,adress,port):
        self.port = port
        self.host = adress
        self.Socket = socket.socket()

    def connect_to_server(self):
        self.Socket.connect((self.host,self.port))
        print("Connected to: "+self.host+":"+str(self.port))
    
    def send_data_to_server(self,data):
        arr = bytes(data, 'utf-8')
        self.Socket.send(arr)

    def recieve_data(self):
        data = self.Socket.recv(1024)
        print(data)

    def close_connection(self):
        self.Socket.close()
        
    