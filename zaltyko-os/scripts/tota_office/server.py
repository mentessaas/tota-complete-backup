#!/usr/bin/env python3
"""
Tota Office - Servidor de la Oficina Virtual
WebSocket server para tiempo real
"""

import asyncio
import json
import random
import uuid
from datetime import datetime
from pathlib import Path
from websockets.server import serve, WebSocketServerProtocol
from typing import Set, Dict, Any

# Configuración
PORT = 8765
OFFICE_WIDTH = 800
OFFICE_HEIGHT = 600


# Estado de la oficina
class OfficeState:
    def __init__(self):
        self.clients: Set[WebSocketServerProtocol] = set()
        self.agents: Dict[str, Any] = {}
        self.messages: list = []
        self.tasks: Dict[str, Any] = {}
        self.init_agents()

    def init_agents(self):
        """Inicializar agentes"""
        self.agents = {
            "tota": {
                "id": "tota",
                "name": "Tota",
                "emoji": "🦊",
                "role": "Orquestador",
                "x": 100,
                "y": 300,
                "desk_x": 80,
                "desk_y": 280,
                "status": "idle",
                "energy": 100,
                "task": "Esperando instrucciones...",
                "color": "#ff9500",
                "description": "Cerebro de la operación. Puedo ayudarte con cualquier cosa.",
                "skills": ["research", "trading", "memoria", "ejecución"],
                "mood": "😊",
            },
            "research_lead": {
                "id": "research_lead",
                "name": "Research Lead",
                "emoji": "🔍",
                "role": "Research",
                "x": 250,
                "y": 300,
                "desk_x": 230,
                "desk_y": 280,
                "status": "idle",
                "energy": 100,
                "task": "Buscando leads...",
                "color": "#58a6ff",
                "description": "Especialista en investigación de mercados y leads.",
                "skills": ["x_scout", "linkedin_scout", "youtube_scout"],
                "mood": "😊",
            },
            "trading_bot": {
                "id": "trading_bot",
                "name": "Trading Bot",
                "emoji": "📈",
                "role": "Trading",
                "x": 400,
                "y": 300,
                "desk_x": 380,
                "desk_y": 280,
                "status": "idle",
                "energy": 100,
                "task": "Analizando mercados...",
                "color": "#3fb950",
                "description": "Bot de trading automático. Analiza y ejecuta operaciones.",
                "skills": ["analisis", "ejecución", "riesgo"],
                "mood": "😊",
            },
            "transcriber": {
                "id": "transcriber",
                "name": "Transcriber",
                "emoji": "🎬",
                "role": "Content",
                "x": 550,
                "y": 300,
                "desk_x": 530,
                "desk_y": 280,
                "status": "idle",
                "energy": 100,
                "task": "Transcribiendo videos...",
                "color": "#bc8cff",
                "description": "Transcribe videos de YouTube automáticamente.",
                "skills": ["transcripcion", "resumenes", "youtube"],
                "mood": "😊",
            },
            "risk_manager": {
                "id": "risk_manager",
                "name": "Risk Manager",
                "emoji": "🛡️",
                "role": "Risk",
                "x": 700,
                "y": 300,
                "desk_x": 680,
                "desk_y": 280,
                "status": "idle",
                "energy": 100,
                "task": "Monitoreando riesgos...",
                "color": "#f85149",
                "description": "Gestiona riesgos y límites de trading.",
                "skills": ["riesgo", "límites", "alertas"],
                "mood": "😊",
            },
        }

        # Áreas de la oficina
        self.areas = {
            "desk_1": {"x": 80, "y": 280, "name": "Escritorio Tota", "type": "desk"},
            "desk_2": {
                "x": 230,
                "y": 280,
                "name": "Escritorio Research",
                "type": "desk",
            },
            "desk_3": {
                "x": 380,
                "y": 280,
                "name": "Escritorio Trading",
                "type": "desk",
            },
            "desk_4": {
                "x": 530,
                "y": 280,
                "name": "Escritorio Content",
                "type": "desk",
            },
            "desk_5": {"x": 680, "y": 280, "name": "Escritorio Risk", "type": "desk"},
            "meeting": {
                "x": 400,
                "y": 100,
                "name": "Sala Reuniones",
                "type": "meeting",
            },
            "kitchen": {"x": 720, "y": 450, "name": "Cocina", "type": "kitchen"},
            "entrance": {"x": 50, "y": 500, "name": "Entrada", "type": "entrance"},
        }

    def get_state(self) -> Dict:
        """Obtener estado completo"""
        return {
            "agents": self.agents,
            "areas": self.areas,
            "messages": self.messages[-50:],  # últimos 50 mensajes
            "tasks": self.tasks,
            "timestamp": datetime.now().isoformat(),
        }

    def move_agent(self, agent_id: str, target_x: int, target_y: int) -> bool:
        """Mover agente a posición"""
        if agent_id not in self.agents:
            return False

        agent = self.agents[agent_id]
        agent["target_x"] = target_x
        agent["target_y"] = target_y
        agent["status"] = "walking"

        # Reducir energía al caminar
        if agent["energy"] > 10:
            agent["energy"] = max(10, agent["energy"] - 2)

        return True

    def add_message(self, sender: str, text: str, recipient: str = None):
        """Añadir mensaje"""
        msg = {
            "id": str(uuid.uuid4()),
            "sender": sender,
            "text": text,
            "recipient": recipient,
            "timestamp": datetime.now().isoformat(),
        }
        self.messages.append(msg)

        # Simular respuesta del agente
        if sender == "user":
            self.simulate_agent_response(text, recipient)

        return msg

    def simulate_agent_response(self, text: str, recipient: str = None):
        """Simular respuesta de agente"""
        # Si es mensaje directo a un agente
        if recipient and recipient in self.agents:
            agent = self.agents[recipient]
            responses = self.get_agent_responses(agent["role"], text)

            # Añadir respuesta del agente después de un delay
            asyncio.create_task(
                self.delayed_response(agent["id"], random.choice(responses))
            )

    async def delayed_response(self, agent_id: str, text: str):
        """Respuesta con delay"""
        await asyncio.sleep(random.uniform(1, 3))

        agent = self.agents.get(agent_id)
        if agent:
            # Añadir mensaje del agente
            msg = {
                "id": str(uuid.uuid4()),
                "sender": agent_id,
                "sender_name": agent["name"],
                "text": text,
                "recipient": "user",
                "timestamp": datetime.now().isoformat(),
            }
            self.messages.append(msg)

            # Broadcast
            await self.broadcast({"type": "message", "data": msg})

            # Actualizar estado del agente - recuperar energía
            agent["status"] = "idle"
            agent["energy"] = min(100, agent.get("energy", 100) + 10)
            agent["mood"] = "😊"
            agent["task"] = random.choice(
                ["Trabajando...", "Analizando...", "Investigando...", "Monitoreando..."]
            )
            await self.broadcast({"type": "agent_update", "data": agent})

    def get_agent_responses(self, role: str, text: str) -> list:
        """Respuestas por rol"""
        text_lower = text.lower()

        responses = {
            "Orquestador": [
                "Entendido. Lo proceso ahora.",
                "Buena idea. Lo añado a la cola.",
                "正在处理... (Procesando)",
                "Perfecto, me pongo con ello.",
                "Ahora te confirmo los resultados.",
            ],
            "Research": [
                "Voy a investigar eso.",
                "Buscando información relevante...",
                "Analizando datos...",
                "Encontré información interesante.",
                "Preparando informe...",
            ],
            "Trading": [
                "Analizando mercado...",
                "Buscando señales de trading...",
                "Verificando precios...",
                "Condiciones actuales: neutrales",
                "Ejecutando análisis técnico...",
            ],
            "Content": [
                "Procesando video...",
                "Extrayendo transcripción...",
                "Generando resumen...",
                "Listo, tienes el contenido.",
                "Analizando contenido...",
            ],
            "Risk": [
                "Verificando límites de riesgo...",
                "Exposición actual: dentro de parámetros.",
                "Alertas activas: ninguna.",
                "Monitoreando continuamente...",
                "Todo bajo control.",
            ],
        }

        return responses.get(role, ["Entendido."])

    async def broadcast(self, message: dict):
        """Broadcast a todos los clientes"""
        if self.clients:
            await asyncio.gather(
                *[client.send(json.dumps(message)) for client in self.clients],
                return_exceptions=True,
            )


# Instancia global
office = OfficeState()


async def handle_client(websocket: WebSocketServerProtocol):
    """Manejar cliente WebSocket"""
    office.clients.add(websocket)
    print(f"Cliente conectado. Total: {len(office.clients)}")

    try:
        # Enviar estado inicial
        await websocket.send(json.dumps({"type": "init", "data": office.get_state()}))

        # Broadcast nuevo cliente
        await office.broadcast(
            {"type": "system", "text": "🦊 Un nuevo usuario se ha unido a la oficina."}
        )

        async for message_raw in websocket:
            try:
                message = json.loads(message_raw)
                msg_type = message.get("type")
                data = message.get("data", {})

                if msg_type == "ping":
                    await websocket.send(json.dumps({"type": "pong"}))

                elif msg_type == "move":
                    agent_id = data.get("agent_id")
                    x = data.get("x")
                    y = data.get("y")
                    if office.move_agent(agent_id, x, y):
                        await office.broadcast(
                            {
                                "type": "agent_move",
                                "data": {"agent_id": agent_id, "x": x, "y": y},
                            }
                        )

                elif msg_type == "message":
                    sender = data.get("sender", "user")
                    text = data.get("text", "")
                    recipient = data.get("recipient")

                    msg = office.add_message(sender, text, recipient)

                    await office.broadcast({"type": "message", "data": msg})

                elif msg_type == "task":
                    task_id = str(uuid.uuid4())
                    task = {
                        "id": task_id,
                        "title": data.get("title", ""),
                        "description": data.get("description", ""),
                        "assignee": data.get("assignee"),
                        "status": "pending",
                        "created": datetime.now().isoformat(),
                    }
                    office.tasks[task_id] = task

                    # Notificar al agente asignado
                    if task["assignee"] in office.agents:
                        agent = office.agents[task["assignee"]]
                        agent["task"] = f"📋 {task['title']}"
                        agent["status"] = "working"
                        # Consumir energía al trabajar
                        agent["energy"] = max(20, agent.get("energy", 100) - 15)
                        agent["mood"] = "🧐"

                        await office.broadcast({"type": "agent_update", "data": agent})

                    await office.broadcast({"type": "task_created", "data": task})

                elif msg_type == "interact":
                    # Interactuar con agente
                    agent_id = data.get("agent_id")
                    if agent_id in office.agents:
                        agent = office.agents[agent_id]
                        await websocket.send(
                            json.dumps({"type": "agent_details", "data": agent})
                        )

                elif msg_type == "meet":
                    # Mover a sala de reuniones
                    agent_id = data.get("agent_id")
                    meeting = office.areas["meeting"]
                    if office.move_agent(agent_id, meeting["x"], meeting["y"]):
                        await office.broadcast(
                            {
                                "type": "agent_move",
                                "data": {
                                    "agent_id": agent_id,
                                    "x": meeting["x"],
                                    "y": meeting["y"],
                                },
                            }
                        )
                        await office.broadcast(
                            {
                                "type": "system",
                                "text": f"🤝 {office.agents[agent_id]['name']} se ha unido a la reunión.",
                            }
                        )

            except json.JSONDecodeError:
                print("Mensaje inválido recibido")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        office.clients.remove(websocket)
        print(f"Cliente desconectado. Total: {len(office.clients)}")


async def main():
    """Iniciar servidor"""
    print(f"""
🏢 TOTA OFFICE SERVER
=====================
🌐 http://localhost:{PORT}
📡 WebSocket: ws://localhost:{PORT}

Presiona Ctrl+C para detener.
    """)

    async with serve(handle_client, "localhost", PORT):
        print("✅ Servidor iniciado!")

        # Simular movimiento aleatorio de agentes
        while True:
            await asyncio.sleep(random.uniform(5, 15))

            # Elegir agente aleatorio
            agent_ids = list(office.agents.keys())
            agent_id = random.choice(agent_ids)
            agent = office.agents[agent_id]

            # Solo mover si está idle
            if agent["status"] == "idle" and random.random() < 0.3:
                # Mover a área aleatoria
                areas = list(office.areas.values())
                area = random.choice(areas)

                office.move_agent(agent_id, area["x"], area["y"])

                await office.broadcast(
                    {
                        "type": "agent_move",
                        "data": {"agent_id": agent_id, "x": area["x"], "y": area["y"]},
                    }
                )

                # Después de un tiempo, volver al desk
                await asyncio.sleep(random.uniform(3, 8))

                office.move_agent(agent_id, agent["desk_x"], agent["desk_y"])

                await office.broadcast(
                    {
                        "type": "agent_move",
                        "data": {
                            "agent_id": agent_id,
                            "x": agent["desk_x"],
                            "y": agent["desk_y"],
                        },
                    }
                )


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Servidor detenido.")
