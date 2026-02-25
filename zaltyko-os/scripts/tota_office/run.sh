#!/bin/bash
# Tota Office - Launcher

cd "$(dirname "$0")"

echo "🏢 TOTA OFFICE"
echo "=============="
echo ""

# Check dependencies
echo "📦 Verificando dependencias..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 no encontrado"
    exit 1
fi

# Check websockets
python3 -c "import websockets" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "📥 Instalando websockets..."
    pip3 install websockets
fi

# Start server in background
echo "🚀 Iniciando servidor..."
python3 server.py &
SERVER_PID=$!

# Wait for server to start
sleep 2

# Open in browser
echo "🌐 Abriendo en navegador..."
open http://localhost:8080

# Simple HTTP server for static files
echo "📡 Iniciando servidor HTTP..."
python3 -m http.server 8080 &
HTTP_PID=$!

echo ""
echo "✅ TOTA OFFICE ABIERTO!"
echo "🌐 http://localhost:8080"
echo ""
echo "Presiona Ctrl+C para detener."
echo ""

# Keep running
trap "kill $SERVER_PID $HTTP_PID 2>/dev/null; echo '👋 Oficina cerrada'; exit" INT TERM

wait
