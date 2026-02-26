# 🎯 Playbook de Setup - Tota (OpenClaw)

> Documentación de nuestro setup actual. Actualizado: 2026-02-20

---

## 🏠 Infraestructura

| Componente | Detalle |
|-----------|---------|
| Hardware | MacBook Air (Elvis) |
| OS | macOS 25.3.0 (arm64) |
| Node | v25.5.0 |
| Puerto Gateway | 18789 |
| Workspace | ~/.openclaw/workspace/ |

---

## 📋 Canales Activos

| Canal | Estado | Config |
|-------|--------|--------|
| Telegram | ✅ Activo | botToken en config |
| WhatsApp | ❌ No configurado | - |
| Discord | ❌ No configurado | - |

---

## 🧠 Modelos

| Modelo | Uso | Estado |
|--------|-----|--------|
| minimax-portal/MiniMax-M2.5 | Por defecto | ✅ |
| minimax-portal/MiniMax-M2.1 | Tareas simples | ✅ |
| openai-codex/gpt-5.2 | Coding complejo | ✅ |

---

## 🔧 Skills Instalados

| Skill | Función |
|-------|---------|
| tavily | Búsquedas web |
| stealth-browser | Scraping anti-detección |
| brevo | Email outreach |
| humanizer | Hacer texto más natural |
| auto-updater | Actualizaciones diarias |
| gog | Gmail/Calendar API |
| ... | - |

---

## ⚙️ Crons Activos

| Cron | Frecuencia | Estado |
|------|------------|--------|
| Dev Agent - Health Check | hourly | ✅ |
| Zaltyko Lead Research | cada 4h | ✅ |
| Tota Heartbeat | cada 4h | ✅ |
| Daily morning summary | 7:30 diario | ✅ |
| secondbrain:kanban-autopilot-daily | 9:00 diario | ✅ |
| Zaltyko Daily Standup | 9:00 L-V | ✅ |
| BrainDump morning | 10:30 L-V | ✅ |
| BrainDump evening | 20:30 L-V | ✅ |
| QA tests | 19:00-20:00 | ⚠️ delivery failed |
| Daily Auto-Update | 4:00 diario | ✅ |
| Tota Daily Backup | 23:00 diario | ✅ |
| Nightly Mission Prompt | 23:00 L-V | ✅ |

---

## 📁 Estructura de Archivos

```
~/.openclaw/workspace/
├── AGENTS.md           # Reglas de operación
├── MEMORY.md           # Memoria a largo plazo
├── KERNEL.md           # Lo esencial de Elvis
├── IDENTITY.md         # Quién soy (Tota)
├── HEARTBEAT.md        # Tareas periódicas
├── KERNEL.md           # Lo esencial
├── zaltyko-os/
│   ├── agents/         # Subagentes
│   ├── leads/         # Leads encontrados
│   ├── outreach/       # Emails enviados
│   ├── research/      # Research (Reddit, etc)
│   ├── automation/    # Scripts automatizados
│   └── status.json    # Estado del proyecto
└── mente-totita/      # Dashboard UI
```

---

## 🔑 API Keys Configuradas

| Servicio | Archivo | Estado |
|----------|--------|--------|
| Tavily | ~/.openclaw/secrets/tavily.json | ✅ |
| Brevo | keys.env | ✅ |
| Vercel | keys.env | ✅ |
| n8n | keys.env | ✅ |
| Gmail (mitotabot) | gog config | ✅ |
| Gmail (elvis) | Token expirado | ❌ |

---

## 🚨 Reglas de Seguridad

1. ✅ NO ejecutar código de internet sin preguntar
2. ✅ NO instalar skills de fuentes desconocidas
3. ✅ Revisar siempre SKILL.md antes de instalar
4. ✅ Usar cuentas separadas para automation
5. ✅ Limitar API keys con presupuestos
6. ✅ No dar acceso a datos sensibles sin aprobación

---

## 📝 Tareas Pendientes

- [ ] Autorizar Gmail (elvisvaldes544@gmail.com)
- [ ] Configurar WhatsApp para outreach
- [ ] YouTube summarizer para research
- [ ] Revisar skills instalados

---

## 🔄 Cómo Replicar Este Setup

```bash
# 1. Instalar OpenClaw
curl -fsSL https://openclaw.ai/install.sh | bash

# 2. Configurar Telegram
# (ver docs de OpenClaw)

# 3. Instalar skills esenciales
npx clawdhub install tavily
npx clawdhub install stealth-browser

# 4. Configurar API keys
# (tavily, brevo, etc)

# 5. Copiar workspace config
# (AGENTS.md, MEMORY.md, etc)
```

---

*Actualizado: 2026-02-20*
*Tota 🐻*
