# Rotation Log - Evita loops de tareas

> Si corro el mismo job 3x seguidas → rotar a otro tipo de tarea.

## Estado actual

```json
{
  "lastJobs": [],
  "jobHistory": [],
  "rotationCounter": 0
}
```

## Jobs disponibles para Zaltyko

| Job | Tipo | Prioridad |
|-----|------|-----------|
| lead-research | research | alta |
| email-outreach | outreach | alta |
| crm-update | ops | media |
| standup-report | report | baja |
| health-check | ops | baja |

## Regla de rotación

1. Si mismo tipo de job 2x seguidas → siguiente tipo
2. Mantener contador de rotación
3. Resetear si hubo interacción humana

## Historial (últimos 10)

| Fecha | Job | Resultado |
|-------|-----|-----------|
| - | - | (vacío) |
