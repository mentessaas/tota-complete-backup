# MEMORY.md - Tota's Brain

> "Lo que recuerdo define quién soy. Lo que olvido me define igual."

---

## Propietario
- **Owner:** Elvis
- **Asistente:** Totin (Mission Control)
- **Equipo:** Rex, Cierra, Copy, Tech

---

## 🎯 Objetivos Actuales

### Objetivo Principal
**Ganar dinero de formas múltiples usando AI**

### Proyectos Activos
| Proyecto | Estado | Prioridad |
|----------|--------|-----------|
| Zaltyko | Activo | Alta |
| Trading | Pausado (API) | Media |
| Research | Activo | Alta |

---

## 👤 Perfil de Elvis

### Preferencias
- Comunicación directa, sin relleno
- No emojis en contexto de trading
- Prefiere Telegram sobre otros canales
- Mañanas para trabajo profundo
- Le gusta One Piece 🏴‍☠️

### Cómo funciona
- Multi-potencial - cambia de intereses
- Conecta ideas de campos distintos
- No le gusta la repetición
- Le gusta aprender y sintetizar

### Objetivos
- Escape del trabajo tradicional
- Building: Zaltyko (SaaS para academias)
- Trading crypto automatizado

---

## 📊 Decisiones Clave

### 2026-03-10
- **AgentHub Automatizado:**
  - Canales creados: #rex, #valeria, #tech, #cierra
  - Cron jobs activos para posts diarios (9-11h)
  - Script: ~/workspace/scripts/log_experiment.sh
- **Tota Auto-Evolution System:**
  - save-config.sh: Guarda snapshots de config como commits
  - evaluate.sh: Auto-evalúa mis respuestas
  - log-learning.sh: Documenta decisiones
  - Cron job diario (23:00) para self-evaluation
- **Auto-Auditoría configurada:**
  - Exec sin approval (security: allowlist) ✅
  - Script: ~/workspace/scripts/auto-audit.sh
  - Cron job: cada 2 horas → reporta en #tota
  - Aprende de errores sin romper nada

### 2026-03-02
- **Investigación OpenFang:** Analicé competencia (OpenFang vs OpenClaw)

### 2026-02-28
- **Investigación OpenFang:** Analicé competencia (OpenFang vs OpenClaw)
- **Setup v2.5:** Apliqué lecciones de OpenFang + Meta-Growth Loops:
  - HEARTBEAT.md → Hands activos con schedule + Meta-Growth
  - AGENTS.md → Estructura de Hands con handbooks
  - APPROVAL_GATES.md → Approval gates como OpenFang
  - **Skills:** 47+ instalados (trading, sales, content, automation)
  - **Workflows:** 5 pipelines activos
  - **Growth Loops:** 5 loops implementados
  - **Gmail:** ✅ Autorizado (3 cuentas)
- **Gap identificado:** Cold start (33x más lento), seguridad (5x menos)

### 2026-02-26
- Setup de equipo de agentes: Rex, Cierra, Copy, Tech
- Workflow paralelo por canales Discord
- Sistema de correcciones (self-improver)
- Daily Research + Evening Review

### 2026-02-25
- Cambio de KuCoin a Asterdex
- Implementación de Articles of Cooperation
- CRM limpio (leads reales)

---

## 🔧 Auto-Correction Rules

### Discord Channel Errors
Si un job falla con "Message failed" o canal no encontrado:
1. Cambiar `delivery.to` a canal principal #tota: `1476346800389619773`
2. Verificar con `message action=channel-list`

### Canales válidos actuales:
- #tota: 1476346800389619773 (principal)
- #tota-operaciones: 1476340924790603847

### Errores comunes:
- "Message failed" = canal no existe
- Timeout = job muy largo, aumentar timeoutSeconds

### CRM (Marzo 2026)
- **Google Sheets CRM:** https://docs.google.com/spreadsheets/d/18Qh-h1X_Ub1M_y71zRAxyv_FiPsLpkA_EUCKCKn6v44
- Sheets: Leads, Proyectos, Facturas
- Email: zaltyko@gmail.com

### Modelos Locales (Marzo 2026)
- Ollama: llama3.2:1b (1.3GB)
- Listo para usar: `/model ollama/llama3.2:1b`

---

## Etiquetas

### Cómo pedirme cosas
1.直接 - máximo 3 opciones
2. Si puedo arreglarlo en 2 min → lo hago
3. Resumen al final de sesiones importantes

### Auto-save
- Decisiones → MEMORY.md + daily
- Errores → errors.md
- Proyectos → projects/*.md

---

## 📅 Tareas Pendientes

### Alta Prioridad
- [ ] Resolver API trading (Hyperliquid u otro exchange)
- [x] **Configurar exec sin approvals** (security: allowlist) ✅
- [ ] Twitter API auth

### Alternativas disponibles (sin API needed)
- **Yahoo Data Fetcher** - Stocks/crypto quotes sin API ✅
- **Hyperliquid** - Datos públicos (precios, funding, OI) sin API ✅

### Media Prioridad
- [x] Probar workflow de canales Discord
- [x] Setup Morning Research
- [x] Gmail autorizado ✅

### Pausado
- [ ] Lead Generation Gimnasia Rítmica (pausado por Elvis)

### Completado v2.5
- [x] Skills 47+ instalados
- [x] 5 Workflows activos
- [x] 5 Meta-Growth Loops
- [x] Scripts automation

---

## 🧠 Lecciones

1. **No inventar datos** - CRM limpio > CRM lleno
2. **Governance funciona** - Agentes con territorios definidos
3. **Automatizar sin spam** - Calidad > Cantidad
4. **Auto-save crítico** - Si no lo grabo, se pierde
5. **Hands > Agentes genéricos** - Agentes pre-configurados con schedule rinden más
6. **Approval gates esenciales** - Siempre pedir permiso para acciones sensibles
7. **速度快 = mejor** - Cold start < 200ms es meta real
8. **Meta-Growth Loops** - Cada acción debe medirse, analizarse y optimizarse

### De OpenFang (2026-02-28)
- Arquitectura monolit binaria reduce complejidad
- Seguridad en profundidad (16 capas) > parches
- Autonomía real = agente trabaja PARA ti, no espera
- **Meta-Growth:** Cada acción = ejecutar → medir → optimizar → repetir

### De análisis hijos IA (2026-03-01)
- **Proactivity:** No esperar siempre, iniciar mejora
- **Context:** Preguntar antes de actuar
- **Creatividad:** Explorar nuevos ángulos
- **Judgment:** Cuestionar supuestos

### De Simon Willison - Agentic Engineering (2026-03-04)
- **Code is cheap, good code isn't:** Escribir código = barato, pero código bueno (testeado, documentado, mantenible) = caro
- **Hoard patterns:** Acumular soluciones probadas con código funcional → recombinar para nuevos problemas
- **Red/Green TDD:** Tests primero → confirmar fail → implementar → pass
- **First run tests:** Siempre ejecutar tests al inicio de sesión coding
- **Linear walkthroughs:** Para entender código que no has escrito
- **Interactive explanations:** Crear visualizaciones para conceptos complejos

### De Polsia - AI That Runs Your Company (2026-03-04)
- **80/20 Revenue Split:** AI only gana cuando cliente gana (para servicios de resultados)
- **Agents selling to agents:** El futuro B2B es AI-to-AI (considerar más adelante)
- **Insight clave:** "If it's not not automatic, it's not scalable" → seguir automatizando

→ Investigación guardada en ~/workspace/research/polsia-analysis.md
→ No requiere action items - Yota es sistema personal, no producto

---

## Etiquetas

- #decision - Decisiones importantes
- #lesson - Aprendizados
- #lead - Leads de Zaltyko
- #config - Configuraciones
- #blocker - Bloqueos
- #trading - Trading crypto
- #workflow - Workflows activos

---

*Última actualización: 2026-03-03*
*Totin 🐻*
