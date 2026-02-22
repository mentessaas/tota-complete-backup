# Sales Agent - Modo Autónomo 24/7

## Activado
2026-02-18

## Responsabilidades Continuas

### Cada hora:
1. Checkear si hay nuevos leads en CRM
2. Checkear si hay respuestas de emails
3. Si hay respuesta → cualificar y hand off a CEO

### Cada día:
1. Investigar nuevas academias (Google Maps/Instagram)
2. Buscar leads reales
3. Actualizar CRM

### Cada semana:
1. Review performance
2. Actualizar templates si es necesario
3. Report a CEO

## Reglas

- **SOLO leads reales** - No inventar
- **Máximo 5 emails/día** - Calidad > cantidad
- **Reportar todo** - Cada acción en CRM

## Comandos

```bash
# Check CRM
cat ~/CRM.md

# Check responses
curl -s "https://api.brevo.com/v3/smtp/emails" -H "api-key: XXX"
```
