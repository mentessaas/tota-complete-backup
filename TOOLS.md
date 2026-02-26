# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leakage your infrastructure.

---

### Trading

**KuCoin:** ✅ API运作正常
- API Key: `878483cd310dafb51a9817e8da1dd4e37de15638661d2b1ff0f18d78d360359a`
- Secret: `909acf6898599f35d0c2d6b35e1a8026ca3a26ebfa776afcdce69d1089969401`
- Balance Futures: $222.00 USDT
**Hyperliquid:** ✅ Testnet funcionando
- Script: `~/zaltyko-os/scripts/hyperliquid_bot.py`
- Docs: `https://hyperliquid.gitbook.io`
- Símbolos: BTC/USDC:USDC, ETH/USDC:USDC, SOL/USDC:USDC

---

### Scrapling (Web Scraping)

- **Script:** `~/zaltyko-os/scripts/scrapling_tool.py`
- **venv:** `~/.openclaw/workspace/.venv/`
- **Activar:** `source ~/.openclaw/workspace/.venv/bin/activate`

**Uso:**
```bash
# Script básico
python3 ~/zaltyko-os/scripts/scrapling_tool.py "https://ejemplo.com" "h1"

# En Python:
from scrapling import Fetcher
f = Fetcher()
resp = f.get('https://ejemplo.com', verify=False)
print(resp.css('title').first.text)
```

**Nota:** Requiere `verify=False` por SSL del sistema.

---

### Mis Capacidades ( Nivel 2.5)

| Categoría | Herramienta | Estado |
|-----------|-------------|--------|
| **Búsqueda** | web_search, web_fetch, scraping | ✅ |
| **Browser** | camofox (stealth), browser | ✅ |
| **Email** | himalaya, gog | ⚠️ Sin auth |
| **Trading** | KuCoin API | ❌ API rota |
| **CRM** | Brevo, Supabase | ⚠️ Sin config |
| **Mensajería** | Telegram, Signal, iMessage | ✅ |
| **Archivos** | read, write, edit, exec | ✅ |
| **TTS** | mac-tts, voicebox | ✅ |
| **Scheduling** | cron | ✅ |

---

### Pending (Lo que necesito de Elvis)

1. **Gmail:** `gog auth add elvisvaldes544@gmail.com`
2. **Nueva API Exchange:** Pendiente que me la envíe
3. **Brevo:** API key en secrets
