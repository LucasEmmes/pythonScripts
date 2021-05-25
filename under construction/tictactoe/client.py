import socket
import os
import threading
import random
import time

PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
# SERVER = input("Please enter server IP: ")
SERVER = "10.17.0.4"
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
connected = True

logged_in = False
in_game = False
opponent = False
my_turn = False
username = False
user_id = False
game_active = False
valid_move = False
game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def clear():
    os.system('cls')
    os.system('mode con: cols=39 lines=20')

def print_board(arr):
    clear()
    print("\n")
    print(f"{arr[0]}\n{arr[1]}\n{arr[2]}")
    print("\n")
    print("\n")

def startup():
    clear()
    print("---------------------------------------")
    print("\n")
    print("Welcome to TicTacToes".rjust(30, " "))
    print("\n")
    print("---------------------------------------")
    print("\n")
    print("\n")
    print("Enter a username between 3 and 20 chars")
    while True:
        username = input(">> ")
        if len(username) < 3 or len(username) > 20:
            print("I said please enter a username between 3 and 20 characters inclusive you fuck")
        elif " " in username:
            print("NO SPACES U CUNT")
        else:
            break
    return username

def get_in_game():
    clear()
    print("---------------------------------------")
    print("\n")
    print("You may create a new room,".rjust(7, " ")) 
    print("or join a friend via code".rjust(7, " "))
    print("\n")
    print("---------------------------------------")
    print("\n")
    print("\n")
    print("Type CREATE or JOIN")
    while True:
        decision = input(">> ")
        if decision.upper() == "CREATE":
            send("CREATE")
            time.sleep(1)
            if not in_game:
                print("Failed to create room")
            else:
                return 1
        elif decision.upper() == "JOIN":
            code = input("\nPlease enter the room code\n>> ")
            if len(code) > 4:
                print("The code is too long (like my dic)\n")
            else:
                send(f"JOIN{code}")
                time.sleep(1)
                if not in_game:
                    print("Failed to connect to room")
                    print("It may be full or the code may be wrong")
                else:
                    return 1
        else:
            print("Listen here you schmuck >:^O")

def make_move():
    print("Make your move")
    move = input(">> ")
    send(f"MOVE{move}")
    while True:
        time.sleep(1)
        if not valid_move:
            print("Not a valid move")
        else:
            return 1


def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)

def receive():
    global logged_in
    global in_game
    global opponent
    global my_turn
    global game_active

    print("RECEIVING DATA")
    while connected:
        data = client.recv(2048).decode(FORMAT)
        print(data)
        data = data.split("-")

        if data[0] == "2":
            if data[1] == "CODE":
                print(f"The code for the room is: {data[2]}")
            elif data[1] == "OPPONENT":
                opponent = data[2]
                print(f"You opponent is: {opponent}")
            elif data[1] == "START":
                print(f"Game has started!")
                if int(data[2]) == user_id:
                    my_turn = True
                    print(f"You go first")
                else:
                    print(f"{opponent} goes first")
                time.sleep(4)
                game_active = True
            elif data[1] == "MOVE":
                board_string = data[2]
                #TODO - turn string into 2d array
                pass
            else:
                pass
        # username handle
        elif data[1] == "USERNAME":
            if data[0] == "1":
                print("USERNAME SET SUCCESS")
                time.sleep(2)
                logged_in = True
            else:
                print("FAILED TO SET USERNAME :((((")
        
        # create room handle
        elif data[1] == "CREATE":
            if data[0] == "1":
                print("You have sucessfully made a room!")
                in_game = True
            else:
                print("FAILED TO CREATE GAME WTFTFTFT")
        # join room handle
        elif data[1] == "JOIN":
            if data[0] == "1":
                print("Joined the game!")
                time.sleep(1)
                in_game = True
            else:
                print("Failed to jion game wtftfwtf")
        elif data[1] == "MOVE":
            if data[0] == "1":
                pass
            else:
                pass
            # TODO - check validity

        # make move handle




def main():
    global logged_in
    global in_game
    global username
    global user_id
    global game_active

    rec_thread = threading.Thread(target=receive)
    rec_thread.start()

    while True:
        if not username:
            username = startup()
            user_id = random.randrange(0xFFFFFFFF) # 16 bit random user id
            send(f"{username}|{user_id}")
        
        if logged_in:
            if not in_game:
                get_in_game()
            elif not game_active:
                print("Waiting for opponent to connect...")
                while not game_active:
                    time.sleep(1)
            else:
                if my_turn:
                    print(game_board)
                    make_move()
                else:
                    time.sleep(1)
main()