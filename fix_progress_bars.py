import re
import os

files = [
    "vol01-1_ai_start.html",
    "vol02-1_canva_basics.html",
    "vol01-3_prompt.html",
    "vol04-1_nano_banana.html",
    "vol05-1_text_to_video.html"
]

# Standard JS Logic to Inject/Update
standard_js = """
        // --- Standardized Checklist & Progress Logic ---
        function toggleTask(taskId, element, groupId) {
            const done = element.classList.toggle('completed');
            state[taskId] = done;
            // Get day number from filename or current state
            const dayMatch = window.location.pathname.match(/vol(\\d+)/);
            const dayKey = dayMatch ? 'day' + parseInt(dayMatch[1]) + '_premium_prog' : 'day_generic_prog';
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
            const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
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
        }
"""

def fix_file(filename):
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        return

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the script section and replace/inject functions
    # We look for switchTab or copyCode which are common
    if "function toggleTask" in content:
        # Replace existing logic
        content = re.sub(r'function toggleTask.*?\n\s*}\s*\n\s*function updateProgress.*?\n\s*}\s*', 
                         standard_js.strip() + "\\n", content, flags=re.DOTALL)
        # Also ensure playStampSound is there
        if "function playStampSound" not in content:
            content = content.replace("</script>", standard_js + "\\n</script>")
    else:
        # Inject before </script>
        content = content.replace("</script>", standard_js + "\\n</script>")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed {filename}")

for f in files:
    fix_file(f)
