# 🔄 Protocolo de Handoffs - Zaltyko OS

## Qué es un Handoff

Cuando un agente termina su parte y necesita que otro continúe.

---

## Handoffs Definidos

### 1. Sales → CRM (Nuevo Lead)
```
De: Sales
Para: CRM/Brevo
Trigger: Nuevo lead identificado
Acción: Agregar al CRM + lista Brevo
```

### 2. Sales → Dev (Demo Ready)
```
De: Sales  
Para: Dev
Trigger: Lead qualified, quiere demo
Acción: Preparar demo environment, test login
```

### 3. Sales → Marketing (Content Request)
```
De: Sales
Para: Marketing
Trigger: Lead pregunta por X
Acción: Crear content relevante
```

### 4. Dev → Sales (Feature Ready)
```
De: Dev
Para: Sales
Trigger: Nueva feature lista
Acción: Actualizar pitch en emails
```

### 5. Marketing → Sales (Lead MQL)
```
De: Marketing
Para: Sales
Trigger: Lead de formulário/blog
Acción: Outreach personalizado
```

### 6. Any → CEO (Escalation)
```
De: Cualquiera
Para: CEO
Trigger: Decisión necesaria / Emergencia
Acción: Resolver inmediatamente
```

---

## Formato de Handoff

```
📤 HANDOFF
De: [Agente]
Para: [Agente]
Asunto: [Qué necesitas]
Contexto: [2-3 líneas]
Urgencia: [low/medium/high]
```

---

## Ejemplo

```
📤 HANDOFF
De: Sales
Para: CRM/Brevo
Asunto: Nuevo lead - María García
Contexto: María de Academia Victoria quiere info. 
Email: maria@academiavictoria.es. Tel: 600123456.
Urgencia: medium
```

---

## Reglas

1. ** Siempre especificar urgencia
2. ** Incluir contexto relevante (no todo el history)
3. ** Si no hay respuesta en 1h → re-enviar + escalar a CEO
4. ** Documentar en CRM toda interacción
