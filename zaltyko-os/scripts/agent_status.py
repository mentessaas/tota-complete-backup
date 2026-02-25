#!/usr/bin/env python3
"""
Multi-Agent Status - Muestra estado visual de agentes
"""
import json
from datetime import datetime

# Estado de ejemplo (en el futuro esto viene de los agentes reales)
AGENTS = {
    "research_lead": {
        "state": "running",
        "task": "Researching academies in Madrid",
        "subagents": {
            "x_scout": {"state": "running", "task": "Finding X accounts"},
            "linkedin_scout": {"state": "idle", "task": None},
            "youtube_scout": {"state": "idle", "task": None},
            "reddit_scout": {"state": "idle", "task": None},
            "web_scout": {"state": "idle", "task": None},
            "saas_scout": {"state": "idle", "task": None},
            "gym_scout": {"state": "idle", "task": None}
        }
    },
    "trading_bot": {
        "state": "idle",
        "task": None,
        "positions": 0
    },
    "content_bot": {
        "state": "idle",
        "task": None
    }
}

def show_visual():
    print("=" * 60)
    print("🤖 MULTI-AGENT SYSTEM STATUS")
    print("=" * 60)
    print(f"Last update: {datetime.now().strftime('%H:%M:%S')}")
    print()
    
    for agent_name, agent_data in AGENTS.items():
        # Emoji según estado
        if agent_data["state"] == "running":
            emoji = "🟢"
        elif agent_data["state"] == "idle":
            emoji = "⚪"
        else:
            emoji = "🔴"
        
        print(f"{emoji} {agent_name.upper()}")
        print(f"   State: {agent_data['state']}")
        
        if agent_data.get("task"):
            print(f"   Task: {agent_data['task']}")
        
        # Subagents
        if agent_data.get("subagents"):
            print("   Subagents:")
            for sub_name, sub_data in agent_data["subagents"].items():
                if sub_data["state"] == "running":
                    sub_emoji = "🟢"
                elif sub_data["state"] == "idle":
                    sub_emoji = "⚪"
                else:
                    sub_emoji = "🔴"
                
                task = sub_data.get("task", "idle")
                print(f"      {sub_emoji} {sub_name}: {task}")
        
        print()

def get_status_json():
    return json.dumps(AGENTS, indent=2)

# CLI
import sys
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "json":
        print(get_status_json())
    else:
        show_visual()
