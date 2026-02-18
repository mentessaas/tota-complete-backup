# 🧠 Sistema de Memoria - Tota

## Estructura

```
memory/
├── dailies/        ← Logs diarios (YYYY-MM-DD.md)
├── projects/       ← Proyectos activos
│   ├── zaltyko.md
│   ├── gymnasticmeet.md
│   └── mentes-saas.md
├── people/         ← Personas
│   └── elvis.md
├── leads/         ← Leads de Zaltyko
├── notes/         ← Notas misceláneas
└── history/       ← Historial de decisiones
```

## Reglas

1. **LEER antes de actuar**: SOUL.md → USER.md → MEMORY.md → proyecto relevante
2. **GUARDAR todo**: Decisiones, lecciones, datos importantes
3. **TAGGUEAR**: #decision, #lead, #lesson, #config
4. **NO DUPLICAR**: Si ya está en CRM, no crear otro archivo

## Comandos Útiles

```bash
# Ver estado de proyecto
cat memory/projects/zaltyko.md

# Ver persona
cat memory/people/elvis.md

# Buscar en memoria
grep -r "keyword" memory/

# Hoy en la historia
ls memory/dailies/
```

## Tags

| Tag | Uso |
|-----|-----|
| #decision | Decisiones de negocio |
| #lesson | Lecciones aprendidas |
| #lead | Leads de Zaltyko |
| #config | Configuraciones |
| #blocker | Bloqueos |
| #idea | Ideas pendientes |

---

*Sistema de memoria v1.0 - 2026-02-18*
*🦊 Tota*
