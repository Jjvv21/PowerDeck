import socket
import threading
import time

# Dirección y puerto del servidor
HOST = '127.0.0.1'
PORT = 65432

# Cola de jugadores
player_queue = []

# Función para manejar la conexión de un jugador
def handle_player_connection(player_socket):
    # Añadir al jugador a la cola
    player_queue.append(player_socket)
    print(f"Jugador conectado. Total de jugadores en cola: {len(player_queue)}")

    # Si hay al menos 2 jugadores en la cola, iniciar el juego
    if len(player_queue) >= 2:
        player1 = player_queue.pop(0)
        player2 = player_queue.pop(0)

        # Enviar mensaje de inicio de juego a los jugadores
        player1.sendall(b"Jugador 1: Has sido emparejado con otro jugador. Inicia el juego!")
        player2.sendall(b"Jugador 2: Has sido emparejado con otro jugador. Inicia el juego!")

    # Si solo hay un jugador y pasan 10 segundos, emparejarlo con un bot
    else:
        player_socket.sendall(b"Esperando un rival...")
        start_time = time.time()
        while len(player_queue) == 1 and time.time() - start_time < 10:
            time.sleep(1)

        if len(player_queue) == 1:  # Si pasa más de 10 segundos, emparejar con bot
            player_socket.sendall(b"No se encontro rival, emparejando con un bot.")
            bot_socket = create_bot_socket()
            player_socket.sendall(b"Emparejado con el bot.")
            bot_socket.sendall(b"Emparejado con un jugador.")
        else:
            # Si se encontró un segundo jugador
            player_socket.sendall(b"Jugador emparejado con otro jugador. Inicia el juego!")

# Función para crear un socket para el bot (simulado)
def create_bot_socket():
    bot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bot_socket.connect((HOST, PORT))  # Conectarse al mismo servidor
    return bot_socket

# Función para escuchar las conexiones de los jugadores
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print("Esperando jugadores...")
        
        while True:
            player_socket, player_address = server_socket.accept()
            print(f"Conexión de: {player_address}")
            threading.Thread(target=handle_player_connection, args=(player_socket,)).start()

# Iniciar el servidor
if __name__ == "__main__":
    start_server()
