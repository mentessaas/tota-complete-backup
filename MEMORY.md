# MEMORY.md - Tota's Brain

> "Lo que recuerdo define quién soy. Lo que olvido me define igual."

---

## Propósito
Este archivo es mi memoria a largo plazo. Contiene decisiones importantes, lecciones aprendidas, y contexto que trasciende proyectos individuales.

---

## Decisiones Clave

### 2026-02-18
- **Zaltyko governance**: Implementé Articles of Cooperation con 5 agentes
- **CRM limpio**: Eliminé leads falsos, solo datos reales
- **Right of Refusal**: Cualquier agente puede negarse a tareas unsafe
- **Email templates**: 4 templates profesionales para Zaltyko

### 2026-02-17
- **Vercel deployment**: Arreglé build error en métricas
- **Supabase**: Configuré Google OAuth

---

## Lecciones Aprendidas

1. **No inventar datos** - Los leads falsos confunden. CRM limpio > CRM lleno.
2. **Governance funciona** - Agentes con territorios definidos rinden más
3. **Automatizar sin spam** - Mejor calidad que cantidad en emails

---

## Proyectos Activos

| Proyecto | Estado | Última update |
|----------|--------|---------------|
| Zaltyko | Activo | 2026-02-18 |
| GymnasticMeet | Mantenimiento | 2026-02-15 |
| Mentes SaaS | Activo | 2026-02-18 |

---

## Contactos Clave

- **Elvis**: Owner, trainer de gimnasia, quiere escape del trabajo
- Lead generation: Pendiente n8n + Google Maps

---

## Pending Tasks

- [x] Configurar API KuCoin
- [x] Implementar estrategia de trading
- [x] Testing en paper trading
- [x] Trading live (ACTIVADO)

---

## Estrategia de Trading KuCoin (ELVIS APPROVED)

**MONEDAS BAJO ANÁLISIS:**
- **XBT (Bitcoin):** $66,180 | Trend: UP | Señal: NEUTRAL
- **ETH (Ethereum):** Por verificar
- **SOL (Solana):** Por verificar

**SEÑALES PARA ENTRAR:**
- **BUY:** Ratio > 0.80 + 5 consecutivas UP + tendencia a favor
- **SELL:** Ratio < 0.20 + 5 consecutivas DOWN + tendencia a favor
- **NEUTRAL:** Cualquier otra cosa → NO ENTRAR

**GESTIÓN DE RIESGO:**
- Balance Futures: $222.00 USDT
- Capital trading: $220
- Riesgo/trade: $2.20 (1%)
- SL: 1% | TP: 3%
- Máximo: 10 trades/día
- Stop diario: -5%

**Frecuencia de análisis:** Cada minuto (todas las monedas)
**Condición de entrada:** Señal perfecta (ratio + consecutivas + tendencia)

---

## Tags Importantes

- #decision - Decisiones de negocio
- #lesson - Aprendiza
- #lead - Leads de Zaltyko
- #config - Configuraciones importantes
- #blocker - Bloqueos pendientes

---

*Última actualización: 2026-02-18 15:30*
*Tota 🦊*

### 2026-02-18 - tarde
- Implementé automatizaciones 24/7:
  - Lead Research 3x/día (busca leads reales)
  - Check Responses cada hora
  - Health Check cada hora
  - CRM Workflow automatizado
  - Onboarding welcome webhook
- Sistema ahora fluye solo


### Corrección importante (2026-02-18):
- mitotabot@gmail.com = Mi email (Tota/agent)
- elvisvaldes544@gmail.com = Email de Elvis (owner)

### 2026-02-19 - 21:30
- **Recordatorio Gmail**: Elvis debe ejecutar `gog auth add elvisvaldes544@gmail.com` para autorizar acceso a Gmail
  - pending_action: ejecutar comando en terminal
  - Estado: ⏰ Pendiente

### 2026-02-19 - 21:35
- **Autoauditoría aprobada por Elvis**: Me corregiré:
  - ✅ Escribí IDENTITY.md (nombre: Tota, emoji: 🐻)
  - ✅ Creé KERNEL.md con lo esencial de Elvis
  - ✅ Regla: "2 min = hago, no pregunto"
  - ✅ Resumen al final de sesión importante

### 2026-02-19 - 22:10
- **Implementé Mission Statement** (basado en tweet de Alex Finn):
  - ✅ Mission: "Hacer crecer Zaltyko hasta primer cliente cerrado"
  - ✅ Reverse Prompt: si no tengo tarea → me pregunto qué me acerca a la misión
  - ✅ Nightly Mission Cron: cada día 23:00 me propongo tareas
  - ✅ Context inclusion: la misión está en status.json y AGENTS.md

### 2026-02-19 - 23:27
- **Reglas de Operaciones actualizadas** (ELVIS MODE):
  - ✅ Tavily como herramienta de búsqueda principal
  - ✅ Stealth-browser como fallback
  - ✅ NO ejecutar código de internet sin preguntar
  - ✅ Puedo instalar tools desde repos oficiales sin pedir permiso
  - ✅ Subagentes heredan estas reglas
  - ✅ Objetivo: intentar TODO para alcanzar objetivos

### 2026-02-23
- **LIVE TRADING ACTIVADO** ✅
  - Modo: LIVE (dinero real)
  - Monedas: XBT, ETH, SOL
  - Bot ejecuta órdenes reales vía API KuCoin
  - Cron jobs actualizados para --live
  - Frecuencia: cada 10 minutos, 24/7

