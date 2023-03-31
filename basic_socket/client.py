import socket

# El cliente debe tener las mismas especificaciones del servidor
host = "localhost" #socket.gethostname()
port = 12345
BUFFER_SIZE = 1024
MESSAGE = 'Hola, mundo! Desde cliente' # Datos que queremos enviar

# usamos with para trabajar con archivos externos  o conexiones de red
# estos serán liberados explicitamente despues de su uso para evitar posibles fugas de memoria
# with [recurso] as alias:
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
    socket_tcp.connect((host, port)) # Nos conectamos al servidor
    # Convertimos str a bytes
    socket_tcp.send(MESSAGE.encode('utf-8'))
    data = socket_tcp.recv(BUFFER_SIZE) # recibimos respuesta dle server
    print("Servidor dice:", data)