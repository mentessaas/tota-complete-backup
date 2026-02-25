# 🏢 Tota Office - Oficina Virtual 2D

Oficina virtual estilo Pokémon donde los agentes son personajes animados con sus propias mesas de trabajo.

## Características

### 🎮 Juego 2D
- Oficina renderizada en Canvas
- 5 agentes con sprites animados
- Mesas de trabajo con computadoras
- Áreas: Reuniones, Cocina, Entrada

### 🤖 Agentes
| Agent | Rol | Descripción |
|-------|-----|-------------|
| 🦊 Tota | Orquestador | Cerebro de la operación |
| 🔍 Research Lead | Research | Investigación de mercados |
| 📈 Trading Bot | Trading | Trading automático |
| 🎬 Transcriber | Content | Transcripción de videos |
| 🛡️ Risk Manager | Risk | Gestión de riesgos |

### 💬 Sistema de Chat
- Chat global (todos ven)
- Chat directo 1:1
- Respuestas automáticas de agentes

### 📋 Tareas
- Crear tareas para agentes
- Notificaciones en tiempo real
- Seguimiento de estado

### 🎯 Interacciones
- Click en agente → Ver detalles
- Chat directo
- Invitar a reuniones
- Asignar tareas

## Instalación

```bash
cd ~/zaltyko-os/scripts/tota_office
pip3 install websockets
```

## Uso

```bash
./run.sh
```

O manualmente:

```bash
# Terminal 1: Servidor
python3 server.py

# Terminal 2: HTTP server
cd static
python3 -m http.server 8080
```

Luego abre: http://localhost:8080

## Controles

- **Click** en agente → Ver detalles
- **Chat** → Escribe y presiona Enter
- **Tabs** → Chat / Agentes / Tareas

## Arquitectura

```
tota_office/
├── server.py          # WebSocket server
├── static/
│   └── index.html    # Frontend completo
├── run.sh            # Launcher
└── README.md         # Este archivo
```

## Tech Stack

- Python 3 + websockets
- HTML5 Canvas
- Vanilla JavaScript
- Estilo retro/pixel

---
🏴‍☠️ Tota Office v1.0
