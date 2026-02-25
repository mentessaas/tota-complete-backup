# 🏢 Tota Office - Virtual 2D Game Plan

## Visión
Oficina virtual estilo Pokémon en 2D donde los agentes son personajes animados que tienen:
- Mesas de trabajo con computadoras
- Se mueven por la oficina
- Reuniones y conversaciones
- Chat en tiempo real
- Puedo interactuar 1:1 con cada uno

---

## Arquitectura

```
┌─────────────────────────────────────────────────────────┐
│                    FRONTEND (HTML/Canvas)              │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐ │
│  │ Office  │  │  Chat   │  │ Agent   │  │ Tasks   │ │
│  │ Canvas  │  │ Panel   │  │ Panel   │  │ Panel   │ │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘ │
└───────┼────────────┼────────────┼────────────┼───────┘
        │            │            │            │
        └────────────┴────────────┼────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │    BACKEND (Python)     │
                    │  ┌─────────────────┐    │
                    │  │ WebSocket Server │    │
                    │  │ - Estado office  │    │
                    │  │ - Movimiento     │    │
                    │  │ - Chat messages  │    │
                    │  │ - Task queue     │    │
                    │  └─────────────────┘    │
                    │  ┌─────────────────┐    │
                    │  │ Agent AI Engine │    │
                    │  │ - Responde chat │    │
                    │  │ - Ejecuta tareas│    │
                    │  │ - Estado mental │    │
                    │  └─────────────────┘    │
                    └────────────────────────┘
```

---

## Componentes

### 1. office_server.py
- WebSocket server (port 8765)
- Estado global de la oficina
- Movimiento de agentes
- Chat broadcasting
- Task management

### 2. office.html
- Canvas 2D con oficina
- Sprites de agentes
- Paneles UI (chat, tasks, details)
- WebSocket client

### 3. Agentes Definidos
| Agent | Emoji | Rol | Ubicación |
|-------|-------|-----|-----------|
| Tota | 🦊 | Orquestador | Desk 1 (principal) |
| Research Lead | 🔍 | Research | Desk 2 |
| Trading Bot | 📈 | Trading | Desk 3 |
| Transcriber | 🎬 | Content | Desk 4 |
| Risk Manager | 🛡️ | Risk | Desk 5 |

---

## Funcionalidades

### 🏢 Oficina 2D
- Fondo de oficina estilo pixel/cartoon
- 5 escritorios con computadoras
- Áreas: Meeting zone, Kitchen, Entrance
- Sprites de 32x32 o 64x64

### 🤖 Comportamiento Agentes
- Idle: en su escritorio trabajando
- Walking: moviéndose por la oficina
- Meeting: en sala de reuniones
- Chat: conversando
- Thinking: procesando tareas

### 💬 Sistema de Chat
- Chat grupal (todos ven)
- Chat 1:1 (click en agente)
- Mensajes con timestamp
- Notificaciones visuales

### 📋 Task System
- Puedo crear tareas para agentes
- Tareas aparecen como notifications
- Agentes responden cuando completan

### 🎮 Controles
- Click en agente → ver detalles + chat 1:1
- Click en área → mover agente
- Click en meeting → iniciar reunión
- Escribir en chat global o privado

---

## Fases de Desarrollo

### Fase 1: Core
- [ ] Servidor WebSocket básico
- [ ] Oficina 2D render
- [ ] Agentes con posiciones
- [ ] Movimiento básico

### Fase 2: Chat
- [ ] Panel de chat
- [ ] Mensajes en tiempo real
- [ ] Chat 1:1

### Fase 3: Interacción
- [ ] Tareas/misiones
- [ ] Estados de agente
- [ ] Detalles de agente

### Fase 4: polish
- [ ] Animaciones
- [ ] Sonidos (opcional)
- [ ] Mejoras visuales

---

## Archivos a Crear

1. `/Users/elvisvaldesinerarte/zaltyko-os/scripts/tota_office/` (directorio)
   - `server.py` - Backend
   - `static/index.html` - Frontend
   - `static/style.css` - Estilos
   - `static/game.js` - Lógica juego
   - `static/agents.json` - Datos agentes
   - `README.md` - Instrucciones

---

## Tech Stack
- Python: websockets, asyncio
- HTML5 Canvas
- Vanilla JavaScript
- No frameworks pesados

---

## Tiempo Estimado
- Fase 1-2: 30-45 min
- Fase 3: 20 min
- Fase 4: 15 min

**Total: ~1.5 horas para MVP completo**
