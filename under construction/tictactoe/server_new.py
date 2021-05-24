import socket
import threading
import time
from room import room
import tictac

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# key: code; value: room obj
rooms = {}
# key: user_id; value: connection
connections = {}

users = {}

def get_room(code):
    for room in rooms:
        if room.room_code == code:
            return room
    return False

def get_connection(user_id):
    for id in connections.keys():
        if id == user_id:
            return connections[id]
    return False

def get_name(id):
    if users[id]:
        return users[id]
    else:
        return "ANONYMOUS PLAYER"


# FUNTIONS USED IN HANDLE_CLIENT
def get_user_info(msg):
    data = msg.split("|")
    if len(data) == 2:
        return data[0], data[1]
    else:
        return False, "anonymous player"

def handle_create_new_room(user_id, conn):
    new_room = room()
    new_room.connect_player(user_id, conn)
    rooms[new_room.room_code] = new_room
    conn.send(f"2-CODE-{new_room.room_code}".encode(FORMAT))
    return new_room


def player_join_room(code, user_id, conn):
    for room_code in rooms.keys():
        if room_code == code:
            if rooms[room_code].connect_player(user_id, conn):
                conn.send("1-JOIN".encode(FORMAT))
                conn.send(f"2-OPPONENT-{get_name(rooms[room_code].p1)}".encode(FORMAT))
                return rooms[room_code]
    return False

def handle_move(user_id, conn, in_room, move):
    if in_room.game.turn(user_id, move):
        conn.send("1-MOVE".encode(FORMAT))
        in_room.announce(f"2-MOVE-{in_room.game.board}")
        return True
    else:
        conn.send("0-MOVE".encode(FORMAT))
        return False

def handle_wincheck(in_room):
    if in_room.game.done:
        if in_room.game.winner:
            in_room.announce(f"2-WINNER-{in_room.game.winner}")
        else:
            in_room.announce(f"2-TIE")
        return True
    return False

# TODO - handle passing info to enemy

def handle_client(conn, addr):
    username = False
    user_id = "anonymous player"
    in_room = False
    enemy_conn = False

    print(f"{addr} connected")
    connected = True

    try:
        while connected:
            msg = conn.recv(2048).decode(FORMAT)

            # GET USERNAME
            if not username:
                username, user_id = get_user_info(msg)
                if username:
                    conn.send("1-USERNAME".encode(FORMAT))
                    users[user_id] = username
                    print(f"{addr} HAS APPLIED THE USERNAME '{username}' AND USER_ID '{user_id}'")
                else:
                    conn.send("0-USERNAME".encode(FORMAT))
                    print(f"SOMETHING WENT WRONG WHEN {addr} TRIED TO APPLY USERNAME")
                    print(f"MESSAGE:{msg}")
                    continue

            # ASSIGN ROOM
            elif not in_room:
                # CREATE NEW ROOM
                if msg[:6].upper() == "CREATE":
                    in_room = handle_create_new_room(user_id, conn)
                    if in_room:
                        conn.send("1-CREATE".encode(FORMAT))
                        print(f"PLAYER {username} HAS CREATED A NEW ROOM")
                    else:
                        conn.send("0-CREATE".encode(FORMAT))
                        print(f"PLAYER {username} FAILED TO CREATE A NEW ROOM")
                        

                # JOIN EXISTING ROOM
                if msg[:4].upper() == "JOIN":
                    in_room = player_join_room(msg[4:], user_id, conn)
                    if in_room:
                        print(f"PLAYER {username} HAS JOINED A ROOM")

                        enemy_conn = in_room.p1_conn
                        enemy_conn.send(f"2-OPPONENT-{username}".encode(FORMAT))
                        time.sleep(1)

                        in_room.start_game()
                        in_room.announce(f"2-START-{in_room.game.player_turn}")

                    else:
                        conn.send("0-JOIN".encode(FORMAT))
                        print(f"PLAYER {username} FAILED TO CONNECT TO A ROOM")

            # MAKE MOVE
            elif msg[:4].upper() == "MOVE":
                if handle_move(user_id, conn, in_room, msg[4:]):
                    print(f"{username} MADE A MOVE")
                    if handle_wincheck(in_room):
                        print("GAME HAS ENDED")
                else:
                    print(f"{username} FAILED TO MAKE MOVE")
            
            else:
                print("COULDN'T PARSE GIBBERISH")

    except socket.error:
        print(f"{user_id} FORCEFULLY DISCONNECTED")
        pass

    conn.close()
    


def start():
    print(f"[STARTING SERVER]")
    server.listen()
    print(f"SERVER IP: {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args=(conn, addr))
        thread.start()
        print("New connection")

start()