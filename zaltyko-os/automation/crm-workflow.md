# CRM Workflow Automation

## Trigger: Nuevo Lead

### Flow:

```
1. LEAD ENTRA (por cualquier fuente)
   ↓
2. CRM Agent LO REGISTRA
   - Nombre, Email, Teléfono, Fuente
   - Status: "lead"
   - Fecha entrada
   ↓
3. SI tiene email válido:
   - Enviar Template 1: Intro
   - Esperar 3 días
   ↓
4. CHECK: ¿Respondió?
   - SÍ → Cualificar → Hand off a Sales
   - NO → Enviar Template 2: Follow-up
   - Esperar 2 días
   ↓
5. CHECK: ¿Respondió?
   - SÍ → Cualificar
   - NO → Archivar (status: "archived")
```

## Status Flow

```
lead → contacted → qualified → prospect → customer
                  ↘ (no response) → archived
```

## Templates

- Template 1: Intro (día 0)
- Template 2: Follow-up (día 3)
- Template 3: Last chance (día 5)

## Automatización

Este workflow corre automáticamente cuando:
1. Sales Agent encuentra lead (research)
2. Usuario se registra en Zaltyko
3. Referencia de otro cliente
