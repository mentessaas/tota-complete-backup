# FEEDBACK SYSTEM - Sistema de Evolución

## Overview
Sistema automático de logging, análisis y evolución de mis acciones.

---

## Componentes

### 1. Logger (feedback_log.py)
Registra cada acción con resultado.
```bash
python3 ~/zaltyko-os/scripts/feedback_log.py <type> <result> <details>
```

### 2. Analyzer (feedback_analyze.py)
Analiza patrones y propone mejoras.
```bash
python3 ~/zaltyko-os/scripts/feedback_analyze.py [type] [days]
```

### 3. Metrics (metrics.py)
KPIs en dashboard simple.
```bash
python3 ~/zaltyko-os/scripts/metrics.py [days]
```

---

## Tipos de Feedback

| Type | Result values | Details |
|------|---------------|---------|
| trade | success, failure, partial | symbol, pnl, reason |
| email | sent, opened, replied, bounced | template, subject, lead |
| lead | valid, invalid, converted | source, city, quality |
| job | success, error, timeout | job_name, error_type |

---

## Integración con Jobs

### Después de cada trade:
```bash
python3 ~/zaltyko-os/scripts/feedback_log.py trade <result> "symbol:BTC,pnl:+2%"
```

### Después de cada email:
```bash
python3 ~/zaltyko-os/scripts/feedback_log.py email reply "template:A"
```

### Después de cada lead:
```bash
python3 ~/zaltyko-os/scripts/feedback_log.py lead valid "source:web"
```

### Después de cada job:
```bash
python3 ~/zaltyko-os/scripts/feedback_log.py job success "job:healthcheck"
```

---

## Dashboard

Se genera en: `~/zaltyko-os/feedback/metrics_latest.json`

---

## Próximos Pasos

1. [x] Crear scripts de logging
2. [x] Crear analyzer
3. [ ] Integrar en jobs existentes
4. [ ] Crear dashboard visual
5. [ ] Auto-ajuste de parámetros

---

*2026-02-25*
