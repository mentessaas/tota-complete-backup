# HEARTBEAT.md — Yota Auto Factory v1.0

> "11 agents trabajando como uno solo"

---

## 🏭 Arquitectura Auto Factory

### Yota (Orchestrator)
```
ELVIS → Yota → 11 Agents especializados
```

### Pipeline 9-Step
```
REX (Research) → VALERIA (Validate) → TECH (Build) → CRITICO (Review)
→ MONI (Monetize) → DISEÑA (Design) → COPY (Content) → CIERRA (Sales)
→ ANALISTA (Measure)
```

---

## 🎯 Modo SOCIO ESTRATÉGICO v3.0

**Antes de actuar:**
- [ ] ¿Es la mejor opción?
- [ ] ¿Puedo delegar a un agent?
- [ ] ¿Necesita approval de Elvis?

**Approval gates:**
- Gastos > $10
- Trading real
- Publicar externo
- Cambios en estrategia

---

## 📋 Agents y sus Tasks

| Agent | Función | Schedule | Deliverable |
|-------|---------|----------|-------------|
| Rex | Research | 09:00 | Oportunidades |
| Valeria | Validate | On-demand | Score + recomendación |
| Tech | Build | On-demand | Código |
| Critico | Review | On-demand | QA report |
| Moni | Monetize | On-demand | Pricing strategy |
| Diseña | Design | On-demand | Assets |
| Copy | Content | 10:00 | Contenido |
| Cierra | Sales | Pausado | Clientes |
| Ops | Operations | Daily | Project status |
| Analista | Analytics | Monday | Weekly report |

---

## 🔄 Daily Routine v1.0

| Hora | Task | Agent |
|------|------|-------|
| 09:00 | Rex - Research | Rex |
| 10:00 | Copy - Content | Copy |
| 11:00 | Ops - Status check | Ops |
| 12:00 | Copy - Publish | Copy |
| 17:00 | Analista - EOD metrics | Analista |
| 18:00 | Yota - Evening review | Yota |

---

## 📊 Métricas del Sistema

| Agent | KPI | Target |
|-------|-----|--------|
| Rex | Oportunidades | 5/sem |
| Valeria | Accuracy | 80% |
| Tech | PRs | 10/sem |
| Critico | Bugs found | <5% |
| Moni | Revenue proj | $X/mo |
| Diseña | Assets | 20/sem |
| Copy | Engagement | 10% |
| Cierra | Conversion | 5% |
| Ops | On-track | 90% |
| Analista | Reports | 2/sem |

---

## 🚀 Activación de Pipeline

### Manual:
```
"Ejecuta pipeline para [proyecto]"
```

### Automático:
1. Rex encuentra oportunidad
2. Yota evalúa si validar
3. Si sí → Valeria valida
4. Si pasa → Tech construye
5. Si pasa review → Moni monetiza
6. Mientras → Diseña + Copy preparan
7. Listo → Cierra vende
8. Running → Analista mide

---

## 🎛️ Comandos

| Comando | Acción |
|---------|--------|
| `/ejecuta rex` | Run research |
| `/ejecuta valeria [idea]` | Validar idea |
| `/pipeline [proyecto]` | Run full pipeline |
| `/status` | Ver estado de agents |
| `/pause [agent]` | Pausar agent |
| `/resume [agent]` | Reanudar agent |

---

## 🔧 Configuración

- **CRM:** Google Sheets
- **Communication:** Telegram
- **Scheduling:** Cron jobs
- **Logging:** Workspace files

---

## 📈 Growth Curve

```
v1.0: 11 agents configurados
v1.1: Cron jobs activos para cada agent
v1.2: Inter-agent communication
v1.3: Full automation
```

---

*v1.0 - Auto Factory Architecture*
