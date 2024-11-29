import socket

# Dirección y puerto del servidor
HOST = '127.0.0.1'
PORT = 65432

# Esta función conecta al cliente con el servidor
def connect():
    # Creamos un socket para conectarnos al servidor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))  # Conectamos al servidor en la dirección y puerto especificados

        while True:
            # Esperamos mensajes del servidor
            data = s.recv(1024)
            print(f"Recibido: {data.decode()}")

            # Si el servidor pregunta si aceptamos la partida, respondemos
            if "¿Aceptar partida?" in data.decode("utf-8"):
                response = input("¿Aceptar partida? (Y/N): ").strip().upper()
                s.sendall(response.encode())  # Enviamos la respuesta al servidor

            # Si el servidor notifica que se canceló o inicia el juego, terminamos
            if b"La cola fue cancelada por tu oponente." in data or b"Inicia el juego!" in data:
                break

# Ejecuta la conexión cuando se corre este archivo
if __name__ == "__main__":
    connect()
