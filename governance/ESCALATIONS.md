# 🚨 Protocolo de Escalamiento - Zaltyko OS

## Cuándo Escalar

Escala a CEO inmediatamente si:

1. **Urgente**: Sitio caído, error crítico
2. **Decisión**: Necesita aprobación de negocio
3. **Bloqueo**: Sin respuesta > 30 min
4. **Riesgo**: Posible daño a negocio/cliente

---

## Niveles de Urgencia

| Nivel | Definición | Tiempo de respuesta |
|-------|------------|---------------------|
| 🔴 HIGH | Sitio caído, cliente furioso | Inmediato |
| 🟡 MEDIUM | Decisión de negocio | 30 min |
| 🟢 LOW | Pregunta, consulta | 2 horas |

---

## Formato de Escalamiento

```
🚨 ESCALATION
De: [Agente]
Nivel: [HIGH/MEDIUM/LOW]
Asunto: [Qué pasa]
Impacto: [Qué pasa si no se resuelve]
Requested: [Qué necesitas de CEO]
```

---

## Ejemplos

###HIGH - Sitio Caído
```
🚨 ESCALATION
De: Dev
Nivel: HIGH
Asunto: Zaltyko no responde
Impacto: No podemos hacer demos, perdemos leads
Requested: Decidir si hacer rollback o esperar
```

### MEDIUM - Cambio de Pricing
```
🚨 ESCALATION  
De: Sales
Nivel: MEDIUM
Asunto: Lead pide descuento 50%
Impacto: €15 vs €29/mes
Requested: Aprobar descuento?
```

---

## Rules

1. **No cry wolf** - Solo escalar si es necesario
2. **Tener solución lista** - No solo reportar, proponer
3. **Documentar** - Todo escalamiento va al log
