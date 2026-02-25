#!/usr/bin/env python3
"""
Decision Logger - Guarda decisiones importantes inmediatamente
Usage: python3 decision_log.py "decisión" "contexto"
"""
import sys
import os
from datetime import datetime

MEMORY_FILE = os.path.expanduser("~/.openclaw/workspace/MEMORY.md")
ERRORS_FILE = os.path.expanduser("~/.openclaw/workspace/memory/errors.md")

def log_decision(decision, context=""):
    """Guarda una decisión en MEMORY.md"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    entry = f"\n### {timestamp}\n- **Decisión**: {decision}\n"
    if context:
        entry += f"  - Contexto: {context}\n"
    entry += f"  - Tag: #decision\n"
    
    # Read current file
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as f:
            content = f.read()
    else:
        content = "# MEMORY.md\n"
    
    # Insert after last ### or at top
    if "### " in content:
        parts = content.split("### ")
        # Find last actual entry (not the header)
        new_content = parts[0] + "### " + f"{timestamp}\n- **Decisión**: {decision}\n" + "### ".join(parts[1:])
    else:
        new_content = content + entry
    
    with open(MEMORY_FILE, 'w') as f:
        f.write(new_content)
    
    print(f"✅ Decisión guardada: {decision}")

def log_error(error, solution, prevention=""):
    """Guarda un error en errors.md"""
    timestamp = datetime.now().strftime("%Y-%m-%d")
    
    entry = f"""
### {timestamp}
- **Error**: {error}
  - Solución: {solution}
"""
    if prevention:
        entry += f"  - Prevention: {prevention}\n"
    
    if os.path.exists(ERRORS_FILE):
        with open(ERRORS_FILE, 'r') as f:
            content = f.read()
    else:
        content = "# Errors & Solutions\n"
    
    content += entry
    
    with open(ERRORS_FILE, 'w') as f:
        f.write(content)
    
    print(f"✅ Error guardado: {error}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    decision = sys.argv[1]
    context = sys.argv[2] if len(sys.argv) > 2 else ""
    
    log_decision(decision, context)
