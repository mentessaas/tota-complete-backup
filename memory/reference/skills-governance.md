# Skills Governance (OpenClaw)

## Objetivo
Estandarizar creación, activación y control de skills para evitar caos, duplicidad y riesgos.

## Convenciones (obligatorio)
- **Ruta estándar**: `~/.openclaw/skills/<skill>/SKILL.md`
- **Nombre**: minúsculas, guiones, ≤64 chars.
- **Frontmatter mínimo**: `name`, `description`.
- **Task skills**: `disable-model-invocation: true` por defecto.
- **Herramientas**: declarar `allowed-tools` (mínimo necesario).
- **Subagente**: usar `context: fork` si la tarea es pesada o multi‑paso.

## Niveles y prioridad
1) Enterprise (si existiera)
2) Personal (global)
3) Proyecto
4) Plugin (namespace `plugin:skill`)

## Activación (checklist)
- [ ] Fuente auditada y confiable
- [ ] Descripción clara + casos de uso
- [ ] Herramientas mínimas declaradas
- [ ] No ejecuta scripts externos sin verificación
- [ ] Añadida al **skills-registry.md**

## Mantenimiento
- Revisar trimestralmente: skills obsoletas / duplicadas.
- Si una skill falla 2 veces seguidas: se desactiva hasta fix.
