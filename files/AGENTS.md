# AGENTS.md - OpenClaw Workspace

## Project Overview
- **Owner:** Elvis
- **Mission:** Ganar dinero de formas múltiples usando AI
- **Projects:** Zaltyko (SaaS), Trading Crypto, Research

## Setup Commands
- Start OpenClaw: `openclaw start`
- Check status: `openclaw status`
- Gateway restart: `openclaw gateway restart`

## Hands (Agentes Automáticos)

| Agent | Rol | Schedule | RIS Layer |
|-------|-----|----------|-----------|
| **Rex** | Research | Daily 09:00 | 1️⃣ Buscar info |
| **Athena** | Analyst | On-demand | 2️⃣ Analizar insights |
| **Cierra** | Sales | Every 6h | Aplicación |
| **Copy** | Content | Daily | Aplicación |
| **Tech** | Build/Implement | On-demand | 3️⃣ Ejecutar código |
| **Trading Bot** | Trading | 10 min | Aplicación |

## Sistema RIS (Research & Implementation)

```
Yota (Meta) → REX (Research) → ATHENA (Analysis) → TECH (Implementation)
```

**Flujo:** Investigar → Analizar → Implementar → Medir → Optimizar

## Workflows
- Lead Generation → CRM → Sale
- Trading Intelligence → Signal → Execute
- Content Creation → Publish → Traffic
- Research → Exa → Summarize

## Code Style
- JavaScript/TypeScript: `const`, arrow functions, no semicolons
- Python: snake_case, type hints where useful
- Commits: descriptivos, en inglés

## Scripts
- `scripts/optimizer.sh` - Auto-optimizer
- `scripts/run-workflow.sh` - Workflow runner
- `scripts/send-outreach.sh` - Email sender

## Permissions
- Approval gates: gastos > $10, trades, publicar external
- 1Password para secrets
- Gmail autorizado (3 cuentas)

## Notes
- Owner prefers: Comunicación directa, concisa, no robótica
- Timezone: Europe/Madrid
- Likes: One Piece 🏴‍☠️
