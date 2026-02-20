# Testing Plan - Zaltyko MVP

## Objetivo
Testear todo el sistema antes de primeros clientes. Sin errores.

## Módulos a Testear

### 1. Onboarding Flow
- [ ] Registro nuevo usuario
- [ ] Crear academia
- [ ] Setup inicial (wizard)
- [ ] Login funciona

### 2. Athlettes
- [ ] Crear atleta
- [ ] Editar atleta
- [ ] Asignar a grupo
- [ ] Ver perfil atleta

### 3. Grupos y Clases
- [ ] Crear grupo
- [ ] Crear clase
- [ ] Asignar atletas a clase
- [ ] Ver calendario

### 4. Asistencia
- [ ] Registrar asistencia
- [ ] Historial por atleta
- [ ] Reporte por clase

### 5. Pagos (Stripe)
- [ ] Checkout funciona
- [ ] Payment success
- [ ] Payment failed
- [ ] Factura generada

### 6. Notificaciones
- [ ] Email welcome
- [ ] In-app notification
- [ ] Parent portal access

### 7. Páginas Públicas
- [ ] /academias - directorio carga
- [ ] /events - eventos carga
- [ ] /academias/[id] - perfil público
- [ ] /events/[id] - evento público

### 8. Mobile/Responsive
- [ ] Dashboard funciona en móvil
- [ ] Forms funcionan en móvil

## Errores a Buscar
- UI/UX bugs
- Errores de consola
- Links rotos
- Forms que no submiten
- API errors
- Auth issues

## Formato de Reporte

```markdown
## [Módulo] - STATUS

### Tests:
- [PASS/FAIL] Test name

### Issues:
1. Issue name
   - Severity: HIGH/MEDIUM/LOW
   - Steps to reproduce
   - Fix suggested
```
