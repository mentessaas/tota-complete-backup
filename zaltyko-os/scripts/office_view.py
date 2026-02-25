#!/usr/bin/env python3
"""
Office View - Visualización 2D de agentes trabajando
Estilo "oficina virtual" como en el video de Claude Code
"""
import os
import json
import time
from datetime import datetime

# Estado guardado
STATE_FILE = os.path.expanduser('~/zaltyko-os/scripts/office_state.json')

class OfficeView:
    def __init__(self):
        self.load_state()
    
    def load_state(self):
        try:
            with open(STATE_FILE, 'r') as f:
                self.state = json.load(f)
        except:
            self.state = self.get_default_state()
    
    def save_state(self):
        with open(STATE_FILE, 'w') as f:
            json.dump(self.state, f, indent=2)
    
    def get_default_state(self):
        return {
            "agents": {
                "tota": {
                    "name": "Tota",
                    "emoji": "🦊",
                    "role": "Orquestador",
                    "status": "thinking",
                    "task": "Esperando...",
                    "x": 2,
                    "y": 2
                },
                "research_lead": {
                    "name": "Research Lead",
                    "emoji": "🔍",
                    "role": "Lead Research",
                    "status": "idle",
                    "task": "",
                    "x": 1,
                    "y": 4
                },
                "x_scout": {
                    "name": "X Scout",
                    "emoji": "🐦",
                    "role": "X Researcher",
                    "status": "idle",
                    "task": "",
                    "x": 1,
                    "y": 5
                },
                "trading_bot": {
                    "name": "Trading Bot",
                    "emoji": "📈",
                    "role": "Trader",
                    "status": "idle",
                    "task": "",
                    "x": 5,
                    "y": 2
                },
                "transcriber": {
                    "name": "Transcriber",
                    "emoji": "🎬",
                    "role": "Content",
                    "status": "idle",
                    "task": "",
                    "x": 5,
                    "y": 4
                }
            },
            "log": [],
            "last_update": datetime.now().isoformat()
        }
    
    def update_agent(self, agent_id, status, task):
        """Actualizar estado de un agente"""
        if agent_id in self.state["agents"]:
            self.state["agents"][agent_id]["status"] = status
            self.state["agents"][agent_id]["task"] = task
            self.state["last_update"] = datetime.now().isoformat()
            
            # Añadir al log
            self.state["log"].append({
                "time": datetime.now().strftime("%H:%M:%S"),
                "agent": agent_id,
                "status": status,
                "task": task
            })
            
            # Keep only last 20 log entries
            self.state["log"] = self.state["log"][-20:]
            
            self.save_state()
    
    def render(self):
        """Renderizar la oficina 2D"""
        # Limpiar pantalla
        os.system('clear' if os.name == 'posix' else 'cls')
        
        print("=" * 70)
        print("🏢 OFICINA VIRTUAL - AGENTES TRABAJANDO")
        print("=" * 70)
        print(f"🕐 Actualizado: {self.state['last_update'][:19]}")
        print()
        
        # Renderizar grid 2D (8x8)
        grid = [["  " for _ in range(8)] for _ in range(8)]
        
        # Plazas de trabajo (工作站)
        stations = {
            (1, 1): "📊 RESEARCH LAB",
            (4, 1): "📈 TRADING FLOOR",
            (1, 4): "🔍 LEAD GEN",
            (4, 4): "🎬 CONTENT"
        }
        
        # Colocar agentes
        for agent_id, agent in self.state["agents"].items():
            x, y = agent["x"], agent["y"]
            
            # Emoji según estado
            if agent["status"] == "running":
                emoji = "⚡"
            elif agent["status"] == "working":
                emoji = "🔨"
            elif agent["status"] == "thinking":
                emoji = "💭"
            else:
                emoji = agent["emoji"]
            
            grid[y][x] = emoji
        
        # Imprimir grid
        print("     0    1    2    3    4    5    6    7")
        print("   +----" * 8 + "+")
        
        for y in range(8):
            row = f" {y} |"
            for x in range(8):
                cell = grid[y][x]
                if (x, y) in stations:
                    row += f" {stations[(x,y)][:3]} |"
                else:
                    row += f" {cell:^4} |"
            print(row)
            print("   +----" * 8 + "+")
        
        # Leyenda
        print("\n📋 ESTADO DE AGENTES:")
        print("-" * 50)
        
        for agent_id, agent in self.state["agents"].items():
            status_emoji = {
                "running": "🟢",
                "working": "🟡",
                "thinking": "🔵",
                "idle": "⚪",
                "error": "🔴"
            }.get(agent["status"], "⚪")
            
            task = agent["task"] if agent["task"] else "(sin tarea)"
            print(f"{status_emoji} {agent['emoji']} {agent['name']}: {task}")
        
        # Log reciente
        if self.state["log"]:
            print("\n📝 ACTIVIDAD RECIENTE:")
            print("-" * 50)
            for entry in self.state["log"][-5:]:
                print(f"  🕐 {entry['time']} - {entry['agent']}: {entry['status']} - {entry['task']}")
        
        print("\n" + "=" * 70)
        print("Presiona Ctrl+C para salir")

# CLI
def main():
    import sys
    
    office = OfficeView()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "update":
            agent = sys.argv[2]
            status = sys.argv[3] if len(sys.argv) > 3 else "working"
            task = " ".join(sys.argv[4:]) if len(sys.argv) > 4 else ""
            office.update_agent(agent, status, task)
            print(f"✅ {agent} actualizado: {status} - {task}")
        
        elif sys.argv[1] == "view":
            office.render()
        
        elif sys.argv[1] == "loop":
            # Modo loop (presiona Ctrl+C para salir)
            try:
                while True:
                    office.render()
                    time.sleep(5)
            except KeyboardInterrupt:
                print("\n👋 Oficina cerrada")
        
        elif sys.argv[1] == "demo":
            # Demo: simular agentes trabajando
            import random
            
            tasks = [
                "Buscando leads en X",
                "Analizando mercado crypto",
                "Transcribiendo video",
                "Investigando competidores",
                "Guardando datos",
                "Generando reporte"
            ]
            
            agents = list(office.state["agents"].keys())
            
            try:
                for i in range(10):
                    agent = random.choice(agents)
                    task = random.choice(tasks)
                    status = random.choice(["running", "working", "thinking"])
                    office.update_agent(agent, status, task)
                    office.render()
                    time.sleep(2)
            except KeyboardInterrupt:
                print("\n👋 Demo terminado")
    else:
        office.render()

if __name__ == "__main__":
    main()
