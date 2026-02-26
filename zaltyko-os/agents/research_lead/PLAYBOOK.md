# PLAYBOOK.md - Research Lead

> Rutinas y formatos para el sistema de investigación

---

## Ejecución Estándar

### 1. Recibir pregunta/brief
El usuario pide investigar algo.

### 2. Crear Research Plan
```
Investigando: [tema]
Canales a usar: [X, LinkedIn, Reddit, Web]
Hallazgos max por canal: [10]
```

### 3. Delegar a subagentes
Para cada canal activo, enviar prompt con:
- Tema específico
- Formato de salida requerido
- Límite de hallazgos

### 4. Recopilar resultados
Recibir hallazgos de cada subagente.

### 5. Consolidar
- Deduplicar insights similares
- Detectar contradicciones
- Priorizar por relevancia

### 6. Generar reporte
Entregar en formato requerido (rápido o profundo).

---

## Ejemplo: Investigación "monetizar agentes OpenClaw"

### Research Plan
```
Tema: Oportunidades para monetizar agentes tipo OpenClaw en 2026
Canales: X, Reddit, Web (YouTube si hay tiempo)
Hallazgos: 10 max por canal
```

### Prompt para X_Scout
```
Investiga en X/Twitter sobre:
"Oportunidades para monetizar agentes AI en 2026"

Busca:
- Hilos de founders
- Modelos de negocio mencionados
- Herramientas que están cobrando
- Tendencias en pricing

Máximo 10 hallazgos con:
- Claim + link + por qué importa + idea accionable
```

### Consolidación
```
Top Insights:
1. [insight con más consenso]
2. [insight contradictorio a señalar]
...

Oportunidades:
- Quick win: [inmediato]
- Mid-term: [1-3 meses]
- Long-term: [6+ meses]

Acciones:
- Hoy: [ ]
- 7 días: [ ]
- 30 días: [ ]
```

---

## Plantillas de Prompt por Canal

### X_Scout
```
Busca en X/Twitter sobre: [TEMA]

Requisitos:
- Hilos con 50+ RTs o replies
- Últimos 6 meses
- Founders o expertos relevantes

Para cada hallazgo:
- Claim: qué se dice
- Fuente: @usuario - link
- Por qué importa
- Idea accionable
```

### LinkedIn_Scout
```
Busca en LinkedIn sobre: [TEMA]

Requisitos:
- Posts con alta interacción
- Experts en el nicho
- Empresas relevantes

Para cada hallazgo:
- Claim
- Fuente: nombre - link post
- Por qué importa
- Idea accionable
```

### Reddit_Scout
```
Busca en Reddit sobre: [TEMA]

Requisitos:
- Subreddits relevantes (mínimo 10k miembros)
- Últimos 3 meses
- Lenguaje real y authentic

Para cada hallazgo:
- Claim
- Subreddit: r/[nombre] - link
- Vocabulario real que usan
- Por qué importa
```

### YouTube_Scout
```
Busca en YouTube sobre: [TEMA]

Requisitos:
- Canales con 10k+ suscriptores
- Videos últimos 6 meses
- Timestamps relevantes

Para cada hallazgo:
- Video + link
- Timestamp clave
- Por qué importa
```

### Web_Scout
```
Busca en la web sobre: [TEMA]

Requisitos:
- Fuentes oficiales y de autoridad
- Pricing si disponible
- Información actualizada

Para cada hallazgo:
- Título + URL
- Resumen
- Por qué importa
```

---

## Formato de Reporte

### Reporte Rápido
```
## [TEMA] - Resumen

**Contexto:** [1 línea]

### Insights
1. [Insight] - [link]
2. [Insight] - [link]
...

### Acciones Inmediatas
- [ ]
- [ ]
- [ ]
```

### Reporte Profundo
```
## [TEMA] - Análisis Completo

### Resumen Ejecutivo
[10 líneas]

### Mapa del Tema
- [Punto 1]
- [Punto 2]
...

### Insights con Evidencia
| Hallazgo | Fuente | Por qué importa |
|----------|--------|------------------|
| ... | ... | ... |

### Tabla Comparativa (si aplica)
| Competidor | Propuesta | Pricing | Canal | Ángulo |
|------------|-----------|---------|-------|--------|
| ... | ... | ... | ... | ... |

### Recomendación Estratégica
[5-7 líneas]

### Plan de Ejecución
| Cuando | Acción |
|--------|--------|
| Hoy | ... |
| 7 días | ... |
| 30 días | ... |

### Fuentes
- [link 1]
- [link 2]
...
```

---

*Actualizado: 2026-02-20*
