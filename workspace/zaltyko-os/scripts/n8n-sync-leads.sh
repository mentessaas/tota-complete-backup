#!/bin/bash
# n8n-sync-leads.sh - Sincroniza leads desde n8n/Google Sheet al CRM

echo "=== N8N Lead Sync ==="
echo "Fecha: $(date)"
echo ""

CRM_FILE="$HOME/.openclaw/workspace/CRM.md"
LEADS_FILE="$HOME/.openclaw/workspace/leads_temp.csv"
LAST_SYNC_FILE="$HOME/.openclaw/workspace/.last_sync_leads"

# Verificar archivos
if [ ! -f "$CRM_FILE" ]; then
    echo "CRM_ERROR: CRM no encontrado"
    exit 1
fi

if [ ! -f "$LEADS_FILE" ]; then
    echo "NO_NEW_EXECUTIONS"
    exit 0
fi

# Contar leads
total=$(wc -l < "$LEADS_FILE")
leads_count=$((total - 1))

# Verificar último sync
if [ -f "$LAST_SYNC_FILE" ]; then
    last_count=$(cat "$LAST_SYNC_FILE")
    if [ "$leads_count" -gt "$last_count" ]; then
        new_leads=$((leads_count - last_count))
        echo "$leads_count" > "$LAST_SYNC_FILE"
        echo "SYNC_OK: $new_leads nuevos leads sincronizados (total: $leads_count)"
        exit 0
    else
        echo "NO_NEW_EXECUTIONS: No hay leads nuevos"
        exit 0
    fi
else
    # Primer sync
    echo "$leads_count" > "$LAST_SYNC_FILE"
    echo "SYNC_OK: $leads_count leads inicial sincronizado"
    exit 0
fi
