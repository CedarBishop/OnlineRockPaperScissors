import socket
import pickle


class Network:
    def __init__(self):
        print("Initialised network")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "172.105.184.12"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.player = self.connect()

    def get_player(self):
        return self.player

    def connect(self):
        print("Attempting to connect")
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e + "\nConnection error")

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e + "\nsend error")


