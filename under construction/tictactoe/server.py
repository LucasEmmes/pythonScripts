import socket
import threading

import room

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

rooms = []


def get_room(code):
    for room in rooms:
        if room.room_code == code:
            return room
    return False

def handle_client(conn, addr):
    username = False
    user_id = False
    in_room = False

    print(f"{addr} connected")
    connected = True

    try:
        while connected:
            msg = conn.recv(2048).decode(FORMAT)

            # GET USERNAME IF NOT REGISTERED
            if not username:
                username, user_id = msg.split("|")
                conn.send("1".encode(FORMAT))

            # IF NOT CONNECTED TO A ROOM, EITHER JOIN OR CREATE
            elif not in_room:
                # JOIN ECISTING ROOM
                if msg[:4] == "JOIN":
                    # find room
                    room_code = msg[4:]
                    check_room = get_room(room_code)
                    # check if room exists
                    if check_room:
                        # check if can join
                        if check_room.connect_player(user_id):
                            # join and inform user
                            in_room = check_room
                            conn.send("1-JOIN".encode(FORMAT))
                            print(f"{username} JUST JOINED ROOM {room_code}")
                        else:
                            conn.send("0-JOIN-FULL".encode(FORMAT))
                            print(f"{username} FAILED TO JOIN {room_code} REASON: FULL")
                    else:
                        conn.send("0-JOIN-CODE".encode(FORMAT))
                        print(f"{username} FAILED TO JOIN {room_code} REASON: ROOM NOT FOUND")
                
                # CREATE NEW ROOM
                elif msg == "CREATE":
                    # create new room and join player to it
                    in_room = room()
                    rooms.append(in_room)
                    room_code = in_room.room_code
                    # inform user about code
                    if in_room.connect_player(user_id):
                        conn.send(f"1-CREATE-{room_code}".encode(FORMAT))
                        print(f"USER {username} HAS MADE A NEW ROOM WITH CODE {room_code}")
                    else:
                        conn.send("0-CREATE".encode(FORMAT))
                        print("FAILED TO CREATE NEW ROOM")

                else:
                    conn.send("0-PARSE".encode(FORMAT))
                    print(f"COULDNT UNDERSTAND A WORD THAT {username} WAS SAYING")

            # IF CONNECTED TO A ROOM: PLAY GAME
            else:
                pass


    except socket.error:
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