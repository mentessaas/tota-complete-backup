#!/bin/bash
# brevo-health.sh - Verifica estado de Brevo

echo "=== Brevo Health Check ==="
echo "Fecha: $(date)"
echo ""

# Verificar API key
if [ -z "$BREVO_API_KEY" ]; then
    echo "❌ BREVO_API_KEY no está configurada"
    exit 1
fi

# Verificar conexión a API
response=$(curl -s -w "%{http_code}" -o /tmp/brevo_response.json \
    -H "Api-Key: $BREVO_API_KEY" \
    -H "Content-Type: application/json" \
    "https://api.brevo.com/v3/account")

http_code="${response: -3}"
body=$(cat /tmp/brevo_response.json)

if [ "$http_code" = "200" ]; then
    echo "✅ Conexión a Brevo: OK"
    
    # Extraer info de cuenta
    email=$(echo "$body" | grep -o '"email":"[^"]*"' | head -1 | cut -d'"' -f4)
    echo "📧 Cuenta: $email"
    
    # Ver listas
    lists=$(curl -s -H "Api-Key: $BREVO_API_KEY" "https://api.brevo.com/v3/contacts/lists?limit=10")
    count=$(echo "$lists" | grep -o '"count":[0-9]*' | cut -d':' -f2)
    echo "📋 Listas: $count"
    
    echo ""
    echo "✅ Health check PASSED"
    exit 0
else
    echo "❌ Error conectando a Brevo (HTTP $http_code)"
    echo "Response: $body"
    exit 1
fi
