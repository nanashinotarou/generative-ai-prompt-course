import os
import re

files = [
    "vol01-1_ai_start.html",
    "vol02-1_canva_basics.html",
    "vol01-3_prompt.html",
    "vol04-1_nano_banana.html",
    "vol05-1_text_to_video.html"
]

# Standard JS Logic to Inject/Update
standard_logic = r'''
        // --- Standardized Checklist & Progress Logic ---
        function toggleTask(taskId, element, groupId) {
            const done = element.classList.toggle('completed');
            state[taskId] = done;
            let dayNum = "1";
            if (document.title.includes("Day")) {
                let match = document.title.match(/Day\s*(\d+)/i);
                if (match) dayNum = match[1];
            }
            const dayKey = 'day' + dayNum + '_premium_prog';
            localStorage.setItem(dayKey, JSON.stringify(state));
            
            updateProgress();
            checkGroups(groupId);
        }

        function checkGroups(triggerGroupId = null) {
            for(let groupId in missionGroups) {
                const groupTasks = missionGroups[groupId];
                const allDone = groupTasks.every(t => state[t]);
                const groupArea = document.getElementById('mission-group-' + groupId);
                
                if (groupArea) {
                    if (allDone && !groupArea.classList.contains('completed')) {
                        groupArea.classList.add('completed');
                        if(groupId == triggerGroupId) {
                            playStampSound();
                            if(groupId == 2) fireConfetti(); 
                        }
                    } else if (!allDone) {
                        groupArea.classList.remove('completed');
                    }
                }
            }
        }

        function updateProgress() {
            const count = allTasks.filter(t => state[t]).length;
            const total = allTasks.length;
            const pct = total > 0 ? Math.round((count / total) * 100) : 0;
            const bar = document.getElementById('progress-bar');
            const txt = document.getElementById('progress-percent');
            if (bar) bar.style.width = pct + '%';
            if (txt) txt.innerText = pct + '%';
        }

        function playStampSound() {
            try {
                const AudioContext = window.AudioContext || window.webkitAudioContext;
                if (!AudioContext) return;
                const audioCtx = new AudioContext();
                const oscillator = audioCtx.createOscillator();
                const gainNode = audioCtx.createGain();
                oscillator.type = 'sine';
                oscillator.frequency.setValueAtTime(150, audioCtx.currentTime);
                oscillator.frequency.exponentialRampToValueAtTime(40, audioCtx.currentTime + 0.1);
                gainNode.gain.setValueAtTime(0.5, audioCtx.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.1);
                oscillator.connect(gainNode);
                gainNode.connect(audioCtx.destination);
                oscillator.start();
                oscillator.stop(audioCtx.currentTime + 0.1);
            } catch(e) { console.error("Audio error", e); }
        }

        function fireConfetti() {
            const c = document.getElementById('confetti');
            if (!c) return;
            const ctx = c.getContext('2d');
            c.width = window.innerWidth; c.height = window.innerHeight;
            const pieces = [], colors = ['#38bdf8', '#34d399', '#fbbf24', '#f87171', '#a78bfa', '#2dd4bf'];
            for (let i = 0; i < 150; i++) {
                pieces.push({
                    x: Math.random() * c.width, y: Math.random() * c.height - c.height,
                    w: Math.random() * 8 + 6, h: Math.random() * 8 + 6,
                    vx: Math.random() * 6 - 3, vy: Math.random() * 5 + 3,
                    color: colors[Math.floor(Math.random() * colors.length)],
                    rot: Math.random() * 360, rs: Math.random() * 10 - 5
                });
            }
            let aid;
            function upd() {
                ctx.clearRect(0, 0, c.width, c.height);
                let active = false;
                pieces.forEach(p => {
                    p.y += p.vy; p.x += p.vx; p.rot += p.rs;
                    if (p.y < c.height) active = true;
                    ctx.save(); ctx.translate(p.x, p.y);
                    ctx.rotate(p.rot * Math.PI / 180);
                    ctx.fillStyle = p.color;
                    ctx.fillRect(-p.w / 2, -p.h / 2, p.w, p.h);
                    ctx.restore();
                });
                if (active) aid = requestAnimationFrame(upd);
                else ctx.clearRect(0, 0, c.width, c.height);
            }
            upd();
            setTimeout(() => { cancelAnimationFrame(aid); ctx.clearRect(0, 0, c.width, c.height); }, 6000);
        }
'''

def fix_file(filename):
    if not os.path.exists(filename):
        return
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Ensure canvas is present
    if '<canvas id="confetti"></canvas>' not in content:
        content = content.replace("<body>", '<body>\n    <canvas id="confetti"></canvas>')

    # Remove existing function definitions if they are old/redundant
    for fn in ["toggleTask", "checkGroups", "updateProgress", "playStampSound", "fireConfetti"]:
        pattern = r"function " + fn + r"\(.*?\)\s*\{.*?\}\n?"
        content = re.sub(pattern, "", content, flags=re.DOTALL)

    # Inject standardized logic before </script>
    marker = "// --- Standardized Checklist & Progress Logic ---"
    if marker not in content:
        # Use a function to avoid backslash escape issues
        content = content.replace("</script>", standard_logic + "\n    </script>")
    else:
        # Replace existing standardized block
        content = re.sub(marker + r".*?function fireConfetti\(\) \{.*?\}", lambda m: standard_logic.strip(), content, flags=re.DOTALL)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed {filename}")

for f in files:
    fix_file(f)
