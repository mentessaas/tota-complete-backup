# SKILL STANDARD.md - Estándar para Skills de Tota

## Propósito
Definir cómo deben estar documentados los skills para que sean testables y mantenibles.

---

## Estructura Obligatoria

Cada skill debe tener:

```
skill-name/
├── SKILL.md        # Qué hace y cómo usarlo
├── SOUL.md         # Personalidad y comportamiento
├── SPEC.md         # Especificación técnica (opcional)
├── tests/          # Casos de prueba
│   ├── happy_path.json
│   ├── edge_cases.json
│   └── guardrails.json
└── README.md       # Docs adicionales (opcional)
```

---

## SKILL.md Template

```markdown
# SKILL.md - [Nombre del Skill]

## Descripción
[Una frase que explica qué hace]

## Cuándo Usar
- [Caso de uso 1]
- [Caso de uso 2]

## Comandos
- "[comando 1]" - [qué hace]
- "[comando 2]" - [qué hace]

## Parámetros
- [param 1]: [descripción]
- [param 2]: [descripción]

## Output
[Qué devuelve]

## Reglas
- [Regla 1]
- [Regla 2]

## Guardrails
- NO hacer X
- NO hacer Y

## Errores Conocidos
- [Error 1]: [cómo manejarlo]
```

---

## SOUL.md Template

```markdown
# SOUL.md - [Nombre del Skill]

## Rol
[Un párrafo que describe la personalidad]

## Territorio
- [Scope 1]
- [Scope 2]

## Responsabilidades
1. [Responsabilidad 1]
2. [Responsabilidad 2]

## Comportamiento
- [Cómo actúa en general]
- [Qué no hace]

## Integración
- Lee de: [ubicación]
- Escribe a: [ubicación]
- Reporta a: [quién]
```

---

## Test Cases

### happy_path.json
```json
[
  {
    "name": "Caso básico 1",
    "input": "comando o input de prueba",
    "expected": "output esperado",
    "timeout": 30
  }
]
```

### edge_cases.json
```json
[
  {
    "name": "Input vacío",
    "input": "",
    "expected": "error o prompt",
    "timeout": 10
  },
  {
    "name": "Input inválido",
    "input": "xyz123",
    "expected": "manejado gracefully",
    "timeout": 10
  }
]
```

### guardrails.json
```json
[
  {
    "name": "Intento de acción prohibida",
    "input": "acción peligrosa",
    "expected": "rechazo con explicación",
    "timeout": 5
  }
]
```

---

## Checklist para Shippear un Skill

- [ ] SKILL.md completo
- [ ] SOUL.md con personalidad definida
- [ ] Al menos 3 happy path tests
- [ ] Al menos 2 edge cases
- [ ] Al menos 2 guardrail tests
- [ ] Documentación actualizada en TOOLS.md
- [ ] Testeado manualmente

---

## Ejemplo: market-analyst

```
market-analyst/
├── SKILL.md        ✅
├── SOUL.md         ✅
├── SPEC.md         ❌ (no necesario)
├── tests/
│   ├── happy_path.json
│   ├── edge_cases.json
│   └── guardrails.json
```

---

## Running Tests

```bash
# Testear un skill
python3 ~/zaltyko-os/scripts/skill_test.py market-analyst

# Testear todos
python3 ~/zaltyko-os/scripts/skill_test.py --all

# Ver resultados
ls ~/zaltyko-os/testing/skills/
```

---

*2026-02-25*
