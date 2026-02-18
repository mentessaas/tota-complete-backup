# SKILLS MANIFESTO v1.0

**Fecha:** 2026-02-17
**Owner:** Elvis / Tota
**Propósito:** Transformar Tota de chat assistant → agent shell

---

## 📁 Estructura

```
~/.openclaw/skills/
├── manifest/          # Este archivo
├── audit-mac/        # Optimización sistema
├── voicebox/         # TTS local
├── whisper/          # Voz→texto
├── himalaya/         # Email CLI
├── opengoat/         # Agentes IA
├── web-research/     # Búsquedas web
└── file-manager/     # Gestión archivos
```

---

## ⚡ REGLA SHELL

> **Antes de responder, verificar:**
> 1. ¿Tengo la herramienta necesaria instalada?
> 2. ¿Necesito ejecutar algo para obtener la respuesta?
> 3. ¿Debo guardar el output en ~/OUTPUT/?

---

## 📋 CATÁLOGO DE SKILLS

### skill:audit-mac
**Qué hace:** Auditoría y optimización de Mac  
**Cuándo usarlo:** Cuando Elvis pide optimizar, velocidad, memoria  
**Cuándo NO:** Si hay problemas específicos de app (no de sistema)  
**Dependencias:** `top`, `ps`, `df`, `launchctl`  
**Output:** JSON con recomendaciones  

### skill:voicebox  
**Qué hace:** TTS local con Voicebox  
**Cuándo usarlo:** Cuando Elvis quiere generación de voz  
**Cuándo NO:** Si necesita voces múltiples o cloud  
**Dependencias:** Voicebox.app corriendo en localhost:8000  
**Output:** .wav audio file  

### skill:whisper
**Qué hace:** Transcripción de audio a texto  
**Cuándo usarlo:** Cuando recibe audio de Telegram  
**Cuándo NO:** Audio en otro idioma sin especificar  
**Dependencias:** `whisper` CLI  
**Output:** Texto  

### skill:himalaya
**Qué hace:** Gestión de email via IMAP/SMTP  
**Cuándo usarlo:** Resúmenes de inbox, buscar emails  
**Cuándo NO:** Envío de emails urgentes (mejor Telegram)  
**Dependencias:** `himalaya` CLI + config en ~/.config/himalaya/  

### skill:opengoat
**Qué hace:** Orquestación de agentes IA  
**Cuándo usarlo:** Workflows complejos que requieren múltiples pasos  
**Cuándo NO:** Tareas simples de una pregunta  
**Dependencias:** `opengoat` CLI + OpenClaw  

### skill:web-research
**Qué hace:** Búsquedas web con Brave/Groq  
**Cuándo usarlo:** Investigación, facts, news  
**Cuándo NO:** Información personal o local  
**Dependencias:** API key Brave en keys.env  

---

## 📦 ENTREGABLES

**Ubicación:** `~/OUTPUT/`

| Tipo | Formato | Ejemplo |
|------|---------|---------|
| Informes | .md | `~/OUTPUT/audit-2026-02-17.md` |
| Código | .sh | `~/OUTPUT/voice2text.sh` |
| Datos | .json | `~/OUTPUT/leads.json` |
| Audio | .wav | `~/OUTPUT/tts-output.wav` |

---

## ⚠️ FALLAS DOCUMENTADAS

| Skill | Qué falló | Por qué | Fix |
|-------|-----------|---------|-----|
| himalaya | No puede configurar sin credenciales | Usuario no dio datos | Pendiente config manual |
| voicebox | No genera sin sample | Qwen necesita audio de referencia | Grabación pendiente 21:30 |

---

## 🔄 COMPACTACIÓN

Cuando el contexto exceda 20 mensajes:
1. Resumir estado actual
2. Guardar artefactos clave en ~/OUTPUT/
3. Compactar a 5 mensajes relevantes
4. Referenciar artifacts en nuevo contexto

---

**Próximo paso:** Elvis, asigname tareas que se repitan → las convertiré en skills.
