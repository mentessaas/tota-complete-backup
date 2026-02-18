# Skills Security Policy

## Regla base
- Solo instalar skills auditadas o de fuente conocida.

## Checklist antes de instalar
- [ ] Origen verificado (repo/autor/URL)
- [ ] No ejecuta scripts externos sin verificación
- [ ] Permisos mínimos (sin acceso a secretos por defecto)
- [ ] Descripción clara de acciones
- [ ] Alternativa sin skill si es posible

## Bloqueos por defecto
- No instalar skills que descargan y ejecutan scripts remotos.
- No instalar skills sin README claro o sin mantenimiento.

## Proceso
1) Evaluar
2) Aprobación explícita de Elvis
3) Instalar
4) Revisar comportamiento en entorno de prueba
