import os

def build_html():
    css = """
        :root {
            --bg-body: #f8fafc;
            --bg-card: rgba(255, 255, 255, 0.85);
            --text-main: #0f172a;
            --text-sub: #475569;
            --accent: #10b981;
            --accent-light: #34d399;
            --accent-bg: #ecfdf5;
            --clickable: #0ea5e9;
            --danger: #ef4444;
            --glass-blur: blur(16px);
            --radius: 20px;
        }

        * { box-sizing: border-box; }

        body {
            margin: 0; padding: 0;
            font-family: 'Noto Sans JP', sans-serif;
            background: var(--bg-body);
            color: var(--text-main);
            background-image: 
                radial-gradient(ellipse at 10% 20%, rgba(16, 185, 129, 0.08), transparent 40%),
                radial-gradient(ellipse at 90% 80%, rgba(14, 165, 233, 0.08), transparent 40%);
            background-attachment: fixed;
            min-height: 100vh;
        }

        /* Fixed Header & Progress */
        .fixed-header {
            position: fixed; top: 0; left: 0; width: 100%;
            background: rgba(255, 255, 255, 0.9); backdrop-filter: var(--glass-blur);
            border-bottom: 1px solid rgba(0,0,0,0.05); z-index: 1000;
            padding: 1rem 2rem; display: flex; align-items: center; justify-content: space-between;
            box-shadow: 0 4px 20px rgba(0,0,0,0.02);
        }

        .back-link {
            color: var(--text-sub); text-decoration: none; font-weight: 700;
            display: flex; align-items: center; gap: 0.5rem; transition: color 0.3s;
        }
        .back-link:hover { color: var(--clickable); }

        .progress-container { flex-grow: 1; max-width: 400px; margin: 0 2rem; }
        .progress-text { display: flex; justify-content: space-between; font-size: 0.85rem; font-weight: 700; color: var(--accent); margin-bottom: 6px; }
        .progress-bar-bg { height: 10px; background: #e2e8f0; border-radius: 12px; overflow: hidden; }
        .progress-bar-fill { height: 100%; background: linear-gradient(90deg, var(--clickable), var(--accent)); width: 0%; border-radius: 12px; transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1); }

        /* Hero */
        .container { max-width: 1000px; margin: 100px auto 80px; padding: 0 20px; }
        .hero { text-align: center; margin-bottom: 3rem; animation: fadeInDown 0.8s ease; }
        .day-badge { background: var(--accent); color: #fff; padding: 0.4rem 1.5rem; border-radius: 30px; font-family: 'Teko', sans-serif; font-size: 1.5rem; letter-spacing: 2px; display: inline-block; margin-bottom: 1rem; }
        .hero h1 { font-size: clamp(2.2rem, 5vw, 3.5rem); margin: 0 0 1rem; font-weight: 900; letter-spacing: -1px; }
        .hero p { color: var(--text-sub); font-size: 1.1rem; max-width: 700px; margin: 0 auto; line-height: 1.8; }

        /* Tabs */
        .tab-container { display: flex; justify-content: center; gap: 1rem; margin-bottom: 3rem; }
        .tab-btn { background: #fff; border: 2px solid #e2e8f0; color: var(--text-sub); padding: 1rem 2.5rem; border-radius: 40px; cursor: pointer; font-weight: 700; font-size: 1rem; transition: all 0.3s; }
        .tab-btn:hover { border-color: var(--clickable); color: var(--clickable); }
        .tab-btn.active { background: var(--accent); color: #fff; border-color: var(--accent); box-shadow: 0 8px 20px rgba(16, 185, 129, 0.25); }
        
        .tab-content { display: none; animation: fadeIn 0.5s ease; }
        .tab-content.active { display: block; }
        .next-tab-btn { display: block; width: 100%; text-align: center; background: linear-gradient(135deg, var(--clickable), #3b82f6); color: #fff; padding: 1.2rem; border-radius: 16px; text-decoration: none; font-weight: 700; font-size: 1.1rem; margin-top: 2rem; border: none; cursor: pointer; transition: transform 0.3s, box-shadow 0.3s; }
        .next-tab-btn:hover { transform: translateY(-3px); box-shadow: 0 10px 25px rgba(14, 165, 233, 0.3); }

        /* Glass Card */
        .glass-card { background: var(--bg-card); backdrop-filter: var(--glass-blur); border: 1px solid rgba(255,255,255,0.7); border-radius: var(--radius); padding: 2.5rem; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.03); transition: transform 0.3s, box-shadow 0.3s; }
        .glass-card:hover { transform: translateY(-2px); box-shadow: 0 15px 35px rgba(0,0,0,0.05); }
        .card-header { display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem; border-bottom: 2px solid #f1f5f9; padding-bottom: 1rem; }
        .card-header i { font-size: 1.5rem; color: var(--accent); background: var(--accent-bg); padding: 1rem; border-radius: 14px; }
        .card-header h2 { margin: 0; font-size: 1.6rem; color: var(--text-main); }

        /* Bento Grid */
        .bento-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin: 2rem 0; }
        .bento-item { background: #fff; border: 1px solid #e2e8f0; border-radius: 16px; padding: 1.5rem; transition: all 0.3s; }
        .bento-item:hover { border-color: var(--clickable); box-shadow: 0 8px 24px rgba(14, 165, 233, 0.1); }
        .bento-item.card-magic { grid-column: 1 / -1; background: #0f172a; color: #fff; border: none; position: relative; overflow: hidden; }
        .bento-item.card-magic::before { content: ''; position: absolute; inset: 0; background: radial-gradient(circle at top right, rgba(16, 185, 129, 0.2), transparent 50%); }
        .bento-item h4 { margin: 0 0 1rem; font-size: 1.2rem; color: var(--clickable); display: flex; align-items: center; gap: 0.5rem;}
        .bento-item.card-magic h4 { color: var(--accent-light); }

        /* Workflow Timeline */
        .workflow { display: flex; flex-direction: column; gap: 1.5rem; position: relative; padding-left: 20px; margin: 2rem 0; }
        .workflow::before { content: ''; position: absolute; left: 34px; top: 10px; bottom: 10px; width: 3px; background: #e2e8f0; z-index: 0; }
        .flow-step { display: flex; align-items: flex-start; gap: 1.5rem; position: relative; z-index: 1; }
        .step-icon { width: 32px; height: 32px; background: var(--clickable); color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0; margin-top: 2px; border: 4px solid var(--bg-body); transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
        .flow-step:hover .step-icon { transform: scale(1.2); background: var(--accent); }
        .step-content { background: #fff; padding: 1.2rem; border-radius: 12px; border: 1px solid #e2e8f0; flex-grow: 1; box-shadow: 0 2px 10px rgba(0,0,0,0.02); }
        .step-content h4 { margin: 0 0 0.5rem; color: var(--text-main); }
        .step-content p { margin: 0; color: var(--text-sub); font-size: 0.95rem; }

        /* Browser Mockup */
        .browser-mockup { background: #1e293b; border-radius: 12px; overflow: hidden; margin: 1.5rem 0; box-shadow: 0 10px 25px rgba(0,0,0,0.15); border: 1px solid #334155; }
        .browser-header { background: #0f172a; padding: 12px 16px; display: flex; gap: 8px; border-bottom: 1px solid #334155; }
        .dot { width: 12px; height: 12px; border-radius: 50%; }
        .dot.red { background: #ff5f56; } .dot.yellow { background: #ffbd2e; } .dot.green { background: #27c93f; }
        .browser-content { padding: 1.5rem; color: #f8fafc; font-family: 'Fira Code', 'Consolas', monospace; font-size: 0.9rem; line-height: 1.6; white-space: pre-wrap; position: relative;}
        
        .copy-btn { position: absolute; top: 10px; right: 10px; background: rgba(255,255,255,0.1); color: #fff; border: 1px solid rgba(255,255,255,0.2); padding: 6px 12px; border-radius: 6px; cursor: pointer; display: flex; align-items: center; gap: 6px; font-size: 0.8rem; transition: all 0.2s; }
        .copy-btn:hover { background: rgba(255,255,255,0.2); }

        /* Mission Ticket & Wax Seal */
        .mission-ticket { background: #fff; border: 2px dashed #cbd5e1; border-radius: 16px; padding: 2rem; margin: 2rem 0; position: relative; display: flex; align-items: center; gap: 2rem; cursor: pointer; transition: all 0.3s; }
        .mission-ticket:hover { border-color: var(--clickable); background: #f0f9ff; }
        .ticket-stub { border-right: 2px dashed #cbd5e1; padding-right: 2rem; flex-shrink: 0; }
        .ticket-stub i { font-size: 2.5rem; color: var(--clickable); }
        .mission-content { flex-grow: 1; }
        .mission-content h3 { margin: 0 0 0.5rem; font-size: 1.3rem; }
        .mission-content p { margin: 0; color: var(--text-sub); }
        .mission-checkbox { width: 34px; height: 34px; border: 3px solid #cbd5e1; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; transition: all 0.3s; background: #fff; }
        .mission-ticket.completed .mission-checkbox { border-color: var(--accent); background: var(--accent); }
        .mission-checkbox i { color: #fff; font-size: 16px; opacity: 0; transform: scale(0); transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
        .mission-ticket.completed .mission-checkbox i { opacity: 1; transform: scale(1); }
        
        /* Wax Seal Animation */
        .wax-seal { position: absolute; top: -15px; right: 20px; width: 60px; height: 60px; background: radial-gradient(circle at 30% 30%, #fca5a5, #ef4444, #991b1b); border-radius: 50%; opacity: 0; transform: scale(3) rotate(-20deg); pointer-events: none; display: flex; align-items: center; justify-content: center; color: rgba(255,255,255,0.8); font-size: 1.5rem; box-shadow: inset 0 0 10px rgba(0,0,0,0.5), 0 5px 10px rgba(0,0,0,0.3); border: 2px solid #b91c1c; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.3)); }
        .wax-seal::after { content: ''; position: absolute; inset: 4px; border: 1px dotted rgba(255,255,255,0.4); border-radius: 50%; }
        .mission-ticket.completed .wax-seal { animation: stampIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards; }
        @keyframes stampIn {
            0% { opacity: 0; transform: scale(3) translateY(-50px) rotate(-20deg); }
            60% { opacity: 1; transform: scale(0.9) translateY(0) rotate(5deg); }
            80% { transform: scale(1.1) rotate(-2deg); }
            100% { opacity: 1; transform: scale(1) rotate(0deg); }
        }

        /* Accordion (Prompt List) */
        .prompt-accordion { margin-bottom: 1rem; border: 1px solid #e2e8f0; border-radius: 12px; background: #fff; overflow: hidden; transition: box-shadow 0.3s; }
        .prompt-accordion:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
        .prompt-accordion summary { padding: 1.2rem 1.5rem; font-weight: 700; font-size: 1.1rem; cursor: pointer; display: flex; align-items: center; gap: 1rem; list-style: none; background: #f8fafc; }
        .prompt-accordion summary::-webkit-details-marker { display: none; }
        .prompt-accordion summary i.fa-chevron-down { color: var(--text-sub); transition: transform 0.3s; margin-left: auto; }
        .prompt-accordion[open] summary i.fa-chevron-down { transform: rotate(180deg); }
        .prompt-accordion[open] summary { border-bottom: 1px solid #e2e8f0; background: #fff; }
        .prompt-content { padding: 1.5rem; animation: slideDown 0.3s ease; }
        @keyframes slideDown { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }

        /* Scenario Sandbox */
        .scenario-sandbox { background: #1e293b; border-radius: 16px; padding: 20px; display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 1.5rem 0; }
        .scenario-pane { background: #0f172a; border-radius: 12px; border: 1px solid #334155; display: flex; flex-direction: column; overflow: hidden;}
        .scenario-header { padding: 10px 15px; font-size: 0.85rem; font-weight: 700; text-align: center; color: #fff;}
        .scenario-header.bad { background: #991b1b; }
        .scenario-header.good { background: #065f46; }
        .scenario-body { padding: 15px; color: #cbd5e1; font-family: monospace; font-size: 0.9rem; white-space: pre-wrap; flex-grow: 1;}
        .scenario-result { padding: 15px; background: #1e293b; border-top: 1px solid #334155; border-bottom-left-radius: 12px; border-bottom-right-radius: 12px; font-size: 0.85rem; display: flex; align-items: center; gap: 10px;}
        .scenario-result img { width: 100%; border-radius: 8px; margin-top: 10px; }

        @media (max-width: 768px) {
            .scenario-sandbox { grid-template-columns: 1fr; }
        }

        /* Particles Context */
        #particleCanvas, #confettiCanvas { position: fixed; inset: 0; pointer-events: none; z-index: 9999; }

        /* Mute Button */
        .sound-toggle { position: fixed; bottom: 30px; left: 30px; background: #fff; border: 1px solid #e2e8f0; width: 44px; height: 44px; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 1000; box-shadow: 0 4px 12px rgba(0,0,0,0.1); color: var(--text-sub); transition: all 0.3s; }
        .sound-toggle:hover { color: var(--clickable); border-color: var(--clickable); transform: scale(1.1); }
        .sound-toggle.muted i::before { content: "\\f6a9"; } /* fa-volume-xmark */

        /* Secret Link */
        .secret-link { text-align: center; margin-top: 5rem; opacity: 0.4; transition: opacity 0.3s; }
        .secret-link:hover { opacity: 1; }
        .secret-link a { color: var(--text-sub); text-decoration: none; font-size: 0.85rem; display: inline-flex; align-items: center; gap: 5px; }

        /* Helpers */
        .tag { background: #e0f2fe; color: #0284c7; padding: 2px 8px; border-radius: 6px; font-size: 0.8rem; font-weight: 700; margin-right: 5px;}
        
        /* Quiz Area */
        .quiz-container { background: #fff; border: 2px solid #e2e8f0; border-radius: 16px; padding: 2rem; margin-top: 3rem; text-align: center;}
        .quiz-container h3 { margin-top: 0; color: var(--clickable); font-size: 1.5rem; }
        .quiz-options { display: flex; flex-direction: column; gap: 10px; max-width: 500px; margin: 20px auto; }
        .quiz-option { padding: 15px; border: 2px solid #e2e8f0; border-radius: 10px; cursor: pointer; transition: all 0.2s; font-weight: 700; background: #f8fafc;}
        .quiz-option:hover { border-color: var(--clickable); background: #f0f9ff; }
        .quiz-option.correct { background: var(--accent-bg); border-color: var(--accent); color: var(--accent); }
        .quiz-option.incorrect { background: #fef2f2; border-color: var(--danger); color: var(--danger); }
        .quiz-feedback { margin-top: 15px; font-weight: 700; height: 24px; }
        .quiz-next { margin-top: 20px; padding: 10px 20px; background: var(--clickable); color: #fff; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; display: none; margin-left: auto; margin-right: auto;}
    """

    js = """
        // Audio Context setup
        let audioCtx;
        let isMuted = false;

        function initAudio() {
            if (!audioCtx) {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }
        }

        function playSound(type) {
            if (isMuted) return;
            initAudio();
            if (audioCtx.state === 'suspended') audioCtx.resume();
            
            const osc = audioCtx.createOscillator();
            const gainNode = audioCtx.createGain();
            osc.connect(gainNode);
            gainNode.connect(audioCtx.destination);
            
            const now = audioCtx.currentTime;
            
            switch(type) {
                case 'click':
                    osc.type = 'sine';
                    osc.frequency.setValueAtTime(600, now);
                    osc.frequency.exponentialRampToValueAtTime(300, now + 0.1);
                    gainNode.gain.setValueAtTime(0.1, now);
                    gainNode.gain.exponentialRampToValueAtTime(0.01, now + 0.1);
                    osc.start(now);
                    osc.stop(now + 0.1);
                    break;
                case 'stamp':
                    osc.type = 'sawtooth';
                    osc.frequency.setValueAtTime(150, now);
                    osc.frequency.exponentialRampToValueAtTime(40, now + 0.2);
                    gainNode.gain.setValueAtTime(0.3, now);
                    gainNode.gain.exponentialRampToValueAtTime(0.01, now + 0.2);
                    osc.start(now);
                    osc.stop(now + 0.2);
                    break;
                case 'magic':
                    osc.type = 'sine';
                    osc.frequency.setValueAtTime(800, now);
                    osc.frequency.linearRampToValueAtTime(1200, now + 0.1);
                    osc.frequency.linearRampToValueAtTime(1600, now + 0.2);
                    gainNode.gain.setValueAtTime(0, now);
                    gainNode.gain.linearRampToValueAtTime(0.1, now + 0.1);
                    gainNode.gain.linearRampToValueAtTime(0, now + 0.3);
                    osc.start(now);
                    osc.stop(now + 0.3);
                    break;
                case 'clear':
                    osc.type = 'triangle';
                    // Arpeggio C E G C
                    [523.25, 659.25, 783.99, 1046.50].forEach((freq, i) => {
                        const t = now + (i * 0.15);
                        const o = audioCtx.createOscillator();
                        const g = audioCtx.createGain();
                        o.type = 'triangle';
                        o.connect(g);
                        g.connect(audioCtx.destination);
                        o.frequency.setValueAtTime(freq, t);
                        g.gain.setValueAtTime(0, t);
                        g.gain.linearRampToValueAtTime(0.1, t + 0.05);
                        g.gain.exponentialRampToValueAtTime(0.01, t + 0.3);
                        o.start(t);
                        o.stop(t + 0.3);
                    });
                    break;
            }
        }

        document.getElementById('toggleSound').addEventListener('click', function() {
            isMuted = !isMuted;
            this.classList.toggle('muted');
        });

        // Tab Switching
        function switchTab(tabId) {
            playSound('click');
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
            document.getElementById(tabId).classList.add('active');
            event.currentTarget.classList.add('active');
            window.scrollTo({top: 0, behavior: 'smooth'});
        }

        // Particle System for Magic Copy
        const canvas = document.getElementById('particleCanvas');
        const ctx = canvas.getContext('2d');
        let particles = [];

        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        class Particle {
            constructor(x, y) {
                this.x = x; this.y = y;
                const angle = Math.random() * Math.PI * 2;
                const speed = Math.random() * 5 + 2;
                this.vx = Math.cos(angle) * speed;
                this.vy = Math.sin(angle) * speed;
                this.life = 1.0;
                this.decay = Math.random() * 0.02 + 0.02;
                this.color = ['#fde047', '#fef08a', '#fbbf24'][Math.floor(Math.random() * 3)];
                this.size = Math.random() * 4 + 2;
            }
            update() {
                this.x += this.vx;
                this.y += this.vy;
                this.vy += 0.1; // gravity
                this.life -= this.decay;
            }
            draw() {
                ctx.globalAlpha = Math.max(0, this.life);
                ctx.fillStyle = this.color;
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fill();
            }
        }

        function createSparkles(e) {
            const rect = e.target.getBoundingClientRect();
            const x = rect.left + rect.width / 2;
            const y = rect.top + rect.height / 2;
            for (let i = 0; i < 30; i++) particles.push(new Particle(x, y));
            if (particles.length <= 30) animateParticles();
        }

        function animateParticles() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            particles.forEach((p, i) => {
                p.update(); p.draw();
                if (p.life <= 0) particles.splice(i, 1);
            });
            if (particles.length > 0) requestAnimationFrame(animateParticles);
            else ctx.clearRect(0, 0, canvas.width, canvas.height);
        }

        function copyPrompt(btn) {
            const pre = btn.nextElementSibling;
            navigator.clipboard.writeText(pre.innerText).then(() => {
                playSound('magic');
                createSparkles(event);
                const originalText = btn.innerHTML;
                btn.innerHTML = '<i class="fa-solid fa-check"></i> Copied!';
                setTimeout(() => btn.innerHTML = originalText, 2000);
            });
        }

        // Mission Logic
        let completedMissions = 0;
        const totalMissions = 2; // one per half
        function completeMission(el, id) {
            if (el.classList.contains('completed')) return; // Prevent unchecking logic for simplicity, or allow toggle
            
            // Toggle
            const isCompleted = el.classList.toggle('completed');
            if (isCompleted) {
                playSound('stamp');
                completedMissions++;
            } else {
                playSound('click');
                completedMissions--;
            }
            
            updateProgress();
        }

        function updateProgress() {
            const pct = Math.round((completedMissions / totalMissions) * 100);
            document.getElementById('progress-percent').innerText = pct + '%';
            document.getElementById('progress-bar').style.width = pct + '%';
            
            if (pct === 100 && completedMissions > 0) {
                setTimeout(() => {
                    playSound('clear');
                    fireConfetti();
                }, 600);
            }
        }

        // Accordion Sound
        document.querySelectorAll('details').forEach(d => {
            d.addEventListener('toggle', (e) => {
                if(d.open) playSound('click');
            });
        });

        // Simple Confetti (reusing particle logic roughly)
        const confCanvas = document.getElementById('confettiCanvas');
        const ctx2 = confCanvas.getContext('2d');
        confCanvas.width = window.innerWidth;
        confCanvas.height = window.innerHeight;
        let confettis = [];
        
        function fireConfetti() {
            for(let i=0; i<100; i++) {
                confettis.push({
                    x: window.innerWidth / 2,
                    y: window.innerHeight,
                    vx: (Math.random() - 0.5) * 20,
                    vy: (Math.random() * -15) - 10,
                    size: Math.random() * 10 + 5,
                    color: `hsl(${Math.random()*360}, 100%, 50%)`,
                    rot: Math.random() * 360,
                    rotSpeed: (Math.random() - 0.5) * 10
                });
            }
            animConfetti();
        }
        
        function animConfetti() {
            ctx2.clearRect(0,0,confCanvas.width, confCanvas.height);
            let active = false;
            confettis.forEach(c => {
                c.vy += 0.3; // gravity
                c.x += c.vx;
                c.y += c.vy;
                c.rot += c.rotSpeed;
                if(c.y < confCanvas.height + 20) active = true;
                
                ctx2.save();
                ctx2.translate(c.x, c.y);
                ctx2.rotate(c.rot * Math.PI / 180);
                ctx2.fillStyle = c.color;
                ctx2.fillRect(-c.size/2, -c.size/2, c.size, c.size);
                ctx2.restore();
            });
            if(active) requestAnimationFrame(animConfetti);
        }

        // Quiz Logic
        const quizData = [
            { question: "Nano Banana Proで「一貫したキャラクター」を維持するために最も重要な機能はどれですか？", options: ["スタイル参照 (Style Reference)", "キャラクター参照 (Character Reference)", "アスペクト比固定 (Aspect Ratio Lock)", "アップスケール (Upscale)"], answer: 1, tier: 1 },
            { question: "画像の一部分だけを指定して、新たなオブジェクトを追加・変更する技術を何と呼びますか？", options: ["アウトペイント (Outpainting)", "インペイント (Inpainting)", "被写界深度調整 (Depth of Field)", "設計図ガイド (Blueprint Guide)"], answer: 1, tier: 2 },
            { question: "特定の構図を厳密に守らせたい場合に、最も有効なアプローチはどれですか？", options: ["プロンプトで構図を長文で説明する", "ChatGPTに構図の指示文を書かせる", "ラフスケッチや設計図を用意して参照画像として読み込ませる", "画像の解像度を最大にする"], answer: 2, tier: 3 }
        ];
        let currentQuizIndex = 0;

        function renderQuiz() {
            const q = quizData[currentQuizIndex];
            document.getElementById('quiz-question').innerText = `Q${currentQuizIndex+1}. ${q.question} (Tier ${q.tier})`;
            const opts = document.getElementById('quiz-options');
            opts.innerHTML = '';
            q.options.forEach((opt, idx) => {
                const div = document.createElement('div');
                div.className = 'quiz-option';
                div.innerText = opt;
                div.onclick = () => checkQuiz(idx, q.answer, div);
                opts.appendChild(div);
            });
            document.getElementById('quiz-feedback').innerText = '';
            document.getElementById('quiz-next').style.display = 'none';
        }

        function checkQuiz(selected, correct, el) {
            const opts = document.querySelectorAll('.quiz-option');
            opts.forEach(o => o.onclick = null); // disable clicks
            if (selected === correct) {
                el.classList.add('correct');
                playSound('magic');
                document.getElementById('quiz-feedback').innerText = '正解！素晴らしいです！🎉';
                document.getElementById('quiz-feedback').style.color = 'var(--accent)';
                createSparkles({target: el});
            } else {
                el.classList.add('incorrect');
                opts[correct].classList.add('correct');
                playSound('click');
                document.getElementById('quiz-feedback').innerText = '惜しい！正解は緑色の選択肢です。';
                document.getElementById('quiz-feedback').style.color = 'var(--danger)';
            }
            if (currentQuizIndex < quizData.length - 1) {
                document.getElementById('quiz-next').style.display = 'block';
            } else {
                document.getElementById('quiz-next').style.display = 'inline-block';
                document.getElementById('quiz-next').innerText = '終了';
                document.getElementById('quiz-next').onclick = () => {
                    document.getElementById('quiz-container').innerHTML = '<h3><i class="fa-solid fa-award"></i> Quiz Completed!</h3><p>全問終了しました。総合理解度チェックに成績が反映されます（デモ）。</p>';
                };
            }
        }

        function nextQuiz() {
            playSound('click');
            currentQuizIndex++;
            renderQuiz();
        }

        window.onload = () => {
            renderQuiz();
        };
    """

    video1_prompts = [
        ("02:05 ①一貫性のあるキャラクターのポージング生成", "キャラクターの三面図やベース画像（Character Reference）を入力し、「走っている」「見上げている」などの動作を追加する。", "1人の女性、走っている、横顔、躍動感、スポーツウェア"),
        ("03:54 ②プロクオリティなサムネイルの新規作成", "テキスト要素を配置する余白（ネガティブスペース）を意識した構図をプロンプトで指定する。", "YouTubeサムネイル用背景、右側に大きな余白、左側に驚くビジネスマン、鮮やかな青背景、高品質、4k"),
        ("05:03 ③既存サムネイルの効率的な編集", "バリエーション生成（Vary）機能を使い、元の構図を保ちつつ色合いやモチーフを微調整する。", "(Vary機能使用) 背景を赤色に、人物の服をスーツに変更"),
        ("05:54 ④サムネイルの改善パターンを即時生成", "プロンプトの特定キーワードだけを差し替えて複数一気に生成。A/Bテスト用の素材を作る。", "YouTubeサムネイル用背景、右側に大きな余白、左側に[笑顔/怒る/泣く]ビジネスマン"),
        ("06:42 ⑤ポップな告知バナーの制作", "「アメコミ風」「ポップアート」「フラットデザイン」などのスタイルキーワードを強調する。", "ポップアートスタイル、アメコミ風、集中線、カラフルな背景、セール告知用バナーの背景素材"),
        ("07:43 ⑥日本語テキストの細かい微調整", "画像内のテキストをインペイント（部分修正）機能で消去し、Canva等で後から追加できるようにする。", "(Inpaint機能使用) テキスト部分をなぞり、プロンプトを「何もない無地の背景」にして修正"),
        ("08:22 ⑦分かりやすいインフォグラフィックスの制作", "「アイソメトリック（等角投影法）」「3Dアイコン」を指定して、図解に使えるパーツを生成する。", "アイソメトリック構図、3Dアイコン、光るパソコン、クリーンな白背景、インフォグラフィック素材"),
        ("09:20 ⑧画像のインペイントとアウトペイント", "アウトペイント機能で画像の上下左右を拡張し、アスペクト比を変えつつ自然な背景を継ぎ足す。", "(Zoom Out / Pan機能使用) 横長の16:9へ拡張、自然な森の風景を横に広げる"),
        ("10:02 ⑨既存の資料をベースにした素材作成", "粗い手書きのラフ図などを読み込ませ（Image to Image）、高精密なイラストに仕上げる。", "(Image to Image) このラフスケッチに基づいた、高品質な3Dレンダリングの家、リアルな光、晴れ"),
        ("10:47 ⑩クライアントの要望に沿ってピンポイントに表現を変える", "インペイント機能を使い、「コーヒーカップ」を「紅茶のティーカップ」に変更するなど、特定箇所だけ書き換える。", "(部分選択) 紅茶が入ったアンティークなティーカップ、湯気"),
        ("11:42 ⑪大量の素材やキャラクターの組み合わせ", "要素をカンマで区切り、重み付け（Weight）パラメーターを使って配置バランスを調整する。", "可愛い犬::2、かっこいい猫::1、公園の中、並んで座っている"),
        ("12:27 ⑫設計図を利用した細かな構図の指定", "棒人間や簡単なポーズ図をControlNet（設計図ガイド）に入れて、その通りのポーズを取らせる。", "(Pose Reference使用) 腕を組んで自信満々に立つスーツの男性、超リアル、8k"),
        ("13:07 ⑬参照画像を使ったスタイルの変換", "「スタイル参照（Style Reference: sref）」を用いて、特定のイラストレーター風のタッチを別のモチーフに適用する。", "(sref 参照画像URL) サイバーパンク都市、雨、ネオンライト"),
        ("13:48 ⑭アスペクト比の完全な修正と維持", "「--ar 16:9」などのパラメーターを付与し、用途にあった正確な比率を指定する。", "美しい夕焼けの海、ヤシの木 --ar 16:9"),
        ("14:38 ⑮写真をパーツごとに分解する", "緑色や白の背景（グリーンバック）を指定し、後から編集ソフトで切り抜きやすくする。", "シンプルな椅子、白背景、スタジオ照明、影なし --no shadow"),
        ("15:32 ⑯高解像度へのアップスケール", "生成された画像を「Upscale（Creative/Subtle）」ボタンで品質を保ったまま高解像度化する。", "(Upscaleボタン実行による高画質化)"),
        ("16:29 ⑰リアルなライティング効果の変更", "「シネマティックライティング」「リムライト」「ゴールデンアワー」等、光の当たり方を指定。", "ポートレート、女性、横顔、シネマティックライティング、バックライト、リムライト、被写体ブレなし"),
        ("17:20 ⑱ピント(被写界深度)の調整", "「ボケ味（Bokeh）」「F値1.4」「マクロ撮影」などカメラのレンズ特性をプロンプトに入れる。", "マクロ撮影、葉にとまる水滴、背景は強くボケている(ボケ味)、F値1.4、超高解像度"),
        ("18:00 ⑲ChatGPT連携による大量生成", "ChatGPTに「Midjourney用のプロンプトを10パターン英語で出力して」と指示し、コピペで量産する。", "(ChatGPTで生成した英語プロンプトをそのまま入力)"),
        ("19:03 ⑳Flow連携による動画の生成(開始と終了の指定)", "静止画を2枚用意し、「AからBへ変化する」AIビデオ生成ツール（LumaやKling等）への繋ぎとして活用する。", "画像A（昼の街）と画像B（夜の街）を生成し、外部ツールで動画化")
    ]

    video2_prompts = [
        ("1. 髪型の変更 [02:03]", "インペイントで髪部分を選択し、髪型を指定。例：「ショートボブ、金髪」", "ショートボブのヘアスタイル、金髪、風になびく"),
        ("2. 顔の表情を変更 [03:18]", "インペイントで口元や目元を選択。「笑顔」や「驚き」等の感情を追加。", "大きな笑顔、白い歯、輝く目"),
        ("3. 服の変更 [03:41]", "インペイントで服全体を選択。「春のカジュアルなワンピース」などに変更。", "黄色い春のカジュアルなワンピース、花柄"),
        ("4. アスペクト比の変更 [04:59]", "Zoom OutまたはPan機能で縦横比を変える。", "(Zoom Out機能使用) 背景のカフェを広く見せる"),
        ("5. オブジェクトの削除 [05:31]", "インペイントで不要なオブジェクトを選択し、プロンプトを空にするか背景を指示。", "木製のテーブルのみ"),
        ("6. オブジェクトの削除（工夫あり） [05:57]", "単純に消すのではなく、「開いたスペースに観葉植物を置く」など自然な補完を行う。", "小さな緑の観葉植物、白い鉢"),
        ("7. 一貫したキャラクター（架空） [06:33]", "「Character Reference (--cref)」を使用して、同じ架空の人物を異なるシーンで生成。", "コーヒーを飲む、カフェのテラス --cref [画像URL] --cw 100"),
        ("8. 一貫したキャラクター（実在） [07:01]", "実在の人物の写真をcrefに入れ、似た人物の画像を生成（肖像権には注意が必要）。", "スーツを着てプレゼンする、会議室 --cref [写真URL]"),
        ("9. 設計図を使ってガイド [08:03]", "下書きや骨組み画像を元に生成（ControlNet等の機能）。", "モダンなリビングルーム、大きな窓、観葉植物 (ベース線画あり)"),
        ("10. 設計図の微修正 [08:50]", "線画の強さ（ウェイト）を調整し、AIの自由度を高める・低くする。", "--iw 0.5 (画像への忠実度パラメーターの調整)"),
        ("11. 製品広告 [09:11]", "商品の背景を豪華にする。「高級感」「水しぶき」などを追加。", "高級化粧品のボトル、黒い大理石の上、金色の水しぶき、ドラマチックな照明"),
        ("12. 素材演出 [10:14]", "布の質感や金属の反射など、マテリアルに特化した指定。", "シルクの布が風に舞う、柔らかい光、パステルピンク"),
        ("13. 食品の演出 [10:46]", "シズル感（湯気、照り、滴るシロップ）を強調する。", "焼きたてのハンバーガー、とろけるチーズ、ほとばしる肉汁、湯気、超リアル、食品広告"),
        ("14. 解体ショットを作成 [11:00]", "Knolling（ノウリング：分解して整然と並べる構図）を指定。", "カメラの分解図、ノウリング構図、真上からの視点、青い背景、整理整頓"),
        ("15. ロゴの変更 [11:11]", "無地のTシャツや看板を生成し、後からCanvaでロゴを合成するための素材作り。", "無地の黒いTシャツを着た若者、真っ白な看板"),
        ("16. 製品モックアップ [11:34]", "ブランクのスマホ画面やポスターフレームを生成。", "木製テーブルの上のiPhone15 モックアップ、画面は真っ白（グリーン）、自然光"),
        ("17. 文字の追加/変更 [11:50]", "引用符（\"\"）で囲んでテキストを描画させる（最新モデルv6以降で有効）。", 'ネオンサインで "HELLO WORLD" と書かれている、路地裏'),
        ("18. 文字の追加/変更（失敗例） [11:59]", "長文や複雑な日本語は崩れるため、テキストは短くするか画像編集ソフトで後載せする。", "※AI生成は文字に弱いため、バウンディングボックスだけ生成してCanvaで文字を入れる手法を解説"),
        ("19. プロの証明写真の作成 [12:29]", "「スタジオライティング」「無地背景」「プロのポートレート」を指定。", "プロのビジネスポートレート、日本人男性30代、グレーの無地背景、笑顔、スタジオ照明")
    ]

    def build_accordions(prompts):
        html = ""
        for i, (title, desc, prompt) in enumerate(prompts):
            html += f'''
            <details class="prompt-accordion">
                <summary><span class="tag">Tip {i+1}</span> {title} <i class="fa-solid fa-chevron-down"></i></summary>
                <div class="prompt-content">
                    <p style="margin-top:0;"><strong>解説:</strong> {desc}</p>
                    <div class="browser-mockup">
                        <div class="browser-header">
                            <div class="dot red"></div><div class="dot yellow"></div><div class="dot green"></div>
                        </div>
                        <div class="browser-content">
                            <button class="copy-btn" onclick="copyPrompt(this)"><i class="fa-regular fa-copy"></i> Copy</button>
                            <pre style="margin:0; font-family:inherit;">{prompt}</pre>
                        </div>
                    </div>
                </div>
            </details>
            '''
        return html

    half1_accordions = build_accordions(video1_prompts)
    half2_accordions = build_accordions(video2_prompts)

    doc = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day 4 | Nano Banana Pro & Image Generation</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Noto+Sans+JP:wght@400;700&family=Teko:wght@500;600;700&family=Fira+Code&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>{css}</style>
</head>
<body>
    <canvas id="particleCanvas"></canvas>
    <canvas id="confettiCanvas"></canvas>

    <!-- Mute Button -->
    <button id="toggleSound" class="sound-toggle" title="Toggle Sound"><i class="fa-solid fa-volume-high"></i></button>

    <!-- Fixed Header -->
    <header class="fixed-header">
        <a href="index.html" class="back-link"><i class="fa-solid fa-arrow-left"></i> Course Home</a>
        <div class="progress-container">
            <div class="progress-text"><span>Day 4 Progress</span><span id="progress-percent">0%</span></div>
            <div class="progress-bar-bg"><div class="progress-bar-fill" id="progress-bar"></div></div>
        </div>
        <div style="width:100px;"></div>
    </header>

    <div class="container">
        <!-- Hero -->
        <div class="hero">
            <div class="day-badge">DAY 04</div>
            <h1>Nano Banana Pro 魔法の活用術</h1>
            <p>本日の目標：テキストから画像への変換技術の基礎をマスターする。<br>動画で紹介された合計39の活用事例を完全にカタログ化しました。コピーしてすぐに使えます。</p>
        </div>

        <!-- Tabs -->
        <div class="tab-container">
            <button class="tab-btn active" onclick="switchTab('half1')">前半：活用術20選（動画編集者向け）</button>
            <button class="tab-btn" onclick="switchTab('half2')">後半：活用術19選（今すぐ使える全般）</button>
        </div>

        <!-- ================= HALF 1 ================= -->
        <div id="half1" class="tab-content active">
            
            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-solid fa-book-open-reader"></i>
                    <h2>No Video Reliance 原則</h2>
                </div>
                <p>動画を視聴しなくても、このページだけで全てのプロンプトのテクニックが習得できるように構成されています。要素を展開して、具体的なプロンプトを確認してください。</p>
                
                <div class="bento-grid">
                    <div class="bento-item card-magic">
                        <h4><i class="fa-solid fa-wand-magic-sparkles"></i> The Magic of Few-Shot</h4>
                        <p>AIへの指示は「ゼロショット（単語のみ）」よりも、「フューショット（具体例付き）」の方が圧倒的に精度が高まります。下記の Scenario Sandbox で比較してみましょう。</p>
                    </div>
                </div>

                <!-- Scenario Sandbox -->
                <div class="scenario-sandbox">
                    <div class="scenario-pane">
                        <div class="scenario-header bad">❌ Zero-Shot (失敗例)</div>
                        <div class="scenario-body">かっこいい犬の画像</div>
                        <div class="scenario-result"><i class="fa-solid fa-robot"></i>「ありきたりな犬の写真が生成されました」</div>
                    </div>
                    <div class="scenario-pane">
                        <div class="scenario-header good">✅ Few-Shot / 詳細指定 (成功例)</div>
                        <div class="scenario-body">ゴールデンレトリバー、サングラスをかけている、サイバーパンクの街、ネオンライト、シネマティックライティング、8k resolution</div>
                        <div class="scenario-result"><i class="fa-solid fa-wand-magic"></i>「プロゲーマーのような高品質な犬の画像が生成されました！」</div>
                    </div>
                </div>
            </div>

            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-solid fa-list"></i>
                    <h2>動画編集者向け 活用術20選</h2>
                </div>
                <p>アコーディオンをクリックして解説とプロンプトを展開し、コピーボタンでコピーしてください。(コピー時に火花の魔法がかかります✨)</p>
                {half1_accordions}
            </div>

            <!-- Mission -->
            <div class="mission-ticket" onclick="completeMission(this, 'm1')">
                <div class="wax-seal"><i class="fa-solid fa-crown"></i></div>
                <div class="ticket-stub"><i class="fa-solid fa-ticket-simple"></i></div>
                <div class="mission-content">
                    <h3>Mission 1: 基礎テクニックの習得</h3>
                    <p>前半のプロンプトを最低3つコピーして、AI画像生成ツールで実際に生成してみましょう。</p>
                </div>
                <div class="mission-checkbox"><i class="fa-solid fa-check"></i></div>
            </div>

            <button class="next-tab-btn" onclick="switchTab('half2')">後半：活用事例19選 へ進む <i class="fa-solid fa-arrow-right"></i></button>
        </div>

        <!-- ================= HALF 2 ================= -->
        <div id="half2" class="tab-content">
            
            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-solid fa-layer-group"></i>
                    <h2>実践：今すぐ使える活用事例19選</h2>
                </div>
                <p>インペイント（部分修正）やアスペクト比の変更など、生成後の「加工」に特化したテクニック集です。</p>
                
                <div class="workflow">
                    <div class="flow-step">
                        <div class="step-icon">1</div>
                        <div class="step-content">
                            <h4>ベース画像を生成</h4>
                            <p>まずは大枠となる画像をシンプルに生成します。</p>
                        </div>
                    </div>
                    <div class="flow-step">
                        <div class="step-icon">2</div>
                        <div class="step-content">
                            <h4>インペイントで部分指定</h4>
                            <p>変更したい部分（服、背景、オブジェクト）だけを投げ縄ツール等で囲みます。</p>
                        </div>
                    </div>
                    <div class="flow-step">
                        <div class="step-icon">3</div>
                        <div class="step-content">
                            <h4>追加プロンプトを実行</h4>
                            <p>囲んだ部分に適用したい新しいプロンプトを入力し再生成します。</p>
                        </div>
                    </div>
                </div>

                {half2_accordions}
            </div>

            <!-- Mission -->
            <div class="mission-ticket" onclick="completeMission(this, 'm2')">
                <div class="wax-seal" style="background: radial-gradient(circle at 30% 30%, #6ee7b7, #10b981, #047857); border-color: #047857;"><i class="fa-solid fa-star"></i></div>
                <div class="ticket-stub"><i class="fa-solid fa-ticket-simple" style="color:#10b981;"></i></div>
                <div class="mission-content">
                    <h3>Mission 2: 部分最適化の習得</h3>
                    <p>一度生成した画像の服や表情をプロンプトで変更する体験をしましょう。</p>
                </div>
                <div class="mission-checkbox"><i class="fa-solid fa-check"></i></div>
            </div>

            <!-- Quiz -->
            <div class="quiz-container" id="quiz-container">
                <h3><i class="fa-solid fa-brain"></i> 理解度チェック</h3>
                <p id="quiz-question"></p>
                <div class="quiz-options" id="quiz-options"></div>
                <div class="quiz-feedback" id="quiz-feedback"></div>
                <button class="quiz-next" id="quiz-next" onclick="nextQuiz()">次の問題へ</button>
            </div>

            <!-- Developer Log Secret Link -->
            <div class="secret-link">
                <a href="index_dev_notes.html"><i class="fa-solid fa-code"></i> Engineering Design Log (Developer Notes) 🤫</a>
            </div>

        </div>
    </div>
    
    <script>{js}</script>
</body>
</html>
"""

    with open(r'g:\マイドライブ\研修\【202603】生成AIとプロンプト\vol04-1_nano_banana.html', 'w', encoding='utf-8') as f:
        f.write(doc)
    print("vol04-1_nano_banana.html generated successfully.")

if __name__ == '__main__':
    build_html()
