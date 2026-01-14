# 💬 TCP Chat Client-Server

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Level](https://img.shields.io/badge/Nivel-Básico-green.svg)]()
[![Status](https://img.shields.io/badge/Status-Completo-success.svg)]()

## 📋 Descripción

Implementación básica de un sistema de chat cliente-servidor utilizando **sockets TCP puros** en Python. Este proyecto demuestra los fundamentos de la programación de redes y comunicación cliente-servidor sin frameworks adicionales.

## 🎯 Objetivos de Aprendizaje

- Comprender el funcionamiento de sockets TCP/IP
- Implementar arquitectura cliente-servidor básica
- Manejar comunicación bidireccional en tiempo real
- Gestionar conexiones de red y excepciones
- Aplicar codificación UTF-8 en mensajes de red

## 🏗️ Arquitectura

```
┌─────────────┐                    ┌─────────────┐
│   CLIENT    │                    │   SERVER    │
│             │                    │             │
│  client.py  │ ◄──── TCP/IP ────► │  server.py  │
│             │    Port 12345      │             │
│ localhost   │                    │ localhost   │
└─────────────┘                    └─────────────┘
```

## 🛠️ Tecnologías Utilizadas

- **Python 3.9+**
- **Socket Library** - Comunicación de red a bajo nivel
- **Threading implícito** - Servidor single-threaded bloqueante

## 📁 Estructura del Proyecto

```
tcp-chat-client-server/
├── README.md           # Este archivo
├── server.py           # Servidor TCP que acepta conexiones
├── client.py           # Cliente TCP que se conecta al servidor
├── requirements.txt    # Dependencias (ninguna externa)
└── screenshots/        # Capturas de ejemplo (opcional)
```

## 🚀 Instalación y Uso

### Requisitos Previos

```bash
Python 3.9 o superior (sin dependencias externas)
```

### Paso 1: Clonar o descargar

```bash
git clone https://github.com/martinaresdev-web/python-offensive-security.git
cd python-offensive-security/01-network-tools/tcp-chat-client-server/
```

### Paso 2: Iniciar el Servidor

```bash
python3 server.py
```

**Salida esperada:**
```
[+] Servidor listo para aceptar una conexión...
```

### Paso 3: Iniciar el Cliente (en otra terminal)

```bash
python3 client.py
```

**Salida esperada:**
```
[+] Se ha conectado el cliente: {IP}:{Puerto}
```

### Paso 4: Chatear

**En el cliente:**
```
[*] Mensaje para enviar al servidor: Hola servidor
```

**En el servidor verás:**
```
[*] Mensaje del cliente: Hola servidor
[*] Mensaje para el cliente: Hola cliente
```

Para cerrar la conexión, escribe `bye` desde el cliente.

## 💻 Detalles Técnicos

### Servidor (`server.py`)

**Funcionalidades principales:**
- Escucha en `localhost:12345`
- Acepta **una conexión** a la vez (single-client)
- Recibe mensajes del cliente (máx. 1024 bytes)
- Envía respuestas interactivas
- Cierra conexión al recibir "bye"

**Código clave:**
```python
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
server_socket.listen(1)
```

### Cliente (`client.py`)

**Funcionalidades principales:**
- Se conecta a `localhost:12345`
- Envía mensajes interactivos al servidor
- Recibe y muestra respuestas del servidor
- Cierra conexión al escribir "bye"

**Código clave:**
```python
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
```

### Protocolo de Comunicación

| Paso | Acción | Descripción |
|------|--------|-------------|
| 1 | **Conexión** | Cliente establece conexión TCP |
| 2 | **Envío** | Cliente envía mensaje (codificado UTF-8) |
| 3 | **Recepción** | Servidor recibe y decodifica |
| 4 | **Respuesta** | Servidor envía respuesta |
| 5 | **Loop** | Se repite hasta que cliente envía "bye" |
| 6 | **Cierre** | Ambos cierran sockets |

## 🔒 Consideraciones de Seguridad

### ⚠️ Vulnerabilidades Actuales

Este es un proyecto **educativo básico** que NO incluye:

- ❌ **Cifrado** - Los mensajes viajan en texto plano
- ❌ **Autenticación** - Cualquiera puede conectarse
- ❌ **Validación de entrada** - No sanitiza mensajes
- ❌ **Concurrencia** - Solo maneja 1 cliente a la vez
- ❌ **Manejo robusto de errores** - Puede fallar con inputs inesperados

### 🛡️ Mejoras de Seguridad Sugeridas

```python
# 1. Cifrado con SSL/TLS
import ssl
context = ssl.create_default_context()

# 2. Validación de longitud de mensaje
if len(message) > MAX_LENGTH:
    raise ValueError("Mensaje demasiado largo")

# 3. Sanitización de entrada
message = re.sub(r'[^\w\s]', '', message)
```

## 🎓 Conceptos de Pentesting Aplicables

### 1. **Reconocimiento de Puertos**
```bash
# Detectar si el servidor está activo
nmap -p 12345 localhost
```

### 2. **Captura de Tráfico**
```bash
# Ver mensajes en texto plano con tcpdump
sudo tcpdump -i lo -A 'tcp port 12345'
```

### 3. **Man-in-the-Middle (MITM)**
- Al no tener cifrado, es vulnerable a interceptación
- Uso educativo: Comprender por qué TLS/SSL es necesario

### 4. **Ataques de Denegación de Servicio (DoS)**
```python
# Ejemplo conceptual: Saturar el servidor
while True:
    client = socket.socket()
    client.connect(('localhost', 12345))
    # Sin cerrar conexiones previas
```

## 📚 Aprendizajes Clave

✅ **Sockets TCP/IP** - Fundamentos de comunicación de red  
✅ **Cliente-Servidor** - Arquitectura básica de sistemas distribuidos  
✅ **Codificación** - Manejo de encoding UTF-8 en red  
✅ **Excepciones** - `KeyboardInterrupt` para cierre limpio  
✅ **Bloques try-finally** - Asegurar cierre de recursos  

## 🚧 Limitaciones y Mejoras Futuras

### Limitaciones Actuales
- Solo soporta 1 cliente simultáneo
- Sin historial de mensajes
- Sin interfaz gráfica
- Comunicación no cifrada

### Roadmap de Mejoras
- [ ] Soporte multi-cliente con threading
- [ ] Implementar cifrado TLS/SSL
- [ ] Añadir autenticación de usuarios
- [ ] Sistema de salas de chat
- [ ] Interfaz GUI con tkinter
- [ ] Logs de conversaciones
- [ ] Soporte para envío de archivos

## 🔗 Relación con Otros Proyectos

Este proyecto es la **base** para herramientas más avanzadas:

- **Port Scanner** - Uso de sockets para detección de puertos
- **Reverse Shell** - Comunicación remota cliente-servidor
- **Packet Sniffer** - Análisis de tráfico TCP

## 📖 Referencias y Recursos

- [Python Socket Documentation](https://docs.python.org/3/library/socket.html)
- [TCP/IP Protocol Suite](https://en.wikipedia.org/wiki/Internet_protocol_suite)
- [Network Programming in Python](https://realpython.com/python-sockets/)

## ⚖️ Disclaimer

Este código es para **fines educativos** únicamente. No usar en entornos de producción sin implementar medidas de seguridad apropiadas (cifrado, autenticación, validación).

## 👨‍💻 Autor

Desarrollado como parte del curso **Python Ofensivo (Hack4u)** y el **Master en Ciberseguridad Zero Day (EDIBS)**.

---

**¿Preguntas o sugerencias?** Abre un issue en el [repositorio principal](https://github.com/TU-USUARIO/python-offensive-security).
