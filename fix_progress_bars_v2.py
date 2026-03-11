import os

files = [
    "vol01-1_ai_start.html",
    "vol02-1_canva_basics.html",
    "vol01-3_prompt.html",
    "vol04-1_nano_banana.html",
    "vol05-1_text_to_video.html"
]

# Standard JS Logic to Inject/Update
standard_js = r'''
        // --- Standardized Checklist & Progress Logic ---
        function toggleTask(taskId, element, groupId) {
            const done = element.classList.toggle('completed');
            state[taskId] = done;
            const dayKey = 'day' + document.title.split('|')[0].trim().replace('Day ', '') + '_premium_prog';
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
            } catch(e) { console.error("Audio error", e); }
        }
'''

def fix_file(filename):
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        return

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Simple approach: Find where toggleTask starts and where the next significant function starts or script ends
    if "function toggleTask" in content:
        # We'll replace from the start of toggleTask to the end of updateProgress
        # Since the structure is somewhat consistent, let's look for known ending markers
        start_idx = content.find("function toggleTask")
        
        # Look for the end of the boilerplate sequence
        # We'll just look for the next "Drag & Drop" or "// Copy" or similar
        end_markers = ["// Drag & Drop", "// Copy", "// Quiz", "</script>"]
        end_idx = -1
        for marker in end_markers:
            m_idx = content.find(marker, start_idx)
            if m_idx != -1:
                if end_idx == -1 or m_idx < end_idx:
                    end_idx = m_idx
        
        if end_idx != -1:
            new_content = content[:start_idx] + standard_js + "\n        " + content[end_idx:]
            content = new_content
            print(f"Fixed existing logic in {filename}")
    else:
        # Just inject before closing script
        content = content.replace("</script>", standard_js + "\n    </script>")
        print(f"Injected new logic in {filename}")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

for f in files:
    fix_file(f)
