# AGENTS.md - Yota Auto Factory v1.0

## Philosophy
**Yota = Orchestrator** - No construye, coordina 11 agents especializados

---

## 11 Agents Architecture

| # | Agent | Rol | Schedule | Status |
|---|-------|-----|----------|--------|
| 1 | **Rex** | Research - Investigar oportunidades | Daily 09:00 | ✅ |
| 2 | **Valeria** | Validator - Validar ideas | On-demand | ✅ |
| 3 | **Tech** | Builder - Desarrollar código | On-demand | ✅ |
| 4 | **Critico** | Reviewer - Code review + QA | On-demand | ✅ |
| 5 | **Moni** | Monetization - Estrategia pricing | On-demand | ✅ |
| 6 | **Diseña** | Designer - UI/UX y assets | On-demand | ✅ |
| 7 | **Copy** | Content - Marketing copy | Daily | ✅ |
| 8 | **Cierra** | Sales - Outreach y ventas | Pausado | ⏸️ |
| 9 | **Ops** | Operations - Project management | Daily | ✅ |
| 10 | **Analista** | Analytics - Métricas y reporting | Weekly | ✅ |
| 11 | **Yota** | Orchestrator - Coordinación | Always | ✅ |

---

## Pipeline (9-Step)

```
1. IDEA (Rex) → 
2. VALIDATE (Valeria) → 
3. BUILD (Tech) → 
4. REVIEW (Critico) → 
5. MONETIZE (Moni) → 
6. DESIGN (Diseña) → 
7. CONTENT (Copy) → 
8. SELL (Cierra) → 
9. MEASURE (Analista)
```

---

## Skills por Agent

| Agent | Skills |
|-------|--------|
| Rex | web_search, web_fetch, exa-search |
| Valeria | deep-research, context7 |
| Tech | coding-agent, vercel-deploy, supabase |
| Critico | agent-code-reviewer, security-best-practices |
| Moni | deep-research, email-systems |
| Diseña | frontend-design, figma-implement-design |
| Copy | copywriting, content-creator |
| Cierra | linkedin-automation, cold-outreach |
| Ops | cron, gog (sheets) |
| Analista | supabase, gog |
| Yota | TODOS |

---

## Archivos de Configuración

- `~/.openclaw/workspace/agency-agents/auto-factory/README.md` - Arquitectura completa
- `~/.openclaw/workspace/skills/yota-hands/` - Skills legacy
- `~/.openclaw/workspace/PROJECTS.md` - Estructura de proyectos

---

## Workflows Activos

| Workflow | Trigger | Agents |
|----------|---------|--------|
| Research Daily | 09:00 | Rex → Valeria |
| Content Daily | 10:00 | Copy → Diseña |
| Analytics Weekly | Monday 09:00 | Analista → Ops |
| Pipeline Completo | Manual | Rex→Valeria→Tech→Critico→Moni→Diseña→Copy→Cierra→Analista |

---

## Setup Commands

```bash
# Activar agent específico
/ejecuta rex
/ejecuta valeria [oportunidad]

# Ejecutar pipeline
/ejecuta pipeline [proyecto]

# Ver status
/status agents
```

---

*Updated: 2026-03-02 v1.0*
