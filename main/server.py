import socket
import threading

# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"[+] New connection from {client_address}")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            broadcast_message(message, client_socket)
        except:
            clients.remove(client_socket)
            break

    client_socket.close()

# Function to broadcast messages to all clients
def broadcast_message(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                clients.remove(client)

# Main function to start the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8080))
    server.listen(5)
    print("[*] Server listening on port 8080")

    while True:
        client_socket, client_address = server.accept()
        clients.append(client_socket)
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

clients = []

if __name__ == "__main__":
    start_server()
