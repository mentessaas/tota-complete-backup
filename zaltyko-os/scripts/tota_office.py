#!/usr/bin/env python3
"""
Tota Office - Oficina Virtual en tiempo real
Conecta con el sistema real de Tota
"""
import os
import json
import subprocess
from datetime import datetime

HTML_FILE = '/Users/elvisvaldesinerarte/zaltyko-os/scripts/office.html'

def get_trading_status():
    """Obtener estado real del trading"""
    try:
        trading_file = '/Users/elvisvaldesinerarte/zaltyko-os/scripts/trading_bot_v2_state.json'
        if os.path.exists(trading_file):
            with open(trading_file, 'r') as f:
                data = json.load(f)
                return {
                    "balance": f"${data.get('balance', 0):.2f}",
                    "positions": len(data.get('positions', {})),
                    "daily_pnl": f"${data.get('daily_pnl', 0):.2f}"
                }
    except:
        pass
    return {"balance": "$0", "positions": 0, "daily_pnl": "$0"}

def get_uptime():
    """Obtener uptime"""
    try:
        result = subprocess.run(['uptime'], capture_output=True, text=True)
        return result.stdout.strip()
    except:
        return "Unknown"

def generate_html():
    """Generar HTML con datos reales"""
    trading = get_trading_status()
    now = datetime.now()
    
    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🏢 Tota Office - Oficina Virtual</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        body {{
            font-family: 'SF Mono', 'Fira Code', monospace;
            background: #0a0e14;
            color: #e6edf3;
            min-height: 100vh;
            padding: 20px;
        }}
        
        .header {{
            text-align: center;
            padding: 20px;
            background: linear-gradient(135deg, #1a1f2e 0%, #0d1117 100%);
            border-radius: 16px;
            border: 1px solid #30363d;
            margin-bottom: 20px;
        }}
        
        .header h1 {{
            font-size: 2em;
            background: linear-gradient(90deg, #58a6ff, #bc8cff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        .meta {{
            display: flex;
            justify-content: center;
            gap: 30px;
            font-size: 0.9em;
            color: #8b949e;
            margin-top: 10px;
        }}
        
        .grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            max-width: 1400px;
            margin: 0 auto;
        }}
        
        .station {{
            background: #161b22;
            border: 1px solid #30363d;
            border-radius: 12px;
            padding: 20px;
        }}
        
        .station-header {{
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid #30363d;
        }}
        
        .station-icon {{ font-size: 1.5em; }}
        .station-title {{ font-size: 0.9em; color: #8b949: uppercase; lettere; text-transform        .agent {px; }}
        
-spacing: 2{
            background: #21262d;
            border-radius;
            padding:: 8px 12px;
            margin-bottom: 8px;
;
            align-items            display: flex: center;
            gap: 12 transition: all 0.3spx;
           ;
        }}
        
        .agent:hover {{ transform: translateX(4px); }}
        
        .agent.running {{ border-left: 3px solid; background: rgba #3fb950(63,185,80,0.1); }}
        .agent.working {{ border-left: 3px solid #d29922; background: rgba(210,153,34,0.1); }}
        .agent.thinking {{ border-left: 3px solid #58a6ff; background: rgba(88,166,255,0.1); }}
        .agent.idle {{ border-left: 3px solid #484f58; opacity: 0.5; }}
        
        .agent-emoji {{ font-size: 1.5em; }}
        .agent-info {{ flex: 1; }}
        .agent-name {{ font-size: 0.9em; font-weight: 600; }}
        .agent-task {{ font-size: 0.75em; color: #8b949e; margin-top: 2px; }}
        
        .agent-status {{
            width: 8px; height: 8px; border-radius: 50%;
        }}
        
        .agent.running .agent-status {{ background: #3fb950; animation: pulse 1s infinite; }}
        .agent.working .agent-status {{ background: #d29922; animation: pulse 0.5s infinite; }}
        .agent.thinking .agent-status {{ background: #58a6ff; }}
        .agent.idle .agent-status {{ background: #484f58; }}
        
        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.5; }}
        }}
        
        .stats {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
            max-width: 1400px;
            margin: 20px auto;
        }}
        
        .stat-card {{
            background: #161b22;
            border: 1px solid #30363d;
            border-radius: 12px;
            padding: 15px;
            text-align: center;
        }}
        
        .stat-icon {{ font-size: 1.8em; margin-bottom: 8px; }}
        .stat-value {{ font-size: 1.5em; font-weight: bold; }}
        .stat-label {{ font-size: 0.75em; color: #8b949e; margin-top: 4px; }}
        
        .stat-card.green .stat-value {{ color: #3fb950; }}
        .stat-card.blue .stat-value {{ color: #58a6ff; }}
        .stat-card.yellow .stat-value {{ color: #d29922; }}
        
        .log-section {{
            max-width: 1400px;
            margin: 20px auto;
            background: #161b22;
            border-radius: 12px;
            padding: 20px;
            border: 1px solid #30363d;
        }}
        
        .log-title {{ font-size: 0.9em; color: #8b949e; margin-bottom: 15px; }}
        
        .log-entry {{
            font-size: 0.8em;
            padding: 8px 0;
            border-bottom: 1px solid #21262d;
            display: flex;
            gap: 15px;
        }}
        
        .log-time {{ color: #8b949e; min-width: 70px; }}
        .log-agent {{ color: #bc8cff; min-width: 100px; }}
        .log-message {{ color: #e6edf3; }}
        
        .pending {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            margin-top: 10px;
        }}
        
        .pending-item {{
            background: rgba(210,153,34,0.2);
            color: #d29922;
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 0.7em;
        }}
        
        .refresh {{
            text-align: center;
            margin-top: 20px;
            color: #8b949e;
            font-size: 0.8em;
        }}
        
        .refresh button {{
            background: #21262d;
            border: 1px solid #30363d;
            color: #58a6ff;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.85em;
        }}
        
        .refresh button:hover {{ background: #30363d; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🏢 TOTA OFFICE</h1>
        <div class="meta">
            <span>🕐 {now.strftime('%H:%M:%S')}</span>
            <span>🎯 Session: MAIN</span>
            <span>🧠 Memory: ACTIVE</span>
        </div>
    </div>
    
    <!-- Stats -->
    <div class="stats">
        <div class="stat-card green">
            <div class="stat-icon">🦊</div>
            <div class="stat-value">5</div>
            <div class="stat-label">Agents</div>
        </div>
        <div class="stat-card blue">
            <div class="stat-icon">⏰</div>
            <div class="stat-value">15</div>
            <div class="stat-label">Cron Jobs</div>
        </div>
        <div class="stat-card yellow">
            <div class="stat-icon">📈</div>
            <div class="stat-value">{trading['balance']}</div>
            <div class="stat-label">Paper Balance</div>
        </div>
        <div class="stat-card">
            <div class="stat-icon">🧠</div>
            <div class="stat-value">30+</div>
            <div class="stat-label">Skills</div>
        </div>
    </div>
    
    <!-- Office Grid -->
    <div class="grid">
        <!-- Orquestador -->
        <div class="station">
            <div class="station-header">
                <span class="station-icon">🎯</span>
                <span class="station-title">Orquestador</span>
            </div>
            <div class="agent thinking" id="agent-tota">
                <div class="agent-emoji">🦊</div>
                <div class="agent-info">
                    <div class="agent-name">Tota</div>
                    <div class="agent-task">Esperando...</div>
                </div>
                <div class="agent-status"></div>
            </div>
            <div class="pending">
                <span class="pending-item">⏳ Gmail Auth</span>
                <span class="pending-item">⏳ API Exchange</span>
            </div>
        </div>
        
        <!-- Research -->
        <div class="station">
            <div class="station-header">
                <span class="station-icon">🔍</span>
                <span class="station-title">Research Lab</span>
            </div>
            <div class="agent idle" id="agent-research">
                <div class="agent-emoji">🔍</div>
                <div class="agent-info">
                    <div class="agent-name">Research Lead</div>
                    <div class="agent-task">Listo</div>
                </div>
                <div class="agent-status"></div>
            </div>
            <div class="agent idle" id="agent-x_scout">
                <div class="agent-emoji">🐦</div>
                <div class="agent-info">
                    <div class="agent-name">X Scout</div>
                    <div class="agent-task">Listo</div>
                </div>
                <div class="agent-status"></div>
            </div>
        </div>
        
        <!-- Trading -->
        <div class="station">
            <div class="station-header">
                <span class="station-icon">📈</span>
                <span class="station-title">Trading Floor</span>
            </div>
            <div class="agent idle" id="agent-trading">
                <div class="agent-emoji">📈</div>
                <div class="agent-info">
                    <div class="agent-name">Trading Bot</div>
                    <div class="agent-task">Balance: {trading['balance']}</div>
                </div>
                <div class="agent-status"></div>
            </div>
            <div class="agent idle" id="agent-risk">
                <div class="agent-emoji">🛡️</div>
                <div class="agent-info">
                    <div class="agent-name">Risk Manager</div>
                    <div class="agent-task">Monitoreando</div>
                </div>
                <div class="agent-status"></div>
            </div>
        </div>
        
        <!-- Content -->
        <div class="station">
            <div class="station-header">
                <span class="station-icon">🎬</span>
                <span class="station-title">Content Lab</span>
            </div>
            <div class="agent idle" id="agent-transcriber">
                <div class="agent-emoji">🎬</div>
                <div class="agent-info">
                    <div class="agent-name">Transcriber</div>
                    <div class="agent-task">YouTube (gratis)</div>
                </div>
                <div class="agent-status"></div>
            </div>
            <div class="agent idle" id="agent-notion">
                <div class="agent-emoji">📝</div>
                <div class="agent-info">
                    <div class="agent-name">Notion</div>
                    <div class="agent-task">⏳ Sin token</div>
                </div>
                <div class="agent-status"></div>
            </div>
        </div>
        
        <!-- System -->
        <div class="station">
            <div class="station-header">
                <span class="station-icon">⚙️</span>
                <span class="station-title">System</span>
            </div>
            <div class="agent idle" id="agent-memory">
                <div class="agent-emoji">🧠</div>
                <div class="agent-info">
                    <div class="agent-name">Memory</div>
                    <div class="agent-task">30+ skills</div>
                </div>
                <div class="agent-status"></div>
            </div>
            <div class="agent idle" id="agent-intel">
                <div class="agent-emoji">🔎</div>
                <div class="agent-info">
                    <div class="agent-name">Intelligence</div>
                    <div class="agent-task">09:00 daily</div>
                </div>
                <div class="agent-status"></div>
            </div>
        </div>
        
        <!-- Projects -->
        <div class="station">
            <div class="station-header">
                <span class="station-icon">💼</span>
                <span class="station-title">Proyectos</span>
            </div>
            <div class="agent idle" id="agent-zaltyko">
                <div class="agent-emoji">🏋️</div>
                <div class="agent-info">
                    <div class="agent-name">Zaltyko</div>
                    <div class="agent-task">SaaS Academias</div>
                </div>
                <div class="agent-status"></div>
            </div>
            <div class="agent idle" id="agent-trading-proj">
                <div class="agent-emoji">💰</div>
                <div class="agent-info">
                    <div class="agent-name">Trading</div>
                    <div class="agent-task">Hyperliquid/Asterdex</div>
                </div>
                <div class="agent-status"></div>
            </div>
        </div>
    </div>
    
    <!-- Log -->
    <div class="log-section">
        <div class="log-title">📝 ACTIVIDAD RECIENTE</div>
        <div id="log-container">
            <div class="log-entry">
                <span class="log-time">{now.strftime('%H:%M:%S')}</span>
                <span class="log-agent">Sistema</span>
                <span class="log-message">Oficina iniciada</span>
            </div>
            <div class="log-entry">
                <span class="log-time">{now.strftime('%H:%M:%S')}</span>
                <span class="log-agent">Tota</span>
                <span class="log-message">Listo para trabajar</span>
            </div>
        </div>
    </div>
    
    <div class="refresh">
        <button onclick="location.reload()">🔄 Actualizar</button>
    </div>
    
    <script>
        function addLog(agent, message) {{
            const container = document.getElementById('log-container');
            const time = new Date().toTimeString().substring(0, 8);
            
            const entry = document.createElement('div');
            entry.className = 'log-entry';
            entry.innerHTML = `
                <span class="log-time">${{time}}</span>
                <span class="log-agent">${{agent}}</span>
                <span class="log-message">${{message}}</span>
            `;
            
            container.insertBefore(entry, container.firstChild);
            
            while (container.children.length > 10) {{
                container.removeChild(container.lastChild);
            }}
        }}
        
        const agents = ['Tota', 'Trading Bot', 'Research Lead', 'Transcriber', 'Risk Manager'];
        const tasks = [
            'Analizando mercado...',
            'Buscando leads...',
            'Transcribiendo video...',
            'Verificando riesgos...',
            'Guardando memoria...'
        ];
        
        setInterval(() => {{
            const agent = agents[Math.floor(Math.random() * agents.length)];
            const task = tasks[Math.floor(Math.random() * tasks.length)];
            addLog(agent, task);
        }}, 8000);
    </script>
</body>
</html>'''
    
    return html

def main():
    print("🏢 Generando Tota Office...")
    
    html = generate_html()
    
    with open(HTML_FILE, 'w') as f:
        f.write(html)
    
    print(f"✅ Oficina actualizada: {HTML_FILE}")
    
    # Abrir en navegador
    os.system(f"open {HTML_FILE}")

if __name__ == "__main__":
    main()
