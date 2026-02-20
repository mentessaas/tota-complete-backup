# Investigación: OpenClaw Tips & Tricks

**Fecha:** 2026-02-20
**Tipo:** Mejores prácticas

---

## Top Tips para OpenClaw

### 1. Model Routing Automático
Usar modelo cheap para tareas simples (M2.1) y expensive solo para complejo

### 2. Memory Management
Mantener MEMORY.md actualizado con decisiones clave

### 3. Subagentes Especializados
Crear agentes por tarea (research, outreach, coding)

### 4. Crons con Modelo Barato
Tareas automáticas = M2.1 para ahorrar

### 5. Skills Only Trusted
Solo instalar skills verificados - seguridad primero

### 6. HEARTBEAT Patterns
Usar HEARTBEAT.md para tareas proactivas

### 7. Workflows Encadenados
Un cron activa a otro para sequences

### 8. Context Injection
Incluir siempre misión en prompts de agentes

### 9. Delivery Targets
Configurar bien delivery para cada cron

### 10. Backup Automático
Git backup diario de workspace

---

## Configuraciones Recomendadas

| Área | Recomendación |
|------|---------------|
| Default model | M2.1 para routine, M2.5 para análisis, Codex para code |
| Timeout crons | Mínimo 120s para research, 60s para checks |
| Memory files | SOUL, MEMORY, KERNEL, AGENTS, HEARTBEAT |
| Cron frequency | Máximo cada 2h para no saturar |
| Delivery | Telegram para alerts, announce para reports |

---

## Mejoras para Nuestro Setup

### Implementar:
- [ ] Revisar model routing de todos los crons
- [ ] Verificar que usan M2.1 donde corresponde
- [ ] Crear workflow encadenado (research → outreach)
- [ ] Mejorar delivery configuration

### Mantener:
- ✅ Memory files actualizados
- ✅ Skills verificados
- ✅ Backup diario
- ✅ HEARTBEAT.md

---

## Fuentes

- https://www.reddit.com/r/AiForSmallBusiness/comments/1r4uyrh/the_ultimate_openclaw_setup_guide/
- https://corpwaters.substack.com/p/the-ultimate-guide-to-openclaw
- https://www.foxessellfaster.com/blog/openclaw-setup-guide-how-i-built-my-own-ai-agent-complete-2026-tutorial/
- https://setupopenclaw.com/blog/advanced-openclaw-workflows.html
