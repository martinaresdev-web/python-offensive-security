# 🐍 Python Offensive Security

[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

[English Version](README_EN.md) | Versión en Español

## 📋 Descripción

Repositorio dedicado al desarrollo de herramientas y scripts de seguridad ofensiva utilizando Python. Este proyecto forma parte de mi formación continua en ciberseguridad, incluyendo el **Master Zero Day (EDIBS)** y el curso **Python Ofensivo (Hack4u)**.

> ⚠️ **Aviso Legal**: Estas herramientas están diseñadas exclusivamente para fines educativos, de investigación en seguridad y pruebas autorizadas. El uso indebido de estas herramientas puede ser ilegal. El autor no se hace responsable del mal uso de este código.

## 🎯 Objetivos del Proyecto

- Desarrollar herramientas de pentesting desde cero
- Aplicar conceptos avanzados de Python en seguridad ofensiva
- Documentar técnicas y metodologías de ethical hacking
- Crear un portafolio técnico demostrable

## 🗂️ Estructura del Repositorio

```
python-offensive-security/
├── 01-network-tools/          # Herramientas de red y análisis
│   ├── tcp-chat-client-server/
│   ├── port-scanner/
│   └── packet-sniffer/
├── 02-web-exploitation/       # Explotación de aplicaciones web
│   ├── sql-injection-scanner/
│   └── directory-bruteforcer/
├── 03-system-tools/           # Herramientas de sistema
│   ├── keylogger-ethical/
│   └── process-injector/
├── 04-cryptography/           # Criptografía y cifrado
│   ├── cipher-tools/
│   └── password-cracker/
└── docs/                      # Documentación adicional
    ├── methodologies/
    └── cheatsheets/
```

## 🛠️ Herramientas Disponibles

### 🌐 Network Tools
| Herramienta | Descripción | Nivel | Estado |
|------------|-------------|-------|--------|
| [TCP Chat](01-network-tools/tcp-chat-client-server/) | Cliente/Servidor chat TCP puro | 🟢 Básico | ✅ Completo |
| Port Scanner | Escáner de puertos multi-hilo | 🟡 Intermedio | 🚧 En desarrollo |
| Packet Sniffer | Captura y análisis de paquetes | 🔴 Avanzado | 📋 Planificado |

### 🌍 Web Exploitation
| Herramienta | Descripción | Nivel | Estado |
|------------|-------------|-------|--------|
| SQL Injection Scanner | Detección automática de SQLi | 🟡 Intermedio | 📋 Planificado |
| Directory Bruteforcer | Fuerza bruta de directorios web | 🟢 Básico | 📋 Planificado |

## 🚀 Inicio Rápido

### Requisitos Previos

```bash
Python 3.9 o superior
pip (gestor de paquetes de Python)
Virtualenv (recomendado)
```

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/martinaresdev-web/python-offensive-security.git
cd python-offensive-security

# Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias globales
pip install -r requirements.txt
```

### Uso de Herramientas Individuales

Cada herramienta tiene su propia documentación y requisitos:

```bash
# Ejemplo: TCP Chat
cd 01-network-tools/tcp-chat-client-server/
pip install -r requirements.txt
python server.py
```

Consulta el README específico de cada proyecto para instrucciones detalladas.

## 📚 Conocimientos Aplicados

Este repositorio implementa conceptos de:

- **Networking**: Sockets TCP/UDP, protocolos de red, análisis de tráfico
- **Seguridad Web**: OWASP Top 10, inyecciones, XSS, CSRF
- **Criptografía**: Cifrado simétrico/asimétrico, hashing, PKI
- **Sistemas Operativos**: Procesos, hilos, permisos, syscalls
- **Python Avanzado**: Concurrencia, programación de red, ctypes, scapy

## 🎓 Formación Relacionada

- **Master en Ciberseguridad Zero Day** - EDIBS (En curso)
- **Python Ofensivo** - Hack4u (Completado)
- **Ingeniería Informática** - Universidad de Vigo (En curso)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add: AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

Lee [CONTRIBUTING.md](CONTRIBUTING.md) para más detalles.

## 📖 Documentación Adicional

- [Guía de Estilo de Código](docs/CODE_STYLE.md)
- [Metodologías de Pentesting](docs/methodologies/)
- [Cheatsheets de Python](docs/cheatsheets/)

## ⚖️ Consideraciones Éticas y Legales

- ✅ Usar **SOLO** en entornos autorizados y controlados
- ✅ Obtener **permiso explícito por escrito** antes de realizar pruebas
- ✅ Respetar las leyes locales e internacionales
- ❌ **NO** usar contra sistemas sin autorización
- ❌ **NO** utilizar para actividades maliciosas

## 📜 Licencia

Este proyecto está bajo la Licencia MIT. Ver [LICENSE](LICENSE) para más detalles.

## 📬 Contacto

**Martín Ares**

- LinkedIn: https://www.linkedin.com/in/martinaresalvarez/
- Email: martinares.dev@gmail.com
- GitHub: @martinaresdev-web (https://github.com/martinaresdev-web)

---

⭐ Si este proyecto te resulta útil, ¡dale una estrella en GitHub!

**Disclaimer**: El autor de este repositorio no se hace responsable del uso indebido de las herramientas aquí proporcionadas. Estas se ofrecen con fines puramente educativos y de investigación en seguridad autorizada.
