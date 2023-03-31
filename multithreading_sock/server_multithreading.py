import socket
import threading

def process_client(client_socket, client_address):
    client_socket.send(f"Hola desde el servidor para el cliente {client_address}".encode("utf-8"))
    client_socket.close()

def start_server():
    host = 'localhost'
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Servidor iniciado en {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Conexión recibida de {client_address[0]}:{client_address[1]}")
        client_thread = threading.Thread(target=process_client, args=(client_socket, client_address))
        client_thread.start()

# con esto le indicamos si el archivo actual está ejecutandose como un programa principal
# __name__ es una variable especial, se estable con __main__ si este se ejecuta como programa main
# en caso de que se importe como modulo en otro programa, se establece el nombre del modulo.
if __name__ == '__main__':
    start_server()