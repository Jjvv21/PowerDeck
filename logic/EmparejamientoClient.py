import socket
import threading

class Client:
# Dirección y puerto del servidor
    HOST = '127.0.0.1'
    PORT = 65432
    looking = True
    result = ""

    # Esta función conecta al cliente con el servidor
    def connect(self):
        # Creamos un socket para conectarnos al servidor
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))  # Conectamos al servidor en la dirección y puerto especificados

            self.looking = True
            self.result = ""
            print("Buscando rival")

            threading.Thread(target=self.listen_to_server, args=(s,)).start()

            try:
                while True:
                    # Keep the client running
                    if not self.looking:
                        s.close()
                        print("Busqueda cancelada")
                        return "Busqueda cancelada"
                    if self.result == "Emparejado con otro jugador." or self.result == "No se encontro rival":
                        return self.result
            except KeyboardInterrupt:
                s.close()
                print("Conexión terminada")
                return "Conexión terminada"

    def listen_to_server(self, sock):
        while self.looking:
            try:
                data = sock.recv(1024)
                if not data:
                    print("Desconectado")
                    break
                print(f"Server: {data.decode()}")
                self.result = data.decode()
            except ConnectionResetError:
                print("El server cerró la conexión")
                break
    
    def cancel_search(self):
        self.looking = False
