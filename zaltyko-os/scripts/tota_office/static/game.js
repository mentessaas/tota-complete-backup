// Tota Office - Game Engine
// Motor de juego con animaciones y renderizado estilo Pokémon moderno

class TotaOfficeGame {
    constructor(canvas) {
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
        
        // Configuración
        this.width = 800;
        this.height = 600;
        this.tileSize = 16;
        this.scale = 3;
        
        // Estado del juego
        this.agents = {};
        this.areas = {};
        this.messages = [];
        this.tasks = {};
        
        // Animación
        this.lastTime = 0;
        this.animFrame = 0;
        
        // Interacción
        this.selectedAgent = null;
        this.hoveredAgent = null;
        this.isDragging = false;
        this.dragTarget = null;
        
        // Partículas
        this.particles = [];
        
        // Inicializar
        this.init();
    }
    
    init() {
        this.canvas.width = this.width;
        this.canvas.height = this.height;
        
        // Event listeners
        this.setupEvents();
        
        // Iniciar loop
        this.gameLoop(0);
    }
    
    setupEvents() {
        // Click en canvas
        this.canvas.addEventListener('click', (e) => this.handleClick(e));
        
        // Mouse move para hover
        this.canvas.addEventListener('mousemove', (e) => this.handleMouseMove(e));
        
        // Doble click para mover
        this.canvas.addEventListener('dblclick', (e) => this.handleDoubleClick(e));
        
        // Context menu (right click) para mover
        this.canvas.addEventListener('contextmenu', (e) => {
            e.preventDefault();
            this.handleRightClick(e);
        });
    }
    
    getMousePos(e) {
        const rect = this.canvas.getBoundingClientRect();
        return {
            x: e.clientX - rect.left,
            y: e.clientY - rect.top
        };
    }
    
    handleClick(e) {
        const pos = this.getMousePos(e);
        
        // Verificar si clicó en un agente
        const clickedAgent = this.getAgentAtPosition(pos.x, pos.y);
        
        if (clickedAgent) {
            // Mostrar detalles del agente
            if (window.showAgentModal) {
                window.showAgentModal(clickedAgent);
            }
            
            // Efecto de partículas
            this.spawnParticles(clickedAgent.x, clickedAgent.y, 'happy');
        }
    }
    
    handleDoubleClick(e) {
        const pos = this.getMousePos(e);
        
        // Verificar si hizo doble click en un agente
        const clickedAgent = this.getAgentAtPosition(pos.x, pos.y);
        
        if (clickedAgent) {
            // Mover agente al cursor
            this.moveAgentTo(clickedAgent.id, pos.x, pos.y);
        }
    }
    
    handleRightClick(e) {
        const pos = this.getMousePos(e);
        
        // Mover agente seleccionado o cualquier agente al cursor
        const clickedAgent = this.getAgentAtPosition(pos.x, pos.y);
        
        if (clickedAgent) {
            this.moveAgentTo(clickedAgent.id, pos.x, pos.y);
        } else {
            // Si no hay agente, mover al agente seleccionado
            if (this.selectedAgent) {
                this.moveAgentTo(this.selectedAgent.id, pos.x, pos.y);
            }
        }
    }
    
    handleMouseMove(e) {
        const pos = this.getMousePos(e);
        
        // Verificar hover
        this.hoveredAgent = this.getAgentAtPosition(pos.x, pos.y);
        
        // Cambiar cursor
        this.canvas.style.cursor = this.hoveredAgent ? 'pointer' : 'default';
    }
    
    getAgentAtPosition(x, y) {
        for (const agent of Object.values(this.agents)) {
            const dist = Math.sqrt((x - agent.x) ** 2 + (y - agent.y) ** 2);
            if (dist < 30) {
                return agent;
            }
        }
        return null;
    }
    
    moveAgentTo(agentId, x, y) {
        if (!this.ws || this.ws.readyState !== WebSocket.OPEN) return;
        
        this.ws.send(JSON.stringify({
            type: 'move',
            data: {
                agent_id: agentId,
                x: Math.max(30, Math.min(this.width - 30, x)),
                y: Math.max(50, Math.min(this.height - 50, y))
            }
        }));
        
        // Efecto visual
        this.spawnParticles(x, y, 'work');
    }
    
    // Actualizar estado desde WebSocket
    updateState(data) {
        this.agents = data.agents || {};
        this.areas = data.areas || {};
        this.messages = data.messages || [];
        this.tasks = data.tasks || {};
    }
    
    // Renderizado principal
    render() {
        this.animFrame++;
        
        // Limpiar canvas
        this.ctx.fillStyle = '#1a1a2e';
        this.ctx.fillRect(0, 0, this.width, this.height);
        
        // Dibujar suelo
        this.drawFloor();
        
        // Dibujar áreas
        this.drawAreas();
        
        // Dibujar escritorios
        this.drawDesks();
        
        // Dibujar props decorativos
        this.drawDecorations();
        
        // Dibujar agentes
        this.drawAgents();
        
        // Dibujar partículas
        this.drawParticles();
        
        // Dibujar UI overlays
        this.drawOverlays();
    }
    
    drawFloor() {
        // Patrón de suelo base
        const floorColors = ['#3d5c5c', '#456666', '#4a7070'];
        
        for (let x = 0; x < this.width; x += this.tileSize) {
            for (let y = 0; y < this.height; y += this.tileSize) {
                // Variación según posición
                const variation = (Math.sin(x * 0.1) * Math.cos(y * 0.1)) > 0 ? 0 : 1;
                this.ctx.fillStyle = floorColors[variation];
                this.ctx.fillRect(x, y, this.tileSize, this.tileSize);
                
                // Borde de tile
                this.ctx.strokeStyle = 'rgba(0, 0, 0, 0.15)';
                this.ctx.lineWidth = 1;
                this.ctx.strokeRect(x, y, this.tileSize, this.tileSize);
            }
        }
        
        // Alfombra central
        this.ctx.save();
        this.ctx.fillStyle = 'rgba(108, 92, 231, 0.1)';
        this.ctx.beginPath();
        this.ctx.ellipse(400, 350, 200, 120, 0, 0, Math.PI * 2);
        this.ctx.fill();
        this.ctx.restore();
    }
    
    drawAreas() {
        // Sala de reuniones
        if (this.areas.meeting) {
            const meeting = this.areas.meeting;
            
            // Área
            this.ctx.fillStyle = 'rgba(108, 92, 231, 0.15)';
            this.ctx.fillRect(320, 40, 160, 100);
            
            // Borde
            this.ctx.strokeStyle = '#6c5ce7';
            this.ctx.lineWidth = 3;
            this.ctx.setLineDash([5, 5]);
            this.ctx.strokeRect(320, 40, 160, 100);
            this.ctx.setLineDash([]);
            
            // Pizarra
            this.ctx.fillStyle = '#dfe6e9';
            this.ctx.fillRect(355, 50, 90, 40);
            this.ctx.strokeStyle = '#636e72';
            this.ctx.lineWidth = 2;
            this.ctx.strokeRect(355, 50, 90, 40);
            
            // Mesa
            this.ctx.fillStyle = '#8b5a2b';
            this.ctx.fillRect(340, 85, 120, 30);
            this.ctx.strokeStyle = '#5d3a1a';
            this.ctx.strokeRect(340, 85, 120, 30);
            
            // Texto
            this.ctx.font = 'bold 12px "Press Start 2P", monospace';
            this.ctx.fillStyle = '#fff';
            this.ctx.textAlign = 'center';
            this.ctx.fillText('🤝 REUNIÓN', 400, 35);
        }
        
        // Cocina
        if (this.areas.kitchen) {
            const kitchen = this.areas.kitchen;
            
            this.ctx.fillStyle = 'rgba(39, 174, 96, 0.15)';
            this.ctx.fillRect(650, 400, 120, 80);
            
            this.ctx.strokeStyle = '#27ae60';
            this.ctx.lineWidth = 3;
            this.ctx.setLineDash([5, 5]);
            this.ctx.strokeRect(650, 400, 120, 80);
            this.ctx.setLineDash([]);
            
            // Mostrador
            this.ctx.fillStyle = '#dfe6e9';
            this.ctx.fillRect(655, 430, 110, 45);
            
            // Items
            this.ctx.font = '16px Arial';
            this.ctx.fillText('☕', 680, 460);
            this.ctx.fillText('🧊', 710, 460);
            this.ctx.fillText('🍵', 740, 460);
            
            this.ctx.font = 'bold 10px "Press Start 2P", monospace';
            this.ctx.fillStyle = '#fff';
            this.ctx.fillText('☕ COCINA', 710, 395);
        }
        
        // Entrada
        if (this.areas.entrance) {
            const entrance = this.areas.entrance;
            
            this.ctx.fillStyle = 'rgba(52, 152, 219, 0.15)';
            this.ctx.fillRect(20, 500, 60, 60);
            
            this.ctx.strokeStyle = '#3498db';
            this.ctx.lineWidth = 3;
            this.ctx.strokeRect(20, 500, 60, 60);
            
            this.ctx.font = '20px Arial';
            this.ctx.fillText('🚪', 50, 535);
        }
    }
    
    drawDesks() {
        const deskPositions = [
            { x: 80, y: 280, role: 'Orquestador', label: 'TOTA' },
            { x: 230, y: 280, role: 'Research', label: 'RESEARCH' },
            { x: 380, y: 280, role: 'Trading', label: 'TRADING' },
            { x: 530, y: 280, role: 'Content', label: 'CONTENT' },
            { x: 680, y: 280, role: 'Risk', label: 'RISK' }
        ];
        
        deskPositions.forEach(desk => {
            // Usar sprite cacheado
            const sprite = SpriteCache.getDeskSprite(desk.role);
            this.ctx.drawImage(sprite, desk.x - 40, desk.y - 30);
            
            // Silla
            const chairColor = '#e74c3c';
            this.ctx.fillStyle = chairColor;
            this.ctx.beginPath();
            this.ctx.ellipse(desk.x, desk.y + 35, 15, 8, 0, 0, Math.PI * 2);
            this.ctx.fill();
            this.ctx.strokeStyle = '#c0392b';
            this.ctx.lineWidth = 2;
            this.ctx.stroke();
            
            // Etiqueta
            this.ctx.font = '10px "Press Start 2P", monospace';
            this.ctx.fillStyle = 'rgba(255, 255, 255, 0.5)';
            this.ctx.textAlign = 'center';
            this.ctx.fillText(desk.label, desk.x, desk.y + 55);
        });
    }
    
    drawDecorations() {
        // Plantas en las esquinas
        const plantPositions = [
            { x: 30, y: 150 },
            { x: 750, y: 150 },
            { x: 30, y: 520 },
            { x: 750, y: 520 }
        ];
        
        plantPositions.forEach(pos => {
            const plant = SpriteCache.getPlant();
            this.ctx.drawImage(plant, pos.x, pos.y);
        });
        
        // Cuadros en la pared
        const paintings = [
            { x: 150, y: 50, color: '#e17055', icon: '⭐' },
            { x: 400, y: 30, color: '#6c5ce7', icon: '🎮' },
            { x: 650, y: 50, color: '#00b894', icon: '💎' }
        ];
        
        paintings.forEach(p => {
            // Marco
            this.ctx.fillStyle = '#5d3a1a';
            this.ctx.fillRect(p.x - 25, p.y - 20, 50, 40);
            
            // Lienzo
            this.ctx.fillStyle = p.color;
            this.ctx.fillRect(p.x - 20, p.y - 15, 40, 30);
            
            // Icono
            this.ctx.font = '16px Arial';
            this.ctx.textAlign = 'center';
            this.ctx.fillText(p.icon, p.x, p.y + 5);
        });
    }
    
    drawAgents() {
        Object.values(this.agents).forEach(agent => {
            const sprite = SpriteCache.getAgentSprite(agent, agent.status);
            
            // Efecto hover
            if (this.hoveredAgent && this.hoveredAgent.id === agent.id) {
                this.ctx.save();
                this.ctx.shadowColor = '#fdcb6e';
                this.ctx.shadowBlur = 20;
            }
            
            // Efecto seleccionado
            if (this.selectedAgent && this.selectedAgent.id === agent.id) {
                this.ctx.save();
                this.ctx.shadowColor = '#74b9ff';
                this.ctx.shadowBlur = 15;
            }
            
            // Dibujar sprite
            this.ctx.drawImage(
                sprite,
                agent.x - sprite.width / 2,
                agent.y - sprite.height / 2
            );
            
            // Nombre
            this.ctx.font = 'bold 10px "Press Start 2P", monospace';
            this.ctx.fillStyle = '#fff';
            this.ctx.textAlign = 'center';
            this.ctx.fillText(agent.name, agent.x, agent.y + 35);
            
            // Restore context
            if (this.hoveredAgent?.id === agent.id || this.selectedAgent?.id === agent.id) {
                this.ctx.restore();
            }
            
            // Barra de energía pequeña
            if (agent.energy !== undefined) {
                const energyWidth = 30;
                const energyHeight = 4;
                const energyX = agent.x - energyWidth / 2;
                const energyY = agent.y + 42;
                
                // Fondo
                this.ctx.fillStyle = 'rgba(0, 0, 0, 0.5)';
                this.ctx.fillRect(energyX, energyY, energyWidth, energyHeight);
                
                // Energía
                const energyColor = agent.energy > 50 ? '#2ecc71' : agent.energy > 25 ? '#f39c12' : '#e74c3c';
                this.ctx.fillStyle = energyColor;
                this.ctx.fillRect(energyX, energyY, energyWidth * (agent.energy / 100), energyHeight);
            }
        });
    }
    
    drawParticles() {
        this.particles = this.particles.filter(p => p.life > 0);
        
        this.particles.forEach(p => {
            this.ctx.globalAlpha = p.life;
            this.ctx.drawImage(
                p.canvas,
                p.x - 4,
                p.y - 4
            );
            this.ctx.globalAlpha = 1;
            
            p.x += p.vx;
            p.y += p.vy;
            p.vy += 0.1; // gravedad
            p.life -= 0.02;
        });
    }
    
    spawnParticles(x, y, type) {
        const newParticles = SpriteGenerator.createParticleEffect(type);
        newParticles.forEach(p => {
            p.x = x;
            p.y = y;
        });
        this.particles.push(...newParticles);
    }
    
    drawOverlays() {
        // Indicador de controls
        this.ctx.fillStyle = 'rgba(0, 0, 0, 0.6)';
        this.ctx.fillRect(10, this.height - 45, 280, 35);
        
        this.ctx.font = '10px "VT323", monospace';
        this.ctx.fillStyle = '#bdc3c7';
        this.ctx.textAlign = 'left';
        this.ctx.fillText('🎮 Click: detalles | DblClick: mover | RightClick: mover aquí', 20, this.height - 22);
    }
    
    gameLoop(timestamp) {
        const deltaTime = timestamp - this.lastTime;
        this.lastTime = timestamp;
        
        this.render();
        
        requestAnimationFrame((t) => this.gameLoop(t));
    }
    
    // Conectar WebSocket
    connect(ws) {
        this.ws = ws;
    }
}

// Inicializar cuando el DOM esté listo
let game = null;

function initGame() {
    const canvas = document.getElementById('officeCanvas');
    if (canvas) {
        game = new TotaOfficeGame(canvas);
    }
}

// Exponer funciones globales
window.initGame = initGame;
window.getGame = () => game;
