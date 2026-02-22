# Research → Outreach Workflow

> Workflow automático: cuando hay leads nuevos, generar outreach

## Trigger
Cuando Lead Research encuentra leads con email

## Flow

```
Lead Research (cada 4h)
    ↓
[Si hay leads nuevos con email]
    ↓
Generar emails humanizados
    ↓
Enviar por Brevo
    ↓
Reportar a Elvis
```

## Implementación

### Paso 1: Lead Research
Ya existe: Zaltyko Lead Research (cada 4h)
- Busca academias
- Guarda en leads/
- Reporta si hay leads

### Paso 2: Check & Generate Emails
Nuevo cron: "Research → Outreach Pipeline"
- Check ~/zaltyko-os/leads/
- Si hay leads sin procesar y con email → generar emails
- Guardar en outreach/emails-pending.json

### Paso 3: Send Emails
Nuevo cron: "Email Outreach Pipeline"
- Lee emails pendientes
- Envía por Brevo
- Mueve a sent/

### Paso 4: Report
- Resumen de emails enviados
- siguiente lead a seguir

---

## Crons Relacionados

| Cron | Frecuencia | Estado |
|------|------------|--------|
| Zaltyko Lead Research | cada 4h | ✅ |
| Email Outreach Pipeline | cada 6h | ⏳ crear |
| Daily Pipeline Check | diario 10:00 | ⏳ crear |

---

*Creado: 2026-02-20*
