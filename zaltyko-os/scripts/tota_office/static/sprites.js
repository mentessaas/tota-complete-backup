// Tota Office - Sprite Generator
// Generador de sprites procedurales estilo Pokémon moderno

const SpriteGenerator = {
    tileSize: 16,
    scale: 3,
    
    // Paleta de colores por agente
    agentPalettes: {
        tota: {
            body: '#ff9f43',
            bodyDark: '#e67e22',
            bodyLight: '#fdcb6e',
            accent: '#ff6b6b',
            eyes: '#2d3436',
            hair: '#d63031'
        },
        research_lead: {
            body: '#74b9ff',
            bodyDark: '#0984e3',
            bodyLight: '#a29bfe',
            accent: '#6c5ce7',
            eyes: '#2d3436',
            hair: '#2d3436'
        },
        trading_bot: {
            body: '#55efc4',
            bodyDark: '#00b894',
            bodyLight: '#81ecec',
            accent: '#00cec9',
            eyes: '#2d3436',
            hair: '#00b894'
        },
        transcriber: {
            body: '#fd79a8',
            bodyDark: '#e84393',
            bodyLight: '#fab1a0',
            accent: '#fdcb6e',
            eyes: '#2d3436',
            hair: '#e84393'
        },
        risk_manager: {
            body: '#ff7675',
            bodyDark: '#d63031',
            bodyLight: '#fab1a0',
            accent: '#636e72',
            eyes: '#2d3436',
            hair: '#2d3436'
        }
    },
    
    // Generar sprite de agente
    createAgentSprite(agent, state = 'idle') {
        const canvas = document.createElement('canvas');
        const size = this.tileSize * this.scale;
        canvas.width = size;
        canvas.height = size;
        const ctx = canvas.getContext('2d');
        
        const palette = this.agentPalettes[agent.id] || this.agentPalettes.tota;
        
        // Animación según estado
        const frame = this.getAnimationFrame(state);
        const bobY = state === 'idle' ? Math.sin(frame * 0.5) * 2 : 0;
        const walkBob = state === 'walking' ? Math.sin(frame * 2) * 3 : 0;
        
        ctx.save();
        ctx.translate(0, bobY + walkBob);
        
        // Sombra
        this.drawShadow(ctx, size / 2, size - 8, 20);
        
        // Cuerpo estilo chibi
        this.drawChibiBody(ctx, size / 2, size / 2 - 5, palette, state);
        
        // Cabeza
        this.drawChibiHead(ctx, size / 2, size / 2 - 20, palette, agent, state);
        
        // Ojos
        this.drawChibiEyes(ctx, size / 2, size / 2 - 22, palette, state, frame);
        
        // Estado/animo sobre la cabeza
        this.drawStatusIndicator(ctx, size / 2, size / 2 - 45, agent);
        
        ctx.restore();
        
        return canvas;
    },
    
    drawShadow(ctx, x, y, radius) {
        ctx.save();
        ctx.fillStyle = 'rgba(0, 0, 0, 0.2)';
        ctx.beginPath();
        ctx.ellipse(x, y, radius, radius * 0.4, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
    },
    
    drawChibiBody(ctx, x, y, palette, state) {
        // Cuerpo principal redondeado
        const gradient = ctx.createRadialGradient(x - 5, y - 10, 0, x, y, 25);
        gradient.addColorStop(0, palette.bodyLight);
        gradient.addColorStop(1, palette.body);
        
        ctx.fillStyle = gradient;
        ctx.beginPath();
        ctx.ellipse(x, y, 20, 22, 0, 0, Math.PI * 2);
        ctx.fill();
        
        // Borde
        ctx.strokeStyle = palette.bodyDark;
        ctx.lineWidth = 2;
        ctx.stroke();
        
        // Belly/blush
        ctx.fillStyle = palette.bodyLight + '60';
        ctx.beginPath();
        ctx.ellipse(x, y + 8, 12, 8, 0, 0, Math.PI * 2);
        ctx.fill();
        
        // Si está trabajando, dibujar brazos
        if (state === 'working') {
            ctx.fillStyle = palette.body;
            // Brazo izq
            ctx.beginPath();
            ctx.ellipse(x - 18, y + 5, 8, 6, -0.5, 0, Math.PI * 2);
            ctx.fill();
            // Brazo der
            ctx.beginPath();
            ctx.ellipse(x + 18, y + 5, 8, 6, 0.5, 0, Math.PI * 2);
            ctx.fill();
        }
    },
    
    drawChibiHead(ctx, x, y, palette, agent, state) {
        // Cabeza
        const gradient = ctx.createRadialGradient(x - 5, y - 8, 0, x, y, 22);
        gradient.addColorStop(0, palette.bodyLight);
        gradient.addColorStop(1, palette.body);
        
        ctx.fillStyle = gradient;
        ctx.beginPath();
        ctx.arc(x, y, 20, 0, Math.PI * 2);
        ctx.fill();
        
        ctx.strokeStyle = palette.bodyDark;
        ctx.lineWidth = 2;
        ctx.stroke();
        
        // Pelo/característica única
        this.drawHair(ctx, x, y - 18, palette, agent.id);
    },
    
    drawHair(ctx, x, y, palette, agentId) {
        ctx.fillStyle = palette.hair;
        
        switch(agentId) {
            case 'tota':
                // Orejas de zorro
                ctx.beginPath();
                ctx.moveTo(x - 15, y + 5);
                ctx.lineTo(x - 22, y - 15);
                ctx.lineTo(x - 8, y - 5);
                ctx.fill();
                ctx.beginPath();
                ctx.moveTo(x + 15, y + 5);
                ctx.lineTo(x + 22, y - 15);
                ctx.lineTo(x + 8, y - 5);
                ctx.fill();
                // Colita
                ctx.beginPath();
                ctx.moveTo(x + 15, y + 10);
                ctx.quadraticCurveTo(x + 30, y, x + 25, y - 20);
                ctx.quadraticCurveTo(x + 20, y - 25, x + 15, y - 15);
                ctx.fill();
                break;
                
            case 'research_lead':
                // Lentes/pelo hacia arriba
                ctx.fillRect(x - 18, y - 5, 36, 8);
                ctx.beginPath();
                ctx.arc(x, y - 12, 12, Math.PI, 0);
                ctx.fill();
                break;
                
            case 'trading_bot':
                // Antena
                ctx.beginPath();
                ctx.moveTo(x, y - 20);
                ctx.lineTo(x, y - 35);
                ctx.strokeStyle = palette.hair;
                ctx.lineWidth = 3;
                ctx.stroke();
                ctx.beginPath();
                ctx.arc(x, y - 38, 4, 0, Math.PI * 2);
                ctx.fillStyle = '#fdcb6e';
                ctx.fill();
                break;
                
            case 'transcriber':
                // Panuelo
                ctx.beginPath();
                ctx.moveTo(x - 20, y - 5);
                ctx.quadraticCurveTo(x, y - 25, x + 20, y - 5);
                ctx.lineTo(x + 15, y + 5);
                ctx.quadraticCurveTo(x, y - 10, x - 15, y + 5);
                ctx.fill();
                break;
                
            case 'risk_manager':
                // Casco/cuerno
                ctx.beginPath();
                ctx.moveTo(x - 8, y - 15);
                ctx.lineTo(x, y - 35);
                ctx.lineTo(x + 8, y - 15);
                ctx.fill();
                break;
        }
    },
    
    drawChibiEyes(ctx, x, y, palette, state, frame) {
        // Ojos grandes estilo Pokémon
        const eyeY = y;
        const eyeSpacing = 8;
        
        // Parpadeo
        const isBlinking = Math.floor(frame / 60) % 4 === 0;
        
        // Ojo izq
        this.drawEye(ctx, x - eyeSpacing, eyeY, palette, isBlinking);
        // Ojo der
        this.drawEye(ctx, x + eyeSpacing, eyeY, palette, isBlinking);
    },
    
    drawEye(ctx, x, y, palette, isBlinking) {
        if (isBlinking) {
            // Ojo cerrado
            ctx.strokeStyle = palette.eyes;
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(x - 6, y);
            ctx.quadraticCurveTo(x, y - 3, x + 6, y);
            ctx.stroke();
        } else {
            // Blanco del ojo
            ctx.fillStyle = '#fff';
            ctx.beginPath();
            ctx.ellipse(x, y, 7, 8, 0, 0, Math.PI * 2);
            ctx.fill();
            
            // Iris
            const gradient = ctx.createRadialGradient(x + 2, y - 2, 0, x, y, 6);
            gradient.addColorStop(0, '#74b9ff');
            gradient.addColorStop(1, palette.eyes);
            ctx.fillStyle = gradient;
            ctx.beginPath();
            ctx.ellipse(x + 1, y, 5, 6, 0, 0, Math.PI * 2);
            ctx.fill();
            
            // Brillo
            ctx.fillStyle = '#fff';
            ctx.beginPath();
            ctx.arc(x - 2, y - 3, 2, 0, Math.PI * 2);
            ctx.fill();
        }
    },
    
    drawStatusIndicator(ctx, x, y, agent) {
        const status = agent.status;
        
        // Fondo del indicador
        ctx.fillStyle = 'rgba(0, 0, 0, 0.6)';
        ctx.beginPath();
        ctx.arc(x, y, 12, 0, Math.PI * 2);
        ctx.fill();
        
        // Emoji según estado
        ctx.font = '14px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        
        let emoji = '';
        switch(status) {
            case 'working': emoji = '⌨️'; break;
            case 'thinking': emoji = '💭'; break;
            case 'walking': emoji = '🚶'; break;
            case 'meeting': emoji = '🤝'; break;
            case 'idle': emoji = agent.energy > 70 ? '😊' : '😴'; break;
            default: emoji = '😐';
        }
        
        ctx.fillText(emoji, x, y);
    },
    
    getAnimationFrame(state) {
        return Math.floor(performance.now() / 100) % 120;
    },
    
    // Generar sprite de escritorio
    createDeskSprite(role) {
        const canvas = document.createElement('canvas');
        const size = 80;
        canvas.width = size;
        canvas.height = size;
        const ctx = canvas.getContext('2d');
        
        // Base del escritorio
        ctx.fillStyle = '#8b5a2b';
        ctx.fillRect(5, 35, 70, 30);
        
        // Borde
        ctx.strokeStyle = '#5d3a1a';
        ctx.lineWidth = 2;
        ctx.strokeRect(5, 35, 70, 30);
        
        // Monitor
        this.drawMonitor(ctx, 15, 15, role);
        
        // Teclado
        ctx.fillStyle = '#2d3436';
        ctx.fillRect(20, 45, 40, 8);
        
        // Adornos según rol
        this.drawDeskProps(ctx, 60, 50, role);
        
        return canvas;
    },
    
    drawMonitor(ctx, x, y, role) {
        // Base del monitor
        ctx.fillStyle = '#2d3436';
        ctx.fillRect(x + 12, y + 25, 16, 6);
        
        // Pantalla
        const gradient = ctx.createLinearGradient(x, y, x + 40, y + 25);
        gradient.addColorStop(0, '#1a1a2e');
        gradient.addColorStop(1, '#0a0a15');
        ctx.fillStyle = gradient;
        ctx.fillRect(x, y, 40, 25);
        
        // Borde pantalla
        ctx.strokeStyle = '#636e72';
        ctx.lineWidth = 2;
        ctx.strokeRect(x, y, 40, 25);
        
        // Brillo de pantalla (glow)
        ctx.fillStyle = 'rgba(127, 219, 255, 0.1)';
        ctx.fillRect(x + 2, y + 2, 36, 10);
        
        // Icono según rol
        ctx.font = '12px Arial';
        ctx.textAlign = 'center';
        let icon = '💻';
        switch(role) {
            case 'Research': icon = '🔍'; break;
            case 'Trading': icon = '📈'; break;
            case 'Content': icon = '🎬'; break;
            case 'Risk': icon = '🛡️'; break;
            default: icon = '🦊';
        }
        ctx.fillText(icon, x + 20, y + 15);
    },
    
    drawDeskProps(ctx, x, y, role) {
        // Diferentes props según rol
        ctx.font = '14px Arial';
        
        switch(role) {
            case 'Research':
                ctx.fillText('📚', x, y);
                break;
            case 'Trading':
                ctx.fillText('📊', x, y);
                break;
            case 'Content':
                ctx.fillText('🎥', x, y);
                break;
            case 'Risk':
                ctx.fillText('⚠️', x, y);
                break;
            default:
                ctx.fillText('☕', x, y);
        }
    },
    
    // Generar tile de suelo
    createFloorTile(variation = 0) {
        const canvas = document.createElement('canvas');
        canvas.width = this.tileSize;
        canvas.height = this.tileSize;
        const ctx = canvas.getContext('2d');
        
        // Color base
        const colors = ['#3d5c5c', '#4a7070', '#456666'];
        ctx.fillStyle = colors[variation % colors.length];
        ctx.fillRect(0, 0, this.tileSize, this.tileSize);
        
        // Patrón de baldosa
        ctx.strokeStyle = 'rgba(0, 0, 0, 0.1)';
        ctx.lineWidth = 1;
        ctx.strokeRect(0, 0, this.tileSize, this.tileSize);
        
        // Detalle central
        ctx.fillStyle = 'rgba(255, 255, 255, 0.03)';
        ctx.fillRect(4, 4, 8, 8);
        
        return canvas;
    },
    
    // Generar elemento de área
    createAreaSprite(type) {
        const canvas = document.createElement('canvas');
        
        switch(type) {
            case 'meeting':
                canvas.width = 160;
                canvas.height = 100;
                this.drawMeetingRoom(canvas.getContext('2d'));
                break;
            case 'kitchen':
                canvas.width = 120;
                canvas.height = 80;
                this.drawKitchen(canvas.getContext('2d'));
                break;
            case 'entrance':
                canvas.width = 60;
                canvas.height = 60;
                this.drawEntrance(canvas.getContext('2d'));
                break;
            default:
                canvas.width = 16;
                canvas.height = 16;
        }
        
        return canvas;
    },
    
    drawMeetingRoom(ctx) {
        // Pared
        ctx.fillStyle = '#2d4040';
        ctx.fillRect(0, 0, 160, 100);
        
        // Suelo
        ctx.fillStyle = '#4a7070';
        ctx.fillRect(0, 70, 160, 30);
        
        // Mesa
        ctx.fillStyle = '#8b5a2b';
        ctx.fillRect(40, 40, 80, 35);
        ctx.strokeStyle = '#5d3a1a';
        ctx.lineWidth = 2;
        ctx.strokeRect(40, 40, 80, 35);
        
        // Sillas
        ctx.fillStyle = '#e74c3c';
        ctx.beginPath();
        ctx.arc(50, 35, 8, 0, Math.PI * 2);
        ctx.fill();
        ctx.beginPath();
        ctx.arc(110, 35, 8, 0, Math.PI * 2);
        ctx.fill();
        
        // Pizarra
        ctx.fillStyle = '#dfe6e9';
        ctx.fillRect(55, 5, 50, 25);
        ctx.strokeStyle = '#636e72';
        ctx.strokeRect(55, 5, 50, 25);
        
        // Texto
        ctx.font = 'bold 10px Arial';
        ctx.fillStyle = '#2d3436';
        ctx.textAlign = 'center';
        ctx.fillText('REUNIÓN', 80, 20);
        
        // Decoración pared
        ctx.fillStyle = '#6c5ce7';
        ctx.fillRect(10, 10, 30, 20);
    },
    
    drawKitchen(ctx) {
        // Fondo
        ctx.fillStyle = '#27ae60';
        ctx.fillRect(0, 0, 120, 80);
        
        // Mostrador
        ctx.fillStyle = '#dfe6e9';
        ctx.fillRect(5, 30, 110, 45);
        ctx.strokeStyle = '#b2bec3';
        ctx.lineWidth = 2;
        ctx.strokeRect(5, 30, 110, 45);
        
        // Electrodomésticos
        ctx.font = '20px Arial';
        ctx.fillText('☕', 20, 55);
        ctx.fillText('🧊', 50, 55);
        ctx.fillText('🍵', 80, 55);
        
        // Letrero
        ctx.font = 'bold 12px Arial';
        ctx.fillStyle = '#fff';
        ctx.textAlign = 'center';
        ctx.fillText('COCINA', 60, 18);
    },
    
    drawEntrance(ctx) {
        // Marco
        ctx.fillStyle = '#8b4513';
        ctx.fillRect(5, 5, 50, 50);
        
        // Puerta
        ctx.fillStyle = '#dfe6e9';
        ctx.fillRect(10, 10, 40, 45);
        
        // Ventana
        ctx.fillStyle = '#74b9ff';
        ctx.fillRect(15, 15, 15, 15);
        ctx.fillRect(35, 15, 15, 15);
        
        // Letrero
        ctx.font = '12px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('🚪', 30, 40);
    },
    
    // Generar planta decorativa
    createPlant() {
        const canvas = document.createElement('canvas');
        canvas.width = 32;
        canvas.height = 40;
        const ctx = canvas.getContext('2d');
        
        // Maceta
        ctx.fillStyle = '#e17055';
        ctx.fillRect(8, 25, 16, 12);
        ctx.strokeStyle = '#d63031';
        ctx.lineWidth = 1;
        ctx.strokeRect(8, 25, 16, 12);
        
        // Hojas
        ctx.fillStyle = '#00b894';
        ctx.beginPath();
        ctx.ellipse(16, 15, 6, 12, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.beginPath();
        ctx.ellipse(10, 18, 5, 10, -0.5, 0, Math.PI * 2);
        ctx.fill();
        ctx.beginPath();
        ctx.ellipse(22, 18, 5, 10, 0.5, 0, Math.PI * 2);
        ctx.fill();
        
        return canvas;
    },
    
    // Generar efecto de partículas
    createParticleEffect(type) {
        const particles = [];
        const colors = {
            happy: ['#fdcb6e', '#ffeaa7', '#fab1a0'],
            work: ['#74b9ff', '#0984e3', '#fff'],
            alert: ['#ff7675', '#d63031', '#fff']
        };
        
        for (let i = 0; i < 8; i++) {
            const canvas = document.createElement('canvas');
            canvas.width = 8;
            canvas.height = 8;
            const ctx = canvas.getContext('2d');
            
            ctx.fillStyle = colors[type][Math.floor(Math.random() * 3)];
            ctx.beginPath();
            ctx.arc(4, 4, 2 + Math.random() * 2, 0, Math.PI * 2);
            ctx.fill();
            
            particles.push({
                canvas,
                vx: (Math.random() - 0.5) * 2,
                vy: -Math.random() * 2 - 1,
                life: 1
            });
        }
        
        return particles;
    }
};

// Cache de sprites generados
const SpriteCache = {
    agents: {},
    desks: {},
    floor: null,
    areas: {},
    
    getAgentSprite(agent, state) {
        const key = `${agent.id}_${state}`;
        if (!this.agents[key]) {
            this.agents[key] = SpriteGenerator.createAgentSprite(agent, state);
        }
        return this.agents[key];
    },
    
    getDeskSprite(role) {
        if (!this.desks[role]) {
            this.desks[role] = SpriteGenerator.createDeskSprite(role);
        }
        return this.desks[role];
    },
    
    getFloorTile() {
        if (!this.floor) {
            this.floor = SpriteGenerator.createFloorTile(Math.floor(Math.random() * 3));
        }
        return this.floor;
    },
    
    getAreaSprite(type) {
        if (!this.areas[type]) {
            this.areas[type] = SpriteGenerator.createAreaSprite(type);
        }
        return this.areas[type];
    },
    
    getPlant() {
        if (!this.plant) {
            this.plant = SpriteGenerator.createPlant();
        }
        return this.plant;
    }
};
