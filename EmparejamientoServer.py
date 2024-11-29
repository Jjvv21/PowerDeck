import socket
import threading
import time

# Dirección y puerto del servidor
HOST = '127.0.0.1'
PORT = 65432

# Lista para almacenar los jugadores que están esperando en la cola
player_queue = []

# Diccionario para guardar los emparejamientos entre jugadores
match_history = {}

# Esta función maneja la conexión con cada jugador
def handle_player_connection(player_socket, player_address):
    # Añadimos al jugador a la cola junto con su dirección
    player_queue.append((player_socket, player_address))
    print(f"Jugador conectado: {player_address}. Total de jugadores en cola: {len(player_queue)}")

    while True:
        # Revisamos si hay al menos dos jugadores en la cola para emparejarlos
        if len(player_queue) >= 2:
            # Sacamos a los dos primeros jugadores de la cola
            player1, addr1 = player_queue.pop(0)
            player2, addr2 = player_queue.pop(0)

            # Guardamos el emparejamiento en un diccionario
            match_history[addr1] = addr2
            match_history[addr2] = addr1

            # Les enviamos un mensaje para que acepten la partida
            player1.sendall("Emparejado con otro jugador. ¿Aceptar partida? (Y/N)".encode("utf-8"))
            player2.sendall("Emparejado con otro jugador. ¿Aceptar partida? (Y/N)".encode("utf-8"))


            # Esperamos la respuesta de ambos jugadores
            player1_response = wait_for_response(player1, addr1)
            player2_response = wait_for_response(player2, addr2)

            if player1_response != "Y" or player2_response != "Y":
                # Si alguno cancela, notificamos a ambos y terminamos el emparejamiento
                player1.sendall(b"La cola fue cancelada por tu oponente.")
                player2.sendall(b"La cola fue cancelada por tu oponente.")
                print(f"Emparejamiento cancelado entre {addr1} y {addr2}")
            else:
                # Si ambos aceptan, se inicia la partida
                player1.sendall(b"Partida aceptada. Inicia el juego!")
                player2.sendall(b"Partida aceptada. Inicia el juego!")
                print(f"Partida iniciada entre {addr1} y {addr2}")
        else:
            # Si no hay suficientes jugadores, notificamos al jugador que espere
            player_socket.sendall(b"Esperando un rival...")
            time.sleep(1)

# Esta función espera una respuesta del jugador dentro de un tiempo límite
def wait_for_response(player_socket, player_address, timeout=10):
    player_socket.settimeout(timeout)  # Establecemos el tiempo límite
    try:
        # Recibimos la respuesta del jugador
        response = player_socket.recv(1024).decode().strip()
        return response
    except socket.timeout:
        # Si el jugador no responde a tiempo, devolvemos "N" (cancelación)
        print(f"Jugador {player_address} no respondió a tiempo.")
        return "N"

# Esta función inicia el servidor y escucha conexiones entrantes
def start_server():
    # Creamos el socket del servidor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))  # Enlazamos el socket a la dirección y puerto
        server_socket.listen()  # Ponemos el socket en modo de escucha

        print("Esperando jugadores...")
        
        while True:
            # Aceptamos nuevas conexiones
            player_socket, player_address = server_socket.accept()
            print(f"Conexión de: {player_address}")
            
            # Creamos un hilo para manejar cada conexión de jugador
            threading.Thread(target=handle_player_connection, args=(player_socket, player_address)).start()

# Inicia el servidor cuando se ejecuta este archivo
if __name__ == "__main__":
    start_server()
