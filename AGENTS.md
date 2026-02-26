# AGENTS.md — Tu Workspace (Elvis / Totin)

---

## 🏠 EQUIPO ACTUAL (Workflow Discord)

| Canal Discord | Agente | Función |
|--------------|--------|---------|
| #rex-investigador | Rex | Research y análisis |
| #cierra-ventas | Cierra | Ventas y ofertas |
| #copy-creator | Copy | Contenido y marketing |
| #tech-builder | Tech | Build y automatizaciones |
| #trading | Trading Bot | Señales y ejecución |
| #general | Totin | Mission Control |

---

## 🎯 Totin Control
- #tota
- #reportes
- #operaciones

---

## 📈 Trading
- **#trading**
- 🧠 trading-chief → market-scanner, signal-analyst, risk-manager, crypto-news
- 💼 business-advisor

---

## 🏢 Zaltyko
- **#ventas**
- 🧠 sales-chief → lead-hunter, data-enricher, outreach-writer, follow-up
- 📊 social-tracker

---

## 📝 Content
- **#content**
- 🧠 content-chief → topic-researcher, copy-generator

---

## 🧠 Personal
- **#personal**
- 🧠 personal-chief → calendar, reminder
- 💡 knowledge-base
- 🔄 auto-updater

---

## Crons Activos

| Chief/Agent | Frecuencia |
|-------------|------------|
| Trading Chief | 10 min |
| Sales Chief | 6h |
| Content Chief | Daily |
| Personal Chief | Daily |
| Knowledge Base | Daily |
| Business Advisor | Daily |
| Social Tracker | Daily |
| Auto Updater | 21:00 |
| Health Check | 1h |
| Morning Briefing | 09:00 |
# OpenClaw Agents - Organización

## 🏠 PRINCIPAL (1)
| ID | Función |
|---|---------|
| main | Tu agente principal (Tota) |

---

## 🐛 BUG FIX (6) - Corrección de errores
| ID | Función |
|---|---------|
| bug-fix/triager | Clasifica y prioriza bugs |
| bug-fix/investigator | Investiga la causa raíz |
| bug-fix/setup | Configura el entorno de debug |
| bug-fix/fixer | Aplica la corrección |
| bug-fix/verifier | Verifica que funciona |
| bug-fix/pr | Crea el PR con los cambios |

---

## ⚙️ FEATURE DEV (6) - Desarrollo de features
| ID | Función |
|---|---------|
| feature-dev/planner | Planifica la feature |
| feature-dev/setup | Prepara el entorno |
| feature-dev/developer | Escribe el código |
| feature-dev/tester | Escribe tests |
| feature-dev/reviewer | Revisa código |
| feature-dev/verifier | Verifica que todo pasa |

---

## 🔒 SECURITY AUDIT (7) - Auditoría de seguridad
| ID | Función |
|---|---------|
| security-audit/scanner | Escanea vulnerabilidades |
| security-audit/prioritizer | Prioriza riesgos |
| security-audit/setup | Prepara auditoría |
| security-audit/fixer | Aplica fixes |
| security-audit/tester | Testea seguridad |
| security-audit/verifier | Verifica fixes |
| security-audit/pr | Crea PR |

---

## 🧠 BUSINESS (2)
| ID | Función |
|---|---------|
| ceo | Dirección estratégica |
| cto | Arquitectura técnica |

---

## 🔍 RESEARCH (2)
| ID | Función |
|---|---------|
| research | Investigación general |
| researcher | Investigador específico |

---

## 📝 BUILD/PLAN/QA/DOCS (4)
| ID | Función |
|---|---------|
| build | Construcción |
| plan | Planificación |
| qa | Quality Assurance |
| docs | Documentación |

---

## 💰 TRADING (1)
| ID | Función |
|---|---------|
| trader | Trading automatizado |

---

## ✍️ WRITING (1)
| ID | Función |
|---|---------|
| writer | Escritura/contenido |

---

## Cuándo usar cada suite

| Necesidad | Agents a usar |
|----------|---------------|
| Bug en código | bug-fix/triager → investigator → fixer → verifier → pr |
| Nueva feature | feature-dev/planner → developer → tester → reviewer → verifier |
| Auditoría seguridad | security-audit/scanner → prioritizer → fixer → tester → verifier |
| Investigar | research / researcher |
| Escribir | writer |
| Trading | trader |
| Estrategia | ceo, cto, plan |
