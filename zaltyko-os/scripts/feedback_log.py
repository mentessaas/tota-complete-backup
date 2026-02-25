#!/usr/bin/env python3
"""
Feedback Logger - Registra resultados de acciones
Usage: python3 feedback_log.py <type> <result> <details>
Types: trade, email, lead, job
Result: success, failure, partial
"""
import sys
import json
import os
from datetime import datetime

BASE_DIR = os.path.expanduser("~/zaltyko-os/feedback")

TYPES = {
    "trade": "trades",
    "email": "emails", 
    "lead": "leads",
    "job": "jobs"
}

def log_feedback(type_name, result, details, tags=None):
    if type_name not in TYPES:
        print(f"Unknown type: {type_name}")
        return
    
    folder = f"{BASE_DIR}/{TYPES[type_name]}"
    os.makedirs(folder, exist_ok=True)
    
    entry = {
        "timestamp": datetime.now().isoformat(),
        "type": type_name,
        "result": result,  # success, failure, partial
        "details": details,
        "tags": tags or []
    }
    
    filename = f"{folder}/{datetime.now().strftime('%Y%m%d')}.jsonl"
    with open(filename, "a") as f:
        f.write(json.dumps(entry) + "\n")
    
    print(f"✅ Logged: {type_name} -> {result}")
    return entry

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)
    
    log_feedback(sys.argv[1], sys.argv[2], sys.argv[3])
