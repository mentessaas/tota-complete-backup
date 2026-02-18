# TOOLS.md — Local Notes (Elvis / Tota)

Este archivo es mi “chuleta” local: rutas, nombres, aliases y detalles del entorno.
**NO guardes aquí secretos** (API keys, tokens, passwords). Solo ubicaciones y nombres.

---

## 0) Principios

* Si necesito un dato local (ruta/alias/nombre), lo busco aquí antes de preguntarte.
* Si falta, pregunto **1 cosa exacta** y lo anoto aquí.
* Nunca guardo credenciales. Solo: “dónde están” o “qué variable usar”.

---

## 1) Entorno local

* Equipo: **MacBook Air M1 (16GB)**
* OS: macOS
* Zona horaria: **Europe/Madrid**
* Chat/canal principal del agente: **"Tota"** (referencia interna)

---

## 2) Rutas importantes (no adivinar)

### OpenClaw

* State dir: `~/.openclaw`
* Workspace dir: `TODO:` (ej: `~/.openclaw/workspace`)

### Second Brain / Obsidian

* Vault nombre: `Segun Cerebro`
* Ruta vault: `/Users/elvisvaldesinerarte/Desktop/Segun Cerebro`
* Kanban/Tablero principal: `http://localhost:3002/inbox`
* Carpeta “inbox” (si usas): `http://localhost:3002/inbox`

---

## 3) Comandos rápidos (copiar/pegar)

> Ajusta los comandos a tu instalación real si difieren.

### OpenClaw

* Ver config clave:

  * `openclaw config get agents.defaults.heartbeat.every`
  * `openclaw config get agents.defaults.heartbeat.model`
* Ver último heartbeat:

  * `openclaw system heartbeat last`

### Git (si tu Second Brain o proyectos usan git)

* Estado: `git status`
* Pull: `git pull`
* Push: `git push`

---

## 4) Providers / Modelos (sin keys)

* Provider principal: `TODO:` (OpenAI / OpenRouter / Ollama / etc.)
* Modelo barato para Heartbeat: `TODO:` (ej: `openai/gpt-4o-mini`)
* Modelo potente (solo cuando haga falta): `TODO:` (ej: `openai/gpt-5-mini`)

Si usas Ollama:

* Base URL: `http://127.0.0.1:11434`
* Modelos instalados (corto): `TODO:`

Ubicación de credenciales (solo ruta):

* `.env` (si existe): `TODO:` (ruta)
* Variables típicas (referencia): `OPENAI_API_KEY`, `OPENROUTER_API_KEY`, `BRAVE_API_KEY`

---

## 5) Canales (dónde habla Tota)

* MAIN SESSION: Chat directo contigo (aquí sí puede usar MEMORY.md)
* Otros canales (si aplica):

  * Telegram: `TODO:` (nombre del bot/canal, sin IDs)
  * Discord/Slack/WhatsApp: `TODO:`

---

## 6) Automatización (solo si ya existe)

* n8n: `TODO:` (local/hosted) + URL si aplica
* Brevo: `TODO:` (listas/flows relevantes)

---

## 7) Defaults operativos (para no discutir cada vez)

* WIP (tareas abiertas): `1`
* Horario “no molestar”: `23:00–08:00`
* Prioridad: **MONEY → OPS/TECH → HEALTH → SOCIAL**
* Si no hay acción clara: `HEARTBEAT_OK`

---

## 8) Runbooks (cosas que se rompen)

### OpenClaw no responde

* Checklist:

  1. ¿Gateway/servicio corriendo? `TODO:` (comando que usas)
  2. ¿Provider/model OK? `TODO:`
  3. Logs: `TODO:`
* Fix típico: `TODO:`

---

## 9) Future (opcional)

Si algún día vuelves a VPS, aquí va una sección “VPS” con host/alias/rutas (sin credenciales).

<!-- antfarm:workflows -->
# Antfarm Workflows

Antfarm CLI (always use full path to avoid PATH issues):
`node ~/.openclaw/workspace/antfarm/dist/cli/cli.js`

Commands:
- Install: `node ~/.openclaw/workspace/antfarm/dist/cli/cli.js workflow install <name>`
- Run: `node ~/.openclaw/workspace/antfarm/dist/cli/cli.js workflow run <workflow-id> "<task>"`
- Status: `node ~/.openclaw/workspace/antfarm/dist/cli/cli.js workflow status "<task title>"`
- Logs: `node ~/.openclaw/workspace/antfarm/dist/cli/cli.js logs`

Workflows are self-advancing via per-agent cron jobs. No manual orchestration needed.
<!-- /antfarm:workflows -->

