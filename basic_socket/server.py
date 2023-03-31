import socket

host = socket.gethostname() # Esta función nos da el nombre de la máquina
port = 12345
BUFFER_SIZE = 1024 # Usamos un número pequeño para tener una respuesta rápida 
print("Iniciando...")
'''Los objetos socket soportan el context manager type
así que podemos usarlo con una sentencia with, no hay necesidad
de llamar a socket_close()
'''
# Creamos un objeto socket tipo TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
    print("Iniciando2 ...", "host" , port)

    socket_tcp.bind(("localhost", port)) 
    socket_tcp.listen(5) # Esperamos la conexión del cliente 
    conn, addr = socket_tcp.accept() # Establecemos la conexión con el cliente 
    with conn:
        print('[*] Conexión establecida') 
        while True:
            # Recibimos bytes, convertimos en str
            data = conn.recv(BUFFER_SIZE)
            print("cliente dice:", data)
            # Verificamos que hemos recibido datos
            if not data:
                break
            else:
                print('[*] Datos recibidos: {}'.format(data.decode('utf-8'))) 
            conn.send("Hola cliente!  Desde el servidor".encode('utf-8')) # Hacemos echo convirtiendo de nuevo a bytes