# PROMPT EVOLUTION.md - Evolución de prompts

## Propósito
Trackear prompts, su rendimiento, e iterar automáticamente.

---

## Prompts Activos

### Trading
| Prompt | ID | Éxito | Última actualización |
|--------|-----|-------|---------------------|
| Signal Analyzer | trading_signal_v1 | 60% | 2026-02-24 |
| Risk Manager | risk_v1 | 95% | 2026-02-23 |

### Email
| Prompt | ID | Éxito | Última actualización |
|--------|-----|-------|---------------------|
| Outreach Template A | email_outreach_v1 | 15% | 2026-02-24 |
| Outreach Template B | email_outreach_v2 | 8% | 2026-02-23 |

### Leads
| Prompt | ID | Éxito | Última actualización |
|--------|-----|-------|---------------------|
| Research Scout | lead_scout_v1 | 70% | 2026-02-24 |
| Validation | lead_validate_v1 | 85% | 2026-02-23 |

---

## Mejoras Pendientes

### Alta Prioridad
- [ ] **email_outreach_v1**: <20% reply rate → Probar subject lines diferentes
- [ ] **trading_signal_v1**: Optimizar timing de entrada

### Testing
- [ ] Probar variation de signal para trend detection
- [ ] Test A/B de templates de email

---

## Historial de Cambios

### 2026-02-25
- Creado sistema de feedback
- Logging automático de trades, emails, leads, jobs
- Análisis semanal automático

---

##Cómo usar

```bash
# Loggear resultado
python3 ~/zaltyko-os/scripts/feedback_log.py trade success "BTC long +2%"
python3 ~/zaltyko-os/scripts/feedback_log.py email reply "Template A"
python3 ~/zaltyko-os/scripts/feedback_log.py lead valid "Madrid"

# Analizar
python3 ~/zaltyko-os/scripts/feedback_analyze.py all 7
```

---

*Actualizado: 2026-02-25*
