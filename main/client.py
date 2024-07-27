from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import socket, threading, pygame, sys

f = open(f"main/name.txt", "r")
username = f.read()
pygame.mixer.init()

def play_sound(i):
    if i == 1:
        pygame.mixer.music.load("main\music\Bad To The Bone Riff Sound Effect.mp3")
    elif i == 2:
        pygame.mixer.music.load(r"main\music\taco-bell.mp3")
    pygame.mixer.music.play()
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            if message == "bttb.mp3":
                play_sound(1)
            elif message == "tbbe.mp3":
                play_sound(2)
            print(message)
        except:
            break

def send_messages():
    while True:
        message = input()
        if message == "bttb.mp3":
            message = message
            play_sound(1)
        elif message == "tbbe.mp3":
            play_sound(2)
        elif message == "{[exit]}":
            exit()
        else:
            message = f"{username} : {message}"
        client_socket.send(message.encode('utf-8'))

def start_client():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages)
    send_thread.start()

if __name__ == "__main__":
    start_client()
