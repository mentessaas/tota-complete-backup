# Configuración de Email - Brevo

## Sender Configurado

| Campo | Valor |
|-------|-------|
| Name | Zaltyko |
| Email | info@elvisinerarte.com |
| Status | ✅ Activo |

## Templates Creados

| ID | Nombre | Estado |
|----|--------|--------|
| 25 | Zaltyko - Bienvenida | ✅ Activo |

## Enviar Email Programáticamente

```bash
curl -X POST "https://api.brevo.com/v3/smtp/email" \
  -H "api-key: xkeysib-REDACTED" \
  -H "Content-Type: application/json" \
  -d '{
    "sender": {"name": "Zaltyko", "email": "info@elvisinerarte.com"},
    "to": [{"email": "destinatario@email.com", "name": "Nombre"}],
    "subject": "Asunto del email",
    "htmlContent": "<html>...</html>"
  }'
```

## Variables para Templates

- `{{name}}` - Nombre del usuario
- `{{dashboardUrl}}` - URL del dashboard
- `{{email}}` - Email del usuario

## Límites

- Plan Free: 300 emails/mes
- Envío: smtp-relay.brevo.com:587

## DNS (para dominio propio)

Cuando tengas dominio zaltyko.com:
- Añadir SPF: v=spf1 include:spf.brevo.com ~all
- Añadir DKIM: (configurar en Brevo)
