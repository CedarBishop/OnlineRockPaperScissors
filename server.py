import socket
from _thread import *
from helper import *
from player import Player
import sys
import pickle

server = "192.168.0.26"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))

except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server started")

players = [Player(0, 0, 50, 50, (0, 255, 255)), Player(100, 100, 50, 50, (255, 255, 0))]

def threaded_client(conn, player_number):
    conn.send(pickle.dumps(players[player_number]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player_number] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player_number == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost Connection")
    conn.close()


current_player = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1
