#!/usr/bin/env python3

import socket
import sys

def start_chat_server():
    host = "localhost"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("[+] Servidor listo para aceptar una conexion...")
    connection, client_addr = server_socket.accept()
    print(f"[+] Se ha conectado el cliente: {client_addr} + {connection}")

    try:
        while True:
            client_message = connection.recv(1024).decode("utf-8", errors="ignore")
            client_message = client_message.replace("\r", "").replace("\n", "")
            print(f"[+] Mensaje del cliente: {client_message}")

            if client_message == "bye":
                break

            sys.stdout.write("\n[+] Mensaje para el cliente: ")
            sys.stdout.flush()
            server_message = sys.stdin.readline().rstrip('\r\n')
            
            if server_message:
                connection.sendall(server_message.encode("utf-8"))
    
    except KeyboardInterrupt:
        print("\n[!] Cerrando servidor...")
    finally:
        connection.close()
        server_socket.close()

start_chat_server()
