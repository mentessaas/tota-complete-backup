# Zaltyko — QA Onboarding Test

Fecha: 2026-02-20 19:00 (Europe/Madrid)
URL: https://zaltyko.vercel.app/onboarding

## Credenciales usadas
- Email: test-onboarding-1771610425@test.com
- Password: QA-Test-2026!

## Resultado
**FAIL**

## Pasos ejecutados
1) Abrí /onboarding (Paso 1 de 2).
2) Rellené:
   - Nombre completo: `QA Onboarding Test`
   - Correo: `test-onboarding-1771610425@test.com`
   - Contraseña / confirmación: `QA-Test-2026!`
3) Click en **“Crear cuenta y continuar”**.

## Errores encontrados
### 1) Registro falla con mensaje genérico
- Observado: aparece notificación **“Error al registrar”** con detalle **`INTERNAL_ERROR`**.
- Impacto: bloquea onboarding (no se puede pasar al paso 2, no se crea la cuenta).

### 2) Redirección / sesión inconsistente → Dashboard rompe
- Tras intentar ir a **/auth/login**, el sistema redirige a **/dashboard**, pero la página muestra:
  - **“Algo salió mal”**
  - “Ha ocurrido un error inesperado. Por favor, intenta recargar la página.”
- Repetido al navegar de nuevo a /auth/login (otra vez redirige a /dashboard y vuelve el error).
- Impacto: incluso si hay sesión/cookie parcial, la app termina en error boundary en dashboard.

## Evidencia
- Screenshot: capturado en el flujo (pantalla “Algo salió mal” en /dashboard).

## Notas
- No fue posible completar el wizard (Paso 2) ni verificar login exitoso debido a `INTERNAL_ERROR` en registro y error boundary en /dashboard.
