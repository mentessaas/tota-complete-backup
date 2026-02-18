# Shipping at inference‑speed (OpenClaw)

## Principio
Reducir latencia de entrega: tareas pequeñas, verificación automática y rutas claras por fase.

## Reglas operativas
1) **CLI‑first**: todo empieza como comando reproducible.
2) **Plan → Build**: 
   - Plan: modelo potente (decisiones)
   - Build: modelo rápido (iteración)
3) **Loop cerrado**: cada tarea termina con `run/check` (tests/command). Si falla → reintento con logs.
4) **Dependencias mínimas**: decidir lenguaje + deps antes de escribir.
5) **Tareas ≤ 1h**: dividir hasta que quepan.

## Checklist de cierre (obligatorio)
- [ ] Output verificable ejecutado
- [ ] Resultado OK + enlace/log
- [ ] Siguiente paso único definido

## Aplicación en OpenClaw
- Usar agentes Plan/Build con prompts separados.
- Añadir comando de verificación en cada story.
- Evitar cambios masivos sin prueba.
