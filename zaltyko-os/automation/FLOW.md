# 🤖 Sistema de Automatización - Zaltyko

## Flujo Completo

```
┌─────────────────────────────────────────────────────────────┐
│                    ZALTYKO AUTOMATION                       │
└─────────────────────────────────────────────────────────────┘

    ┌──────────────┐
    │   LEAD       │
    │   RESEARCH   │ ← Sales Agent 3x/día (web_search)
    └──────┬───────┘
           ↓
    ┌──────────────┐
    │   CRM        │ ← Se guarda con formato estándar
    │   + Email 1  │ ← Template Intro
    └──────┬───────┘
           ↓ (3 días)
    ┌──────────────┐
    │  CHECK:      │
    │  Respondió?  │
    └──────┬───────┘
      ↓         ↓
     SÍ         NO
      ↓         ↓
┌─────────┐  ┌──────────────┐
│Qualify  │  │  Email 2    │ ← Template Follow-up
│→ Demo   │  │  (día 3)    │
└─────────┘  └──────┬───────┘
                    ↓ (2 días)
             ┌──────────────┐
             │  CHECK:      │
             │  Respondió?  │
             └──────┬───────┘
               ↓         ↓
              SÍ         NO
               ↓         ↓
         ┌─────────┐  ┌───────────┐
         │Qualify  │  │ ARCHIVED  │
         └─────────┘  └───────────┘
```

---

## Jobs Activos

| Job | Frecuencia | Qué hace |
|-----|------------|----------|
| Lead Research | 10am, 2pm, 6pm | Busca leads reales |
| Check Responses | Cada hora | Mira si hay respuestas |
| CRM Update | On-demand | Actualiza status |
| Health Check | Cada hora | Verifica sistema |
| Weekly Review | Domingos | Auto-mejora |

---

## Onboarding Flow

```
Usuario se registra
       ↓
Webhook /api/webhooks/welcome
       ↓
Email de bienvenida (Brevo)
       ↓
Usuario → Dashboard
```

---

## CRM Status

- **lead**: Nuevo lead
- **contacted**: Email enviado
- **qualified**: Interesado, quiere demo
- **prospect**: En proceso de cierre
- **customer**: Cliente pagado
- **archived**: Sin respuesta (después de 2 emails)
