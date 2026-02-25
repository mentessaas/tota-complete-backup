#!/usr/bin/env python3
"""
Skill Testing Framework
Testea skills automaticamente basándose en archivos de test.

Usage: python3 skill_test.py <skill_name>
       python3 skill_test.py --all
"""
import sys
import os
import json
from datetime import datetime

SKILLS_DIR = os.path.expanduser("~/.openclaw/workspace/skills")
AGENTS_DIR = os.path.expanduser("~/.openclaw/workspace/agents")
WORKSPACE_DIR = os.path.expanduser("~/.openclaw/workspace")
TEST_RESULTS_DIR = os.path.expanduser("~/zaltyko-os/testing/skills")

def load_test_cases(skill_path):
    """Carga los casos de test desde archivos JSON"""
    tests = {
        "happy_path": [],
        "edge_cases": [],
        "guardrails": []
    }
    
    test_dir = f"{skill_path}/tests"
    if not os.path.exists(test_dir):
        return tests
    
    for test_type in tests.keys():
        test_file = f"{test_dir}/{test_type}.json"
        if os.path.exists(test_file):
            with open(test_file, 'r') as f:
                try:
                    tests[test_type] = json.load(f)
                except:
                    pass
    
    return tests

def run_skill_test(skill_name, test_type, test_case):
    """Ejecuta un test individual (simulado por ahora)"""
    skill_path = find_skill_path(skill_name)
    
    if not skill_path:
        return {
            "status": "skip",
            "reason": f"Skill {skill_name} no encontrado"
        }
    
    # Verificar que existe SKILL.md
    skill_md = f"{skill_path}/SKILL.md"
    if not os.path.exists(skill_md):
        return {
            "status": "skip",
            "reason": "Sin SKILL.md"
        }
    
    # Verificar que tiene SOUL.md (recomendado)
    has_soul = os.path.exists(f"{skill_path}/SOUL.md")
    
    # Por ahora, solo verificamos estructura
    # En el futuro, esto podría ejecutar el skill realmente
    return {
        "status": "pass",
        "test_type": test_type,
        "has_soul": has_soul,
        "test_case": test_case.get("name", "unnamed"),
        "timestamp": datetime.now().isoformat()
    }

def find_skill_path(skill_name):
    """Encuentra la ruta de un skill"""
    # Buscar en skills
    path = f"{SKILLS_DIR}/{skill_name}"
    if os.path.exists(path):
        return path
    
    # Buscar en agents
    path = f"{AGENTS_DIR}/{skill_name}"
    if os.path.exists(path):
        return path
    
    # Buscar en workspace
    path = f"{WORKSPACE_DIR}/{skill_name}"
    if os.path.exists(path):
        return path
    
    # Buscar en zaltyko-os/agents
    path = f"{WORKSPACE_DIR}/zaltyko-os/agents/{skill_name}"
    if os.path.exists(path):
        return path
    
    return None

def test_skill(skill_name):
    """Testea un skill específico"""
    skill_path = find_skill_path(skill_name)
    
    results = {
        "skill": skill_name,
        "path": skill_path,
        "timestamp": datetime.now().isoformat(),
        "tests": {
            "happy_path": [],
            "edge_cases": [],
            "guardrails": []
        },
        "checks": {
            "has_skill_md": False,
            "has_soul_md": False,
            "has_tests": False
        }
    }
    
    if not skill_path:
        results["status"] = "not_found"
        return results
    
    # Verificar archivos obligatorios
    results["checks"]["has_skill_md"] = os.path.exists(f"{skill_path}/SKILL.md")
    results["checks"]["has_soul_md"] = os.path.exists(f"{skill_path}/SOUL.md")
    
    # Cargar test cases
    test_cases = load_test_cases(skill_path)
    has_tests = any(test_cases[k] for k in test_cases)
    results["checks"]["has_tests"] = has_tests
    
    # Testear happy path
    for tc in test_cases.get("happy_path", []):
        result = run_skill_test(skill_name, "happy_path", tc)
        results["tests"]["happy_path"].append(result)
    
    # Testear edge cases
    for tc in test_cases.get("edge_cases", []):
        result = run_skill_test(skill_name, "edge_cases", tc)
        results["tests"]["edge_cases"].append(result)
    
    # Testear guardrails
    for tc in test_cases.get("guardrails", []):
        result = run_skill_test(skill_name, "guardrails", tc)
        results["tests"]["guardrails"].append(result)
    
    # Calcular resultado
    all_checks = all(results["checks"].values())
    
    results["status"] = "pass" if all_checks else "incomplete"
    results["summary"] = {
        "skill_md": "✅" if results["checks"]["has_skill_md"] else "❌",
        "soul_md": "✅" if results["checks"]["has_soul_md"] else "❌",
        "tests": "✅" if results["checks"]["has_tests"] else "❌"
    }
    
    return results

def test_all_skills():
    """Testea todos los skills y agents"""
    results = []
    
    # Skills del workspace
    print("🔍 Buscando skills...")
    
    for item in os.listdir(SKILLS_DIR):
        path = f"{SKILLS_DIR}/{item}"
        if os.path.isdir(path):
            print(f"  Testing skill: {item}")
            result = test_skill(item)
            results.append(result)
    
    # Agents
    for item in os.listdir(AGENTS_DIR):
        path = f"{AGENTS_DIR}/{item}"
        if os.path.isdir(path):
            print(f"  Testing agent: {item}")
            result = test_skill(item)
            results.append(result)
    
    return results

def save_results(results, filename=None):
    """Guarda resultados en JSON"""
    os.makedirs(TEST_RESULTS_DIR, exist_ok=True)
    
    if filename is None:
        filename = f"test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    filepath = f"{TEST_RESULTS_DIR}/{filename}"
    with open(filepath, 'w') as f:
        json.dump(results, f, indent=2)
    
    return filepath

def main():
    if len(sys.argv) < 2:
        # Testear todo por defecto
        results = test_all_skills()
    elif sys.argv[1] == "--all":
        results = test_all_skills()
    else:
        skill_name = sys.argv[1]
        results = test_skill(skill_name)
    
    # Mostrar resultados
    if isinstance(results, list):
        passed = sum(1 for r in results if r.get("status") == "pass")
        incomplete = sum(1 for r in results if r.get("status") == "incomplete")
        not_found = sum(1 for r in results if r.get("status") == "not_found")
        
        print(f"\n📊 Test Results:")
        print(f"  ✅ Pass: {passed}")
        print(f"  ⚠️  Incomplete: {incomplete}")
        print(f"  ❌ Not Found: {not_found}")
        
        print("\n📋 Details:")
        for r in results:
            status = r.get("status", "unknown")
            if status == "pass":
                emoji = "✅"
            elif status == "incomplete":
                emoji = "⚠️"
            else:
                emoji = "❌"
            
            summary = r.get("summary", {})
            skill_md = summary.get("skill_md", "?")
            soul_md = summary.get("soul_md", "?")
            tests = summary.get("tests", "?")
            
            print(f"  {emoji} {r.get('skill')}: SKILL={skill_md} SOUL={soul_md} TESTS={tests}")
    else:
        r = results
        print(f"\n📊 {r.get('skill')}: {r.get('status')}")
        print(f"   SKILL.md: {'✅' if r['checks']['has_skill_md'] else '❌'}")
        print(f"   SOUL.md: {'✅' if r['checks']['has_soul_md'] else '❌'}")
        print(f"   Tests: {'✅' if r['checks']['has_tests'] else '❌'}")
    
    # Guardar
    filepath = save_results(results)
    print(f"\n💾 Saved to: {filepath}")

if __name__ == "__main__":
    main()
