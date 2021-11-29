##################################################################
# SOCKETSERV.PY --------------------------------------------------
#
# Se declara la clase MyTCPHandler donde por el metodo handle
# se actua sobre los paquetes recibidos en bytes y se los guarda
# o presenta como string
#
# En caso de ejecutarlo como main:
# Se abre un socket en modo TCP en puerto y host indicados
# se instancia el server y se queda escuchando hasta que sea
# terminado, no es necesario el server.kill al implementar el with
##################################################################

from genericpath import exists
import socketserver
from binascii import hexlify
# from controlador import log_socios

# def log_registro_socket(obj):
#     def interior(*args, **kwargs):
#         log_socios.registrar("socket", "cliente")
#         obj(*args, **kwargs)

#     return interior


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    # @log_registro_socket
    def handle(self):
        # self.request is the TCP socket connected to the client
        data = self.request.recv(1024).strip()
        # self.data = self.request.recv(1024).strip()
        binarios = bytearray(data)
        print("Nuevo mensaje desde {}".format(self.client_address[0]))
        print(hexlify(binarios).decode("utf-8"))

        # print("{} wrote:".format(self.client_address[0]))
        # print(self.data)
        # just send back the same data, but upper-cased
        respuesta = 0xF3
        data = bytearray(respuesta.to_bytes(2, "big"))
        self.request.sendall(data)
        # self.request.sendall(data.upper())


if __name__ == "__main__":
    try:
        HOST, PORT = "localhost", 9999
        # with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
        print("/*--- Iniciamos el Server ---*/")
        server.serve_forever()
        print("/*---Server Terminado---*/")
        server.server_close()
        # server.kill()
    except:
        # Atrapamos el error
        if exists(server):
            server.kill()
        print("_🔥 🔥 🔥_ Ha ocurrido un ERROR _🔥_🔥_🔥_")
