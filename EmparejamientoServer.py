import socket
import threading
import time

# Dirección y puerto del servidor
HOST = '127.0.0.1'
PORT = 65432
TIMEOUT = 60

# Lista para almacenar los jugadores que están esperando en la cola
player_queue = []

# Diccionario para guardar los emparejamientos entre jugadores
match_history = {}

# Esta función maneja la conexión con cada jugador
def handle_player_connection(player_socket, player_address):
    # Añadimos al jugador a la cola junto con su dirección
    print(f"Jugador conectado: {player_address}. Total de jugadores en cola: {len(player_queue)}")
    join_time = time.time()
    while True:
        if time.time() - join_time > TIMEOUT:
            print(f"{player_address} agotó su tiempo.")
            player_socket.sendall(b"No se encontro rival")
            for i in range(0, len(player_queue)):
                if player_socket is player_queue[i][0]:
                    player_queue.pop(i)
            player_socket.close()
            return
        # Revisamos si hay al menos dos jugadores en la cola para emparejarlos
        if len(player_queue) >= 2:
            # Sacamos a los dos primeros jugadores de la cola
            player1, addr1 = player_queue.pop(0)
            player2, addr2 = player_queue.pop(0)

            # Guardamos el emparejamiento en un diccionario
            match_history[addr1] = addr2
            match_history[addr2] = addr1

            # Les enviamos un mensaje para que acepten la partida
            player1.sendall("Emparejado con otro jugador.".encode("utf-8"))
            player2.sendall("Emparejado con otro jugador.".encode("utf-8"))


            # Esperamos la respuesta de ambos jugadores
            player1.close()
            player2.close()

        else:
            # Si no hay suficientes jugadores, notificamos al jugador que espere
            time.sleep(1)
            try:
                # Verificacion de desconexion
                player_socket.settimeout(1)
                data = player_socket.recv(1024)
                if not data:
                    raise ConnectionResetError
                player_socket.sendall(b"Esperando un rival...")
            except socket.timeout:
                continue  # Continuar
            except ConnectionResetError:
                for i in range(0, len(player_queue)):
                    if player_socket is player_queue[i][0]:
                        player_queue.pop(i)
                print(f"{player_address} desconectado.")
                return

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
            player_queue.append([player_socket, player_address])
            print(f"Conexión de: {player_address}")
            
            # Creamos un hilo para manejar cada conexión de jugador
            threading.Thread(target=handle_player_connection, args=(player_socket, player_address)).start()

# Inicia el servidor cuando se ejecuta este archivo
if __name__ == "__main__":
    start_server()
