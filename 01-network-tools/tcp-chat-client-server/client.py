#!/usr/bin/env python3

import socket

def start_chat_client():
    host = "localhost"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        client_message = input("\n[+] Mensaje para enviar al servidor: ")
        client_message = client_message.replace("\r", "").replace("\n", "")
        client_socket.send(client_message.encode())

        if client_message == "bye":
            break

        server_message = client_socket.recv(1024).decode("utf-8", errors="ignore")
        server_message = server_message.replace("\r", "").replace("\n", "")
        print(f"[+] Mensaje del servidor: {server_message.strip()}")

    client_socket.close()

start_chat_client()

