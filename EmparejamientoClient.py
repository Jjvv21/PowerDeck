import socket

# Dirección y puerto del servidor
HOST = '127.0.0.1'
PORT = 65432

# Conectar al servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    while True:
        data = s.recv(1024)
        print(f"Recibido: {data.decode()}")
        if data == b"Emparejado con el bot." or data == b"Jugador emparejado con otro jugador. Inicia el juego!":
            break
