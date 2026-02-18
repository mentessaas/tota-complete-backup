#!/bin/bash
# Tota Complete Restore Script
# To use on a new Mac:

# 1. Install OpenClaw
# npm install -g openclaw

# 2. Clone this backup
# git clone https://github.com/mentessaas/tota-workspace-backup.git ~/.openclaw/workspace

# 3. Copy identity files
cp SOUL.md ~/.openclaw/workspace/
cp USER.md ~/.openclaw/workspace/
cp IDENTITY.md ~/.openclaw/workspace/
cp TOOLS.md ~/.openclaw/workspace/
cp AGENTS.md ~/.openclaw/workspace/
cp HEARTBEAT.md ~/.openclaw/workspace/
cp MEMORY.md ~/.openclaw/workspace/

# 4. Copy memory
cp -r memory ~/.openclaw/workspace/

# 5. Copy zaltyko-os
mkdir -p ~/.openclaw/workspace/zaltyko-os
cp -r zaltyko-os/* ~/.openclaw/workspace/zaltyko-os/

# 6. Start OpenClaw
# openclaw start

echo "✅ Restore complete!"
