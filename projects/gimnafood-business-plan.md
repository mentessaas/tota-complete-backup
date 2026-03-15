# 📋 Plan de Negocio: GimnaFood
## App de Nutrición para Gimnastas

> Fecha: 2026-03-04
> Versión: 1.0

---

## 1. Producto

### 1.1 Concepto
**GimnaFood** - La primera app de nutrición diseñada específicamente para gimnastas (rítmica, artística,trampolín)

### 1.2 Propuesta de Valor
> "Nutrición diseñada por expertos para gimnastas, no para atletas cualquiera"

### 1.3 Features MVP

| Feature | Prioridad | Descripción |
|---------|-----------|-------------|
| **Foto → Nutrition AI** | P0 | Foto comida → calories + macros + consejos |
| **Recetas gimnastas** | P0 | Recetas赛前/赛后 específicas |
| **Seguimiento peso** | P0 | Tracking peso + evolución |
| **Calendario competencias** | P1 | Alertas赛前 preparación |
| **Perfil gimnasta** | P1 | Edad, categoría, nivel |
| **Guía nutricional** | P2 | Artículos赛前/赛后 |
| **Comunidad** | P2 | Forum gimnastas |

### 1.4 Features V2+

- Integración wearables (Fitbit, Apple Watch)
- Chat con nutricionista
- Planes personalizados
- Integración academias (CRM)
- Modo offline

---

## 2. Tecnología

### 2.1 Tech Stack

| Capa | Tecnología | Justificación |
|------|------------|---------------|
| **Mobile** | React Native | iOS + Android, 1 código |
| **Backend** | Supabase | Postgres + Auth + Storage + Edge Functions |
| **AI** | OpenAI Vision API | Foto → nutrition analysis |
| **Analytics** | PostHog | Product analytics |
| **Payments** | Stripe | Suscripciones |
| **Email** | Resend | Transaccional |
| **Hosting** | Vercel | Frontend |

### 2.2 Arquitectura

```
┌─────────────────────────────────────────┐
│           React Native App              │
│  (iOS + Android)                        │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│              Vercel                       │
│  (API Routes + SSR)                      │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│            Supabase                       │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  │
│  │ Auth    │  │ DB      │  │ Storage │  │
│  └─────────┘  └─────────┘  └─────────┘  │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│          OpenAI Vision API               │
│  (Image → Nutrition Analysis)            │
└─────────────────────────────────────────┘
```

### 2.3 Costos Mensuales Estimados

| Servicio | Fase MVP | Fase Growth |
|----------|----------|-------------|
| Supabase | €0 (free) | €50 |
| OpenAI | €100 | €500 |
| Vercel | €0 (free) | €20 |
| Stripe | 0% + fees | 0% + fees |
| **Total** | **€100/mes** | **€570/mes** |

### 2.4 Desarrollo

| Fase | Tiempo | Estimación |
|------|--------|------------|
| MVP | 8-12 semanas | €3,000-5,000 (outsource) o propio |
| V1 | 4 semanas extra | - |
| V2 | 8 semanas extra | - |

---

## 3. Modelo de Negocio

### 3.1 Revenue Streams

| Stream | % Revenue | Descripción |
|--------|-----------|-------------|
| **Suscripciones** | 80% | Freemium → Premium |
| **Nutricionista** | 15% | Consultas 1:1 |
| **Academias** | 5% | Planes para clubs |

### 3.2 Pricing

| Tier | Precio | Features |
|------|--------|----------|
| **Free** | €0 | - Seguimiento básico<br>- 10 fotos AI/mes<br>- Recetas básicas |
| **Pro** | €6.99/mes | - Ilimitado AI<br>- Todas recetas<br>- Calendario competencias<br>- Seguimiento peso |
| **Elite** | €14.99/mes | - Todo Pro<br>- Chat nutricionista<br>- Planes personalizados<br>- Priority support |

### 3.3 Proyección Revenue

| Año | Usuarios | MRR | Notas |
|-----|----------|-----|-------|
| 1 | 10,000 | €3,000 | Spain launch |
| 2 | 50,000 | €25,000 | Europa |
| 3 | 200,000 | €120,000 | Global |

---

## 4. Estrategia

### 4.1 Go-to-Market

**Fase 1: España (Meses 1-6)**
- Academia de RG como partners
- Influencers gimnastas
- Content marketing

**Fase 2: Europa (Meses 7-12)**
- España → Portugal → Italia → Francia
- Translator localization
- Partnerships federaciones

**Fase 3: Global (Año 2)**
- English + Español
- Mercados anglosajones

### 4.2 Canales Adquisición

| Canal | % Budget | ROI Esperado |
|-------|----------|--------------|
| TikTok/IG Ads | 40% | 2.5x |
| Influencers | 30% | 3x |
| Content SEO | 20% | 5x |
| PR/Prensa | 10% | 2x |

### 4.3 Partnerships

- **Federaciones** - Oficialidad = confianza
- **Academias** - Canal de distribución
- **Nutricionistas** - Credibilidad + revenue
- **Marcas sports** - Patrocinio

---

## 5. Marketing

### 5.1 Branding

**Nombre:** GimnaFood

**Logotipo:** (diseñar)
- G + Fork + Ribbon (gimnasia)
- Colores: Morado (#6B46C1) + Verde (#10B981)

**Tono:**
- Profesional pero cercano
- Empoderante
- No intimidante

**Messaging:**
- "Come como una campeón"
- "Tu nutrition, tu rendimiento"
- "Diseñado por gimnastas, para gimnastas"

### 5.2 Canales

| Canal | Focus | Formato |
|-------|-------|---------|
| **TikTok** | Virality | Before/after, tips, recetas |
| **Instagram** | Comunidad | Reels, stories, carousel |
| **YouTube** | Profundidad | Tutorials, entrevistas |
| **Podcast** | Autoridad | Gimnastas + nutricionistas |
| **Blog SEO** | Organic | Recetas, guías |

### 5.3 Content Strategy

**Pilar 1: Nutrition Tips**
- "Qué comer antes de competir"
- "Cómo mantener peso en temporada"
- "Recetas赛前 30 min"

**Pilar 2: Entrevistas**
- Gimnastas profesionales
- Nutricionistas deportivos

**Pilar 3: Virality**
- Challenges (#GimnaFoodChallenge)
- User Generated Content

### 5.4 Kpis Marketing

| KPI | Mes 1 | Mes 6 | Año 1 |
|-----|-------|-------|-------|
| Downloads | 1,000 | 10,000 | 50,000 |
| DAU/MAU | 20% | 30% | 35% |
| CAC | €5 | €3 | €2 |
| LTV | €20 | €40 | €60 |

---

## 6. Operaciones

### 6.1 Equipo MVP

| Rol | Modalidad | Costo |
|-----|-----------|-------|
| Founder/CEO | Elvis | - |
| Developer | Outsourced | €3,000 |
| Designer | Fiverr | €500 |
| Community | Founder | - |

### 6.2 Nutricionistas

- 2-3 nutricionistas deportivos como advisors
- Modelo revenue share en consultas

### 6.3 Legal

- RGPD compliant
- Términos de uso
- Disclaimer médico

---

## 7. Riesgos y Mitigación

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|-------------|
| Competidor grande copia | Media | Alto | First mover + comunidad |
| AI costs失控 | Alta | Medio | Limits, caching |
| Churn alto | Media | Alto | Comunidad, features |
| Regulation nutrition | Baja | Medio | Disclaimer claro |

---

## 8. Timeline

### 2026 Q1-Q2: Build
- [ ] Semana 1-2: Research + Spec
- [ ] Semana 3-8: MVP Development
- [ ] Semana 9-10: Beta (50 users)
- [ ] Semana 11-12: Launch prep

### 2026 Q3: Launch España
- [ ] Soft launch (1,000 users)
- [ ] Iterate based on feedback
- [ ] First paid conversions

### 2026 Q4: Scale
- [ ] 10,000 users
- [ ] First partnerships
- [ ] Prepare Europe

---

## 9. Next Steps

1. [ ] Validar con gimnastas reales (entrevistas)
2. [ ] Crear landing page + waitlist
3. [ ] Diseñar UI/UX
4. [ ] Desarrollar MVP
5. [ ] Beta test con 50 gimnastas

---

## 10. Preguntas Abiertas

- ¿Nombre "GimnaFood" o diferente?
- ¿Pricing correcto?
- ¿Priorizar iOS o Android primero?
- ¿Build propio o outsource?

---

*Plan de negocio v1.0 - 2026-03-04*
*Para validar y iterar*
