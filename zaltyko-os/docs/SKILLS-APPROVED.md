# 🔒 Skills Approved List

> Lista de skills verificados para nuestro setup. Actualizado: 2026-02-20

---

## ✅ Skills Verificados (Instalados)

| Skill | Fuente | Función | Revisado |
|-------|--------|---------|----------|
| tavily | Oficial | Búsquedas web | ✅ 2026-02-19 |
| stealth-browser | ClawHub | Scraping anti-detección | ✅ 2026-02-19 |
| brevo | Keys.env | Email outreach | ✅ 2026-02-19 |
| humanizer | ClawHub | Humanizar texto | ✅ 2026-02-19 |
| auto-updater | ClawHub | Updates diarios | ✅ 2026-02-19 |
| gog | NPM | Gmail/Calendar | ✅ Oficial |

| youtube-summarizer | ClawHub (abe238) | Resumir videos | ⚠️ Requiere MCP server extra |

---

## ⚠️ Skills con Precaución

| Skill | Riesgo | Acción requerida |
|-------|--------|------------------|
| Cualquiera de fuente desconocida | ALTO | NO instalar |
| Skills con código exec | MEDIO | Revisar SKILL.md primero |
| Skills de authors no verificados | MEDIO | Buscar reviews primero |

---

## ❌ Skills NO Instalamos

| Reason | Ejemplo |
|--------|---------|
| Código de internet sin verificar | Skills random de GitHub |
| Permisos excesivos | Skills que piden root |
| Sin documentación clara | Skills sin SKILL.md |
| Autores desconocidos | Skills nuevos sin reviews |

---

## 🔍 Cómo Verificar un Skill Antes de Instalar

1. **Revisar SKILL.md completo**
   - Buscar comandos `exec`, `bash`, `curl`
   - Verificar que no hay URLs sospechosas

2. **Buscar en Reddit/Google**
   - "skillname openclaw scam"
   - "skillname openclaw security"

3. **Revisar el repositorio**
   - Si está en GitHub, revisar commits
   - Verificar que no hay código ofuscado

4. **Empezar en modo seguro**
   - Probar en un subagente primero
   - No dar acceso a credenciales inmediatamente

---

## 📋 Checklist Antes de Instalar

- [ ] Revisé SKILL.md completo
- [ ] No hay comandos `curl | bash` o similar
- [ ] Busqué reviews/quejas en internet
- [ ] El autor es verificado o conocido
- [ ] Los permisos son mínimos
- [ ] Tengo approve de Elvis (si es crítico)

---

## 🚨 Si Algo Sale Mal

Si un skill hace algo sospechoso:
1. **Desinstalar inmediatamente**
2. **Revisar logs** en ~/.openclaw/logs/
3. **Reportar** en GitHub de OpenClaw
4. **No ejecutar** comandos que sugiere

---

*Actualizado: 2026-02-20*
*Tota 🐻*
