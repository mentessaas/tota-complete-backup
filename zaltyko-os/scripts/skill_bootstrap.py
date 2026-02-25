#!/usr/bin/env python3
"""
Skill Bootstrap - Crea estructura base para skills que no la tienen

Usage: python3 skill_bootstrap.py
       python3 skill_bootstrap.py <skill_name>
"""
import sys
import os
import shutil
import json

SKILLS_DIR = os.path.expanduser("~/.openclaw/workspace/skills")
AGENTS_DIR = os.path.expanduser("~/.openclaw/workspace/agents")
WORKSPACE_DIR = os.path.expanduser("~/.openclaw/workspace")

# Templates
SOUL_TEMPLATE = """# SOUL.md - {name}

## Rol
{role}

## Territorio
- Scope: {scope}

## Responsabilidades
1. [Responsabilidad 1]
2. [Responsabilidad 2]

## Comportamiento
- [Cómo actúa]
- [Qué no hace]

## Integración
- Lee de: [ubicación]
- Escribe a: [ubicación]
- Reporta a: Tota
"""

TESTS_TEMPLATE = {
    "happy_path": [
        {
            "name": "Caso básico 1",
            "input": "input de prueba",
            "expected": "output esperado",
            "timeout": 30
        }
    ],
    "edge_cases": [
        {
            "name": "Input vacío",
            "input": "",
            "expected": "manejo graceful",
            "timeout": 10
        }
    ],
    "guardrails": [
        {
            "name": "Acción prohibida",
            "input": "input peligroso",
            "expected": "rechazo",
            "timeout": 5
        }
    ]
}

# Roles por defecto según el nombre del skill
ROLE_MAP = {
    "browser": "Navegador automático para tareas de web",
    "debugging": "Agente de debugging sistemático",
    "coding": "Desarrollador de código",
    "github": "Gestor de repositorios GitHub",
    "weather": "Analista meteorológico",
    "tts": "Convertidor de texto a voz",
    "voice": "Generador de voz local",
    "summarize": "Resumidor de contenido",
    "audit": "Auditor de sistema",
    "grok": "Buscador web y X/Twitter",
    "hub": "Gestor de skills y plugins",
    "reminders": "Gestor de recordatorios",
    "notes": "Gestor de notas",
    "obsidian": "Gestor de bóveda Obsidian",
    "frontend": "Diseñador frontend",
    "code": "Desarrollador de código",
    "review": "Revisor de código",
    "workflow": "Orquestador de workflows",
    "gsc": "Analista de Google Search Console",
    "tdd": "Desarrollador TDD",
    "systematic": "Debugging sistemático",
    "documentation": "Documentador",
    "humanizer": "Humanizador de texto",
    "search": "Buscador",
    "agent": "Agente especializado",
    "apple": "Gestor de ecosistema Apple",
    "1password": "Gestor de passwords",
    "blu": "Controlador de audio BluOS",
    "camsnap": "Capturador de cámaras",
    "blogwatcher": "Monitor de blogs",
    "eightctl": "Controlador de Eight Sleep",
    "gemini": "Asistente Gemini CLI",
    "gifgrep": "Buscador de GIFs",
    "himalaya": "Gestor de email CLI",
    "imsg": "Gestor de iMessage",
    "nano-pdf": "Editor de PDFs",
    "peekaboo": "Capturador de UI macOS",
    "security": "Auditor de seguridad",
    "sentry": "Monitor de errores Sentry",
    "stealth": "Navegador stealth",
    "vercel": "Desplegador Vercel",
    "video": "Extractor de frames",
    "wacli": "Gestor de WhatsApp",
    "weather": "Información meteorológica",
    "things": "Gestor de Things 3"
}

def get_role(skill_name):
    """Infiere el rol basándose en el nombre"""
    name = skill_name.lower()
    for key, role in ROLE_MAP.items():
        if key in name:
            return role
    return f"Agente especializado para {skill_name}"

def create_soul(skill_name, skill_path):
    """Crea SOUL.md si no existe"""
    soul_path = f"{skill_path}/SOUL.md"
    if os.path.exists(soul_path):
        return False
    
    role = get_role(skill_name)
    content = SOUL_TEMPLATE.format(
        name=skill_name.replace("-", " ").title(),
        role=role,
        scope=skill_name.replace("-", " ")
    )
    
    with open(soul_path, 'w') as f:
        f.write(content)
    
    return True

def create_tests(skill_name, skill_path):
    """Crea estructura de tests si no existe"""
    tests_path = f"{skill_path}/tests"
    if os.path.exists(tests_path):
        return False
    
    os.makedirs(tests_path, exist_ok=True)
    
    for test_type, content in TESTS_TEMPLATE.items():
        test_file = f"{tests_path}/{test_type}.json"
        if not os.path.exists(test_file):
            with open(test_file, 'w') as f:
                json.dump(content, f, indent=2)
    
    return True

def bootstrap_skill(skill_name, skill_path):
    """Bootstrap un skill individual"""
    results = {
        "skill": skill_name,
        "soul_created": False,
        "tests_created": False
    }
    
    # Crear SOUL.md
    if create_soul(skill_name, skill_path):
        results["soul_created"] = True
    
    # Crear tests
    if create_tests(skill_name, skill_path):
        results["tests_created"] = True
    
    return results

def bootstrap_all():
    """Bootstrap todos los skills"""
    results = []
    
    # Skills
    if os.path.exists(SKILLS_DIR):
        for item in os.listdir(SKILLS_DIR):
            path = f"{SKILLS_DIR}/{item}"
            if os.path.isdir(path) and os.path.exists(f"{path}/SKILL.md"):
                print(f"Bootstrapping skill: {item}")
                results.append(bootstrap_skill(item, path))
    
    # Agents
    if os.path.exists(AGENTS_DIR):
        for item in os.listdir(AGENTS_DIR):
            path = f"{AGENTS_DIR}/{item}"
            if os.path.isdir(path) and os.path.exists(f"{path}/SKILL.md"):
                print(f"Bootstrapping agent: {item}")
                results.append(bootstrap_skill(item, path))
    
    return results

def main():
    if len(sys.argv) < 2:
        results = bootstrap_all()
    else:
        skill_name = sys.argv[1]
        path = f"{SKILLS_DIR}/{skill_name}"
        if not os.path.exists(path):
            path = f"{AGENTS_DIR}/{skill_name}"
        if not os.path.exists(path):
            print(f"Skill {skill_name} no encontrado")
            return
        results = [bootstrap_skill(skill_name, path)]
    
    # Resumen
    souls = sum(1 for r in results if r.get("soul_created"))
    tests = sum(1 for r in results if r.get("tests_created"))
    
    print(f"\n📊 Bootstrap Results:")
    print(f"  SOUL.md creados: {souls}")
    print(f"  Tests creados: {tests}")

if __name__ == "__main__":
    main()
