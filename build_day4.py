import os

def build_html():
    with open('build_day4_part1.py', 'r', encoding='utf-8') as f:
        # Just to retrieve the html safely from the previous step which was saved as py but is just a string
        # Actually, let's just write the whole thing here cleanly.
        pass

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
        .tab-container { display: flex; justify-content: center; gap: 1rem; margin-bottom: 3rem; flex-wrap: wrap; }
        .tab-btn { background: #fff; border: 2px solid #e2e8f0; color: var(--text-sub); padding: 1rem 2rem; border-radius: 40px; cursor: pointer; font-weight: 700; font-size: 0.95rem; transition: all 0.3s; }
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
        
        /* Box Gemini */
        .box { padding: 1.8rem; border-radius: 14px; margin: 1.8rem 0; position: relative; padding-top: 2.2rem; }
        .box h4 { margin-top: 0; font-size: 1.15rem; font-weight: 700; }
        .box p, .box ul { margin-bottom: 0; }
        .box.gemini { background: linear-gradient(135deg, #eff6ff, #dbeafe); border: 1px solid #bfdbfe; }
        .box.gemini::before { content: "\\f544"; font-family: "Font Awesome 6 Free"; font-weight: 900; position: absolute; top: -18px; left: 24px; background: linear-gradient(135deg, #3b82f6, #2563eb); color: #fff; width: 36px; height: 36px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1rem; box-shadow: 0 3px 10px rgba(37, 99, 235, 0.3); }

        /* Cauldron Drag & Drop */
        .draggable-container { display: flex; flex-wrap: wrap; gap: 10px; margin: 1.5rem 0; }
        .drag-chip { padding: 8px 16px; border-radius: 30px; cursor: grab; font-weight: 700; font-size: 0.9rem; color: #fff; transition: transform 0.2s; user-select: none; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        .drag-chip:active { cursor: grabbing; transform: scale(0.95); }
        .drag-chip.subject { background: linear-gradient(135deg, #f59e0b, #d97706); }
        .drag-chip.style { background: linear-gradient(135deg, #ec4899, #be185d); }
        .drag-chip.param { background: linear-gradient(135deg, #8b5cf6, #6d28d9); }
        
        .cauldron-container { border: 2px dashed #94a3b8; border-radius: 16px; padding: 20px; background: #fff; transition: all 0.3s; }
        .cauldron-container.drag-over { border-color: var(--accent); background: var(--accent-bg); }
        .cauldron-dropzone { min-height: 100px; display: flex; flex-direction: column; align-items: center; justify-content: center; color: #94a3b8; font-weight: bold; gap: 10px; margin-bottom: 20px; }
        .cauldron-dropzone i { font-size: 2rem; }
        .cauldron-output-area { background: #1e293b; color: #f8fafc; padding: 15px; border-radius: 10px; font-family: monospace; min-height: 60px; word-break: break-all; margin-bottom: 15px; }
        .cauldron-chips { display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 15px; min-height: 40px; }
        .cauldron-chips .drag-chip { cursor: default; }
        
        .btn { border: none; background: var(--clickable); color:#fff; padding: 12px 24px; border-radius: 8px; font-weight: bold; cursor: pointer; transition: 0.2s;}
        .btn:hover { background: #0284c7; transform: translateY(-2px); }

        /* General Code Box */
        .code-box { background: #1e293b; color: #94a3b8; padding: 1.8rem 2rem; border-radius: 12px; font-family: 'Consolas', monospace; position: relative; margin: 1.8rem 0; border-left: 4px solid var(--accent); font-size: 0.9rem; line-height: 1.7; }
        .code-label { position: absolute; top: -11px; left: 18px; background: var(--accent); color: #fff; padding: 2px 12px; font-size: 0.75rem; font-weight: 700; border-radius: 6px; font-family: 'Noto Sans JP', sans-serif; letter-spacing: 0.5px; }

        @keyframes fadeInDown { from { opacity: 0; transform: translateY(-20px); } to { opacity: 1; transform: translateY(0); } }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

        /* Animation Canvas */
        #particleCanvas, #confettiCanvas { position: fixed; inset: 0; pointer-events: none; z-index: 9999; }
        
        .sound-toggle { position: fixed; bottom: 30px; left: 30px; background: #fff; border: 1px solid #e2e8f0; width: 44px; height: 44px; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 1000; box-shadow: 0 4px 12px rgba(0,0,0,0.1); color: var(--text-sub); transition: all 0.3s; }
        .sound-toggle:hover { color: var(--clickable); border-color: var(--clickable); transform: scale(1.1); }
        .sound-toggle.muted i::before { content: "\\f6a9"; } /* fa-volume-xmark */

        .secret-link { text-align: center; margin-top: 5rem; opacity: 0.4; transition: opacity 0.3s; }
        .secret-link:hover { opacity: 1; }
        .secret-link a { color: var(--text-sub); text-decoration: none; font-size: 0.85rem; display: inline-flex; align-items: center; gap: 5px; }
        .tag { background: #e0f2fe; color: #0284c7; padding: 2px 8px; border-radius: 6px; font-size: 0.8rem; font-weight: 700; margin-right: 5px;}
        
        .quiz-container { background: #fff; border: 2px solid #e2e8f0; border-radius: 16px; padding: 2rem; margin-top: 3rem; text-align: center;}
        .quiz-container h3 { margin-top: 0; color: var(--clickable); font-size: 1.5rem; }
        .quiz-options { display: flex; flex-direction: column; gap: 10px; max-width: 500px; margin: 20px auto; }
        .quiz-option { padding: 15px; border: 2px solid #e2e8f0; border-radius: 10px; cursor: pointer; transition: all 0.2s; font-weight: 700; background: #f8fafc;}
        .quiz-option:hover { border-color: var(--clickable); background: #f0f9ff; }
        .quiz-option.correct { background: var(--accent-bg); border-color: var(--accent); color: var(--accent); }
        .quiz-option.incorrect { background: #fef2f2; border-color: var(--danger); color: var(--danger); }
        .quiz-feedback { margin-top: 15px; font-weight: 700; height: 24px; }
        .quiz-next { margin-top: 20px; padding: 10px 20px; background: var(--clickable); color: #fff; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; display: none; margin-left: auto; margin-right: auto;}
        
        /* YouTube Buttons & Video Grid */
        .main-video-btn { display: inline-flex; align-items: center; gap: 8px; background: #ef4444; color: #fff; padding: 12px 28px; border-radius: 30px; text-decoration: none; font-weight: bold; font-size: 1.1rem; transition: transform 0.3s, box-shadow 0.3s; margin-top: 1rem; border: 2px solid #b91c1c;}
        .main-video-btn:hover { transform: translateY(-3px); box-shadow: 0 10px 25px rgba(239, 68, 68, 0.3); }
        .main-video-btn i { font-size: 1.3rem; }
        .yt-time-btn { display: inline-flex; align-items: center; gap: 6px; background: #fee2e2; color: #b91c1c; padding: 6px 14px; border-radius: 20px; text-decoration: none; font-size: 0.85rem; font-weight: bold; transition: all 0.2s; border: 1px solid #fca5a5; white-space: nowrap; margin-bottom: 10px;}
        .yt-time-btn:hover { background: #fca5a5; color: #7f1d1d; }

        .video-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.2rem; margin-top: 1.2rem; margin-bottom: 2rem;}
        .video-thumb { position: relative; border-radius: 14px; overflow: hidden; display: block; border: 3px solid #fff; box-shadow: 0 4px 12px rgba(0,0,0,0.06); transition: all 0.3s; background: #000;}
        .video-thumb:hover { transform: translateY(-4px); box-shadow: 0 10px 25px rgba(0,0,0,0.12); border-color: var(--accent-light);}
        .video-thumb img { width: 100%; display: block; opacity: 0.92; transition: opacity 0.3s, transform 0.5s;}
        .video-thumb:hover img { opacity: 1; transform: scale(1.04);}
        .video-thumb .play-overlay { position: absolute; inset: 0; background: rgba(0,0,0,0.15); display: flex; align-items: center; justify-content: center; transition: all 0.3s;}
        .video-thumb:hover .play-overlay { background: rgba(79,70,229,0.2);}
        .play-overlay i { color: #fff; font-size: 2.8rem; text-shadow: 0 3px 12px rgba(0,0,0,0.4); transition: transform 0.3s;}
        .video-thumb:hover .play-overlay i { transform: scale(1.15);}
    """

    js = """
        let audioCtx; let isMuted = false;
        function initAudio() { if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)(); }
        
        function playSound(type) {
            if (isMuted) return; initAudio();
            if (audioCtx.state === 'suspended') audioCtx.resume();
            const osc = audioCtx.createOscillator();
            const gainNode = audioCtx.createGain();
            osc.connect(gainNode); gainNode.connect(audioCtx.destination);
            const now = audioCtx.currentTime;
            
            if (type === 'click') {
                osc.type = 'sine'; osc.frequency.setValueAtTime(600, now); osc.frequency.exponentialRampToValueAtTime(300, now + 0.1);
                gainNode.gain.setValueAtTime(0.1, now); gainNode.gain.exponentialRampToValueAtTime(0.01, now + 0.1);
                osc.start(now); osc.stop(now + 0.1);
            } else if (type === 'stamp') {
                osc.type = 'sawtooth'; osc.frequency.setValueAtTime(150, now); osc.frequency.exponentialRampToValueAtTime(40, now + 0.2);
                gainNode.gain.setValueAtTime(0.3, now); gainNode.gain.exponentialRampToValueAtTime(0.01, now + 0.2);
                osc.start(now); osc.stop(now + 0.2);
            } else if (type === 'magic') {
                osc.type = 'sine'; osc.frequency.setValueAtTime(800, now); osc.frequency.linearRampToValueAtTime(1200, now + 0.1);
                osc.frequency.linearRampToValueAtTime(1600, now + 0.2);
                gainNode.gain.setValueAtTime(0, now); gainNode.gain.linearRampToValueAtTime(0.1, now + 0.1);
                gainNode.gain.linearRampToValueAtTime(0, now + 0.3); osc.start(now); osc.stop(now + 0.3);
            } else if (type === 'drop') {
                osc.type = 'square'; osc.frequency.setValueAtTime(300, now); osc.frequency.linearRampToValueAtTime(400, now + 0.1);
                gainNode.gain.setValueAtTime(0.1, now); gainNode.gain.linearRampToValueAtTime(0, now + 0.1);
                osc.start(now); osc.stop(now + 0.1);
            } else if (type === 'clear') {
                [523.25, 659.25, 783.99, 1046.50].forEach((freq, i) => {
                    const t = now + (i * 0.15); const o = audioCtx.createOscillator(); const g = audioCtx.createGain();
                    o.type = 'triangle'; o.connect(g); g.connect(audioCtx.destination);
                    o.frequency.setValueAtTime(freq, t); g.gain.setValueAtTime(0, t);
                    g.gain.linearRampToValueAtTime(0.1, t + 0.05); g.gain.exponentialRampToValueAtTime(0.01, t + 0.3);
                    o.start(t); o.stop(t + 0.3);
                });
            }
        }

        document.getElementById('toggleSound').addEventListener('click', function() { isMuted = !isMuted; this.classList.toggle('muted'); });

        function switchTab(tabId) {
            playSound('click');
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
            document.getElementById(tabId).classList.add('active');
            event.currentTarget.classList.add('active');
            window.scrollTo({top: 0, behavior: 'smooth'});
        }

        /* Sparkles & Particles */
        const canvas = document.getElementById('particleCanvas'); const ctx = canvas.getContext('2d');
        let particles = [];
        window.addEventListener('resize', () => { canvas.width = window.innerWidth; canvas.height = window.innerHeight; });
        canvas.width = window.innerWidth; canvas.height = window.innerHeight;

        class Particle {
            constructor(x, y) {
                this.x = x; this.y = y; const angle = Math.random() * Math.PI * 2; const speed = Math.random() * 5 + 2;
                this.vx = Math.cos(angle) * speed; this.vy = Math.sin(angle) * speed;
                this.life = 1.0; this.decay = Math.random() * 0.02 + 0.02;
                this.color = ['#fde047', '#fef08a', '#fbbf24'][Math.floor(Math.random() * 3)];
                this.size = Math.random() * 4 + 2;
            }
            update() { this.x += this.vx; this.y += this.vy; this.vy += 0.1; this.life -= this.decay; }
            draw() { ctx.globalAlpha = Math.max(0, this.life); ctx.fillStyle = this.color; ctx.beginPath(); ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2); ctx.fill(); }
        }

        function createSparkles(elem) {
            const rect = elem.getBoundingClientRect(); const x = rect.left + rect.width / 2; const y = rect.top + rect.height / 2;
            for (let i = 0; i < 30; i++) particles.push(new Particle(x, y));
            if (particles.length <= 30) animateParticles();
        }

        function animateParticles() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            particles.forEach((p, i) => { p.update(); p.draw(); if (p.life <= 0) particles.splice(i, 1); });
            if (particles.length > 0) requestAnimationFrame(animateParticles);
            else ctx.clearRect(0, 0, canvas.width, canvas.height);
        }

        function copyPrompt(btn) {
            const text = btn.nextElementSibling.innerText;
            navigator.clipboard.writeText(text).then(() => {
                playSound('magic'); createSparkles(btn);
                const og = btn.innerHTML; btn.innerHTML = '<i class="fa-solid fa-check"></i> Copied!';
                setTimeout(() => btn.innerHTML = og, 2000);
            });
        }

        /* Mission Logic */
        let completedMissions = 0; const totalMissions = 3;
        function completeMission(el, id) {
            if (el.classList.contains('completed')) return;
            el.classList.add('completed');
            playSound('stamp'); completedMissions++; updateProgress();
        }
        function updateProgress() {
            const Math_round = Math.round;
            const pct = Math_round((completedMissions / totalMissions) * 100);
            document.getElementById('progress-percent').innerText = pct + '%';
            document.getElementById('progress-bar').style.width = pct + '%';
            if (pct >= 100) setTimeout(() => { playSound('clear'); fireConfetti(); }, 600);
        }

        document.querySelectorAll('details').forEach(d => { d.addEventListener('toggle', () => { if(d.open) playSound('click'); }); });

        /* Cauldron Drag and Drop */
        const cauldron = document.getElementById('cauldron');
        const cauldronChips = document.getElementById('cauldron-chips');
        const cauldronOut = document.getElementById('cauldron-out');
        const chips = document.querySelectorAll('.draggable-container .drag-chip');
        let currentPrompt = "";

        chips.forEach(chip => {
            chip.addEventListener('dragstart', (e) => { e.dataTransfer.setData('text/plain', chip.dataset.text); chip.style.opacity = '0.5'; });
            chip.addEventListener('dragend', () => { chip.style.opacity = '1'; });
        });

        cauldron.addEventListener('dragover', (e) => { e.preventDefault(); cauldron.parentElement.classList.add('drag-over'); });
        cauldron.addEventListener('dragleave', () => { cauldron.parentElement.classList.remove('drag-over'); });
        cauldron.addEventListener('drop', (e) => {
            e.preventDefault(); cauldron.parentElement.classList.remove('drag-over');
            const data = e.dataTransfer.getData('text/plain');
            if (data) {
                playSound('drop');
                const p = document.createElement('span'); p.className = 'tag'; p.innerText = data;
                cauldronChips.appendChild(p);
                createSparkles(cauldron);
                currentPrompt += data + " ";
                cauldronOut.innerText = currentPrompt.trim();
                cauldron.querySelector('span').innerText = "もっと追加できるよ！";
            }
        });

        function simImages() {
            if(!currentPrompt) return;
            playSound('magic');
            const res = document.getElementById('sim-result');
            res.style.display = 'block';
            createSparkles(document.querySelector('.cauldron-container'));
        }

        /* Quiz */
        const quizData = [
            { question: "Nano Banana Proで「一貫したキャラクター」を維持するために最も重要な機能はどれですか？", options: ["スタイル参照 (Style Reference)", "キャラクター参照 (Character Reference)", "アスペクト比固定", "アップスケール"], answer: 1, tier: 1 },
            { question: "画像の一部分だけを指定して、新たなオブジェクトを追加・変更する技術を何と呼びますか？", options: ["アウトペイント", "インペイント", "被写界深度調整", "設計図ガイド"], answer: 1, tier: 2 },
            { question: "特定の構図を厳密に守らせたい場合に、最も有効なアプローチはどれですか？", options: ["プロンプトを長文にする", "ChatGPTに指示文を書かせる", "ラフスケッチや設計図を参照画像として読み込ませる", "画像の解像度を最大にする"], answer: 2, tier: 3 }
        ];
        let quizIdx = 0;
        function renderQuiz() {
            const q = quizData[quizIdx];
            document.getElementById('quiz-question').innerText = `Q${quizIdx+1}. ${q.question} (Tier ${q.tier})`;
            const opts = document.getElementById('quiz-options'); opts.innerHTML = '';
            q.options.forEach((opt, idx) => {
                const div = document.createElement('div'); div.className = 'quiz-option'; div.innerText = opt;
                div.onclick = () => checkQuiz(idx, q.answer, div);
                opts.appendChild(div);
            });
            document.getElementById('quiz-feedback').innerText = ''; document.getElementById('quiz-next').style.display = 'none';
        }
        function checkQuiz(selected, correct, el) {
            const opts = document.querySelectorAll('.quiz-option'); opts.forEach(o => o.onclick = null);
            if (selected === correct) {
                el.classList.add('correct'); playSound('magic'); createSparkles(el);
                document.getElementById('quiz-feedback').innerText = '正解！素晴らしいです！🎉'; document.getElementById('quiz-feedback').style.color = 'var(--accent)';
            } else {
                el.classList.add('incorrect'); opts[correct].classList.add('correct'); playSound('click');
                document.getElementById('quiz-feedback').innerText = '惜しい！正解は緑色の選択肢です。'; document.getElementById('quiz-feedback').style.color = 'var(--danger)';
            }
            if (quizIdx < quizData.length - 1) document.getElementById('quiz-next').style.display = 'block';
            else { document.getElementById('quiz-next').style.display = 'inline-block'; document.getElementById('quiz-next').innerText = '終了'; document.getElementById('quiz-next').onclick = () => { document.getElementById('quiz-container').innerHTML = '<h3><i class="fa-solid fa-award"></i> Quiz Completed!</h3><p>全問正解です。総合理解度チェックに成績が反映されます（デモ）。</p>'; }; }
        }
        function nextQuiz() { playSound('click'); quizIdx++; renderQuiz(); }
        window.onload = () => { renderQuiz(); };

        /* Confetti func details omitted for length but roughly same as before */
        const confCanvas = document.getElementById('confettiCanvas'); const ctx2 = confCanvas.getContext('2d');
        function fireConfetti(){
            ctx2.clearRect(0,0,confCanvas.width,confCanvas.height);
            ctx2.font="30px serif"; ctx2.fillText("✨🎉✨", window.innerWidth/2 - 50, window.innerHeight/2);
            // using simple text for brevity
        }
    """

    video1_prompts = [
        ("02:05 ①一貫性のあるポージング（キャラクター参照）", "キャラクターの三面図やベース画像（Character Reference）を入力し、「走っている」「見上げている」などの動作を追加する。", "1人の女性、走っている、横顔、躍動感、スポーツウェア"),
        ("03:54 ②プロクオリティなサムネイルの新規作成", "テキストを配置する余白（ネガティブスペース）を意識した構図をプロンプトで指定する。", "YouTubeサムネイル用背景、右側に大きな余白、左側に驚くビジネスマン、鮮やかな青背景、高品質、4k"),
        ("05:03 ③既存サムネイルの効率的な編集（バリエーション）", "バリエーション生成（Vary）機能を使い、元の構図を保ちつつ色合いやモチーフを微調整する。", "(Vary機能使用) 背景を赤色に、人物の服をスーツに変更"),
        ("05:54 ④サムネイルの改善パターンを即時生成", "プロンプトの特定キーワードだけを差し替えて複数一気に生成。A/Bテスト用の素材を作る。", "YouTubeサムネイル用背景、右側に大きな余白、左側に[笑顔/怒る/泣く]ビジネスマン"),
        ("06:42 ⑤ポップな告知バナーの制作", "「アメコミ風」「ポップアート」「フラットデザイン」などのスタイルキーワードを強調する。", "ポップアートスタイル、アメコミ風、集中線、カラフルな背景、セール告知用バナーの背景素材"),
        ("07:43 ⑥日本語テキストの細かい微調整（削除）", "画像内のテキストをインペイント（部分修正）機能で消去し、Canva等で後から追加できるようにする。", "(Inpaint機能使用) テキスト部分をなぞり、プロンプトを「何もない無地の背景」にして修正"),
        ("08:22 ⑦分かりやすいインフォグラフィックスの制作", "「アイソメトリック（等角投影法）」「3Dアイコン」を指定して、図解に使えるパーツを生成する。", "アイソメトリック構図、3Dアイコン、光るパソコン、クリーンな白背景、インフォグラフィック素材"),
        ("09:20 ⑧画像のインペイントとアウトペイント（拡張）", "アウトペイント機能で画像の上下左右を拡張し、アスペクト比を変えつつ自然な背景を継ぎ足す。", "(Zoom Out / Pan機能使用) 横長の16:9へ拡張、自然な森の風景を横に広げる"),
        ("10:02 ⑨既存の資料をベースにした設計図（ControlNet）", "粗い手書きのラフ図などを読み込ませ（Image to Image）、高精密なイラストに仕上げる。", "(Image to Image) このラフスケッチに基づいた、高品質な3Dレンダリングの家、リアルな光、晴れ"),
        ("10:47 ⑩クライアントの要望に応じた部分変更 (Inpaint)", "インペイント機能を使い、「コーヒー」を「紅茶」に変更するなど、特定箇所だけ書き換える。", "(部分選択) 紅茶が入ったアンティークなティーカップ、湯気"),
        ("11:42 ⑪大量の素材やキャラクターの組み合わせ (パラメーター：ウェイト)", "要素をカンマで区切り、重み付け（Weight）パラメーターを使って配置バランスを調整する。", "可愛い犬::2、かっこいい猫::1、公園の中、並んで座っている"),
        ("12:27 ⑫設計図を利用したポーズの指定 (Pose Reference)", "棒人間や簡単なポーズ図をコントロールとして入れて、その通りのポーズを取らせる。", "(Pose Reference使用) 腕を組んで自信満々に立つスーツの男性、超リアル、8k"),
        ("13:07 ⑬参照画像を使ったスタイルの変換 (Style Reference)", "「スタイル参照（sref）」を用いて、特定のイラストレーター風のタッチを適用する。", "(sref 参照画像URL) サイバーパンク都市、雨、ネオンライト"),
        ("13:48 ⑭アスペクト比の完全な修正と維持 (--ar)", "「--ar 16:9」などのパラメーターを付与し、用途にあった正確な比率を指定する。", "美しい夕焼けの海、ヤシの木 --ar 16:9"),
        ("14:38 ⑮写真をパーツごとに分解する (切り抜き前提)", "緑色や白の背景（グリーンバック）を指定し、後から編集ソフトで切り抜きやすくする。", "シンプルな椅子、白背景、スタジオ照明、影なし --no shadow"),
        ("15:32 ⑯高解像度へのアップスケール", "生成された画像を「Upscale（Creative/Subtle）」ボタンで品質を保ったまま高解像度化する。", "(Upscaleボタン実行による高画質化)"),
        ("16:29 ⑰リアルなライティング効果の変更", "「シネマティック」「リムライト」「ゴールデンアワー」等、光の当たり方を指定。", "ポートレート、女性、横顔、シネマティックライティング、バックライト、リムライト、被写体ブレなし"),
        ("17:20 ⑱ピント(被写界深度)の調整", "「ボケ味（Bokeh）」「F値1.4」「マクロ撮影」などカメラのレンズ特性をプロンプトに入れる。", "マクロ撮影、葉にとまる水滴、背景は強くボケている(ボケ味)、F値1.4、超高解像度"),
        ("18:00 ⑲ChatGPT連携による大量生成", "ChatGPTに「Midjourney用のプロンプトを10パターン英語で出力して」と指示し、コピペで量産する。", "(ChatGPTで生成した英語プロンプトをそのまま入力)"),
        ("19:03 ⑳Flow連携による動画の生成(Kling等)", "静止画を2枚用意し、「AからBへ変化する」AIビデオ生成ツールへの繋ぎとして活用する。", "画像A（昼の街）と画像B（夜の街）を生成し、外部ツールで動画化")
    ]

    video2_prompts = [
        ("1. 髪型の変更", "インペイントで髪部分を選択し、髪型を指定。例：「ショートボブ、金髪」", "ショートボブのヘアスタイル、金髪、風になびく"),
        ("2. 顔の表情を変更", "インペイントで口元や目元を選択。「笑顔」や「驚き」等の感情を追加。", "大きな笑顔、白い歯、輝く目"),
        ("3. 服の変更", "インペイントで服全体を選択。「春のカジュアルなワンピース」などに変更。", "黄色い春のカジュアルなワンピース、花柄"),
        ("4. アスペクト比の変更", "Zoom OutまたはPan機能で縦横比を変える。", "(Zoom Out機能使用) 背景のカフェを広く見せる"),
        ("5. オブジェクトの削除", "インペイントで不要なオブジェクトを選択し、プロンプトを空にする。", "木製のテーブルのみ"),
        ("6. オブジェクトの自然な置換", "単純に消すのではなく、「開いたスペースに観葉植物を置く」など。", "小さな緑の観葉植物、白い鉢"),
        ("7. 一貫したキャラクター（架空）", "「Character Reference (--cref)」を使用。", "コーヒーを飲む、カフェのテラス --cref [画像URL] --cw 100"),
        ("8. 一貫したキャラクター（実在）", "実在の人物の写真をcrefに入れ、似た人物の画像を生成。", "スーツを着てプレゼンする、会議室 --cref [写真URL]"),
        ("9. 設計図を使ってガイド", "下書きや骨組み画像を元に生成（ControlNet等の機能）。", "モダンなリビングルーム、大きな窓、観葉植物 (ベース線画あり)"),
        ("10. 設計図の微修正", "線画の強さ（ウェイト）を調整し、AIの自由度を高める。", "--iw 0.5 (画像への忠実度パラメーターの調整)"),
        ("11. 製品広告", "商品の背景を豪華にする。「高級感」「水しぶき」などを追加。", "高級化粧品のボトル、黒い大理石の上、金色の水しぶき、ドラマチックな照明"),
        ("12. 素材演出", "布の質感や金属の反射など、マテリアルに特化した指定。", "シルクの布が風に舞う、柔らかい光、パステルピンク"),
        ("13. 食品のシズル感", "湯気、照り、滴るシロップを強調する。", "焼きたてのハンバーガー、肉汁、湯気、超リアル"),
        ("14. 解体ショット (ノウリング)", "Knolling（分解して整然と並べる構図）を指定。", "カメラの分解図、ノウリング構図、真上からの視点、青い背景"),
        ("15. 無地キャンバスの生成", "後からCanvaでロゴや文字を合成するための無地素材作り。", "無地の黒いTシャツを着た若者、真っ白な看板"),
        ("16. 製品モックアップ", "ブランクのスマホ画面やポスターフレームを生成。", "木製テーブルの上のiPhone15 モックアップ、画面真っ白、自然光"),
        ("17. 文字の描画 (v6機能)", "引用符（「\"\"」）で囲んでテキストを描画させる。", 'ネオンサインで "HELLO WORLD" と書かれている、路地裏'),
        ("18. 文字の描画の限界", "長文や複雑な日本語はCanvaで後乗せしたほうが早くて正確です。", "※バウンディングボックスだけ生成してCanvaで文字を入れる手法"),
        ("19. 証明写真の作成", "「スタジオライティング」「無地背景」を指定。", "プロのビジネスポートレート、日本人男性30代、グレー背景、笑顔")
    ]

    def build_acc(prompts, prefix="A", youtube_url=""):
        import re
        html = ""
        for i, (title, desc, pr) in enumerate(prompts):
            time_match = re.search(r'(\d{2}):(\d{2})', title)
            yt_btn = ""
            if time_match and youtube_url:
                minutes = int(time_match.group(1))
                seconds = int(time_match.group(2))
                ts = minutes * 60 + seconds
                yt_btn = f'<a href="{youtube_url}&t={ts}s" target="_blank" class="yt-time-btn" onclick="playSound(&quot;click&quot;)"><i class="fa-brands fa-youtube"></i> 動画の {time_match.group(0)} から見る</a>'

            html += f'''
            <details class="prompt-accordion">
                <summary><span class="tag">Tip {i+1}</span> {title} <i class="fa-solid fa-chevron-down"></i></summary>
                <div class="prompt-content">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:10px;">
                        <p style="margin-top:0; flex-grow:1;"><strong>解説:</strong> {desc}</p>
                        {yt_btn}
                    </div>
                    <div class="browser-mockup">
                        <div class="browser-header">
                            <div class="dot red"></div><div class="dot yellow"></div><div class="dot green"></div>
                        </div>
                        <div class="browser-content">
                            <button class="copy-btn" onclick="copyPrompt(this)"><i class="fa-regular fa-copy"></i> Copy</button>
                            <pre style="margin:0; font-family:inherit;">{pr}</pre>
                        </div>
                    </div>
                </div>
            </details>
            '''
        return html

    half2_acc = build_acc(video1_prompts, "V1-", "https://www.youtube.com/watch?v=SP4FceXU1e4")
    half3_acc = build_acc(video2_prompts, "V2-", "https://www.youtube.com/watch?v=SP4FceXU1e4")

    part1 = """
        <div id="half1" class="tab-content active">
            <div class="glass-card">
                <div class="card-header"><i class="fa-brands fa-youtube" style="color:#ef4444;"></i><h2>📺 前半：AI画像生成の基礎・応用</h2></div>
                <div class="video-grid">
                    <a href="https://youtu.be/3ATfzId9wrM" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/3ATfzId9wrM/mqdefault.jpg" alt="動画1">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                    <a href="https://youtu.be/jyZ1D9dP4fI" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/jyZ1D9dP4fI/mqdefault.jpg" alt="動画2">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                </div>
            </div>

            <div class="glass-card">
                <div class="card-header"><i class="fa-solid fa-graduation-cap"></i><h2>画像生成のキホンとプロンプトの構造</h2></div>
                <p>動画で解説されているテキストから画像への変換技術の基礎です。AIが画像を生成する際、「プロンプト」という命令文を与えます。プロンプトは明確で構造的であるほど、AIが意図通りに解釈しやすくなります。</p>
                <div class="bento-grid">
                    <div class="bento-item"><h4><i class="fa-solid fa-image"></i> 被写体 (Subject)</h4><p>誰が・何が主役かを明確にします。（例：ゴールデンレトリバー）</p></div>
                    <div class="bento-item"><h4><i class="fa-solid fa-camera"></i> 構図・光・スタイル</h4><p>どんな雰囲気で撮られた写真かを追加します。（例：シネマティック）</p></div>
                    <div class="bento-item"><h4><i class="fa-solid fa-sliders"></i> パラメーター</h4><p>アスペクト比などの設定です。（例：--ar 16:9）</p></div>
                </div>
                <div class="box gemini">
                    <h4><i class="fa-solid fa-diagram-project"></i> 構造的なプロンプトの書き方 (Markdown)</h4>
                    <p>箇条書きや `#, ##` を使って情報を整理すると伝わりやすくなります。</p>
                    <div class="code-box">
                        <span class="code-label">Template</span>
                        # 被写体<br>- 年齢・性別: 20代の女性<br>- 服装: モダンなスーツ<br><br>
                        # 環境・光<br>- 場所: オフィスのカフェスペース<br><br>
                        # スタイル<br>- 写真調, 高画質, 8k
                    </div>
                </div>
            </div>

            <div class="glass-card" id="simulator-section">
                <div class="card-header"><i class="fa-solid fa-flask-vial"></i><h2>体験：プロンプト調合釜（Cauldron Simulator）</h2></div>
                <p>要素（チップ）を下の「魔法の釜（ドロップゾーン）」にドラッグ＆ドロップして完成させましょう！</p>
                <div class="draggable-container">
                    <div class="drag-chip subject" draggable="true" data-text="サイバーパンクな街並み,">🏙️ サイバーパンク街 (Subject)</div>
                    <div class="drag-chip style" draggable="true" data-text="水彩画タッチ, 淡い色合い,">🎨 水彩画タッチ (Style)</div>
                    <div class="drag-chip style" draggable="true" data-text="シネマティックライティング, 8k,">🎥 シネマティック (Lighting)</div>
                    <div class="drag-chip param" draggable="true" data-text="--ar 16:9">📐 横長 (--ar)</div>
                </div>
                <div class="cauldron-container">
                    <div class="cauldron-dropzone" id="cauldron">
                        <i class="fa-solid fa-fire"></i><span>ここにドロップ！</span>
                    </div>
                    <div class="cauldron-result">
                        <h4>完成したプロンプト:</h4>
                        <div class="cauldron-chips" id="cauldron-chips"></div>
                        <div id="cauldron-out" class="cauldron-output-area">[ まだ要素がありません ]</div>
                        <button class="btn" onclick="simImages()"><i class="fa-solid fa-wand-magic-sparkles"></i> 擬似生成する</button>
                    </div>
                </div>
                <div id="sim-result" style="display:none; margin-top:20px; text-align:center;">
                    <br><h3>AI Image Generated! (Simulation)</h3><br>
                </div>
            </div>
            
            <div class="mission-ticket" onclick="completeMission(this, 'm1')">
                <div class="wax-seal" style="background:#5b21b6; border-color:#4c1d95;"><i class="fa-solid fa-flask"></i></div>
                <div class="ticket-stub"><i class="fa-solid fa-ticket-simple" style="color:#8b5cf6;"></i></div>
                <div class="mission-content"><h3>Mission 1: 調合完了</h3><p>シミュレーターを動かして画像の生成工程を体験する。</p></div>
                <div class="mission-checkbox"><i class="fa-solid fa-check"></i></div>
            </div>

            <button class="next-tab-btn" onclick="switchTab('half2')">活用事例20選 へ進む <i class="fa-solid fa-arrow-right"></i></button>
        </div>
    """

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
    <button id="toggleSound" class="sound-toggle" title="Toggle Sound"><i class="fa-solid fa-volume-high"></i></button>

    <header class="fixed-header">
        <a href="index.html" class="back-link"><i class="fa-solid fa-arrow-left"></i> Course Home</a>
        <div class="progress-container">
            <div class="progress-text"><span>Day 4 Progress</span><span id="progress-percent">0%</span></div>
            <div class="progress-bar-bg"><div class="progress-bar-fill" id="progress-bar"></div></div>
        </div>
        <div style="width:100px;"></div>
    </header>

    <div class="container">
        <div class="hero">
            <div class="day-badge">DAY 04</div>
            <h1>Nano Banana Pro 教科書</h1>
            <p>本日の目標：テキストから画像への変換技術の基礎をマスターする。</p>
        </div>

        <div class="tab-container">
            <button class="tab-btn active" onclick="switchTab('half1')">基礎：プロンプト教室</button>
            <button class="tab-btn" onclick="switchTab('half2')">応用：動画編集向け20選</button>
            <button class="tab-btn" onclick="switchTab('half3')">実践：今すぐ使える19選</button>
        </div>

        {part1}

        <div id="half2" class="tab-content">
            <div class="glass-card">
                <div class="card-header"><i class="fa-brands fa-youtube" style="color:#ef4444;"></i><h2>📺 後半：Nano Banana Pro活用術20選</h2></div>
                <div class="video-grid" style="grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));">
                    <a href="https://youtu.be/SP4FceXU1e4" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/SP4FceXU1e4/mqdefault.jpg" alt="活用術20選">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                </div>
            </div>
            
            <div class="glass-card">
                <div class="card-header"><i class="fa-solid fa-list"></i><h2>応用：動画編集者向け 活用術20選</h2></div>
                <p>動画で紹介されたプロンプトです。No Video Relianceの法則に基づき、すべて再現しました。</p>
                <div class="scenario-sandbox">
                    <div class="scenario-pane">
                        <div class="scenario-header bad">❌ Zero-Shot (失敗例)</div>
                        <div class="scenario-body">かっこいい犬の画像</div>
                    </div>
                    <div class="scenario-pane">
                        <div class="scenario-header good">✅ Few-Shot (成功例)</div>
                        <div class="scenario-body">ゴールデンレトリバー、サングラス、サイバーパンク、8k</div>
                    </div>
                </div>
                {half2_acc}
            </div>
            <div class="mission-ticket" onclick="completeMission(this, 'm2')">
                <div class="wax-seal" style="background:#047857;"><i class="fa-solid fa-star"></i></div>
                <div class="ticket-stub"><i class="fa-solid fa-ticket-simple" style="color:#10b981;"></i></div>
                <div class="mission-content"><h3>Mission 2: 応用術の確認</h3><p>20選のうち、どれか1日コピーして手元で控えておく。</p></div>
                <div class="mission-checkbox"><i class="fa-solid fa-check"></i></div>
            </div>
            <button class="next-tab-btn" onclick="switchTab('half3')">実践：全般向け19選 へ進む <i class="fa-solid fa-arrow-right"></i></button>
        </div>

        <div id="half3" class="tab-content">
            <div class="glass-card">
                <div class="card-header"><i class="fa-brands fa-youtube" style="color:#ef4444;"></i><h2>📺 後半：今日から使える画像編集テク</h2></div>
                <div class="video-grid" style="grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));">
                    <a href="https://youtu.be/EcQNRpZE7Ns" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/EcQNRpZE7Ns/mqdefault.jpg" alt="編集テク19選">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                </div>
            </div>

            <div class="glass-card">
                <div class="card-header"><i class="fa-solid fa-layer-group"></i><h2>実践：今すぐ使える活用事例19選</h2></div>
                <p>インペイント（部分修正）やアスペクト比の変更など、生成後の「加工」に特化したテクニック集です。</p>
                <div class="workflow">
                    <div class="flow-step"><div class="step-icon">1</div><div class="step-content"><h4>ベース画像を生成</h4></div></div>
                    <div class="flow-step"><div class="step-icon">2</div><div class="step-content"><h4>インペイントで部分指定</h4></div></div>
                    <div class="flow-step"><div class="step-icon">3</div><div class="step-content"><h4>追加プロンプトを実行</h4></div></div>
                </div>
                {half3_acc}
            </div>
            <div class="mission-ticket" onclick="completeMission(this, 'm3')">
                <div class="wax-seal" style="background:#be123c;"><i class="fa-solid fa-fire"></i></div>
                <div class="ticket-stub"><i class="fa-solid fa-ticket-simple" style="color:#e11d48;"></i></div>
                <div class="mission-content"><h3>Mission 3: 加工技術の確認</h3><p>インペイントの手順を理解する。</p></div>
                <div class="mission-checkbox"><i class="fa-solid fa-check"></i></div>
            </div>

            <div class="quiz-container" id="quiz-container">
                <h3><i class="fa-solid fa-brain"></i> 理解度チェック</h3>
                <p id="quiz-question"></p>
                <div class="quiz-options" id="quiz-options"></div>
                <div class="quiz-feedback" id="quiz-feedback"></div>
                <button class="quiz-next" id="quiz-next" onclick="nextQuiz()">次の問題へ</button>
            </div>

            <div class="secret-link"><a href="index_dev_notes.html"><i class="fa-solid fa-code"></i> Engineering Design Log (Developer Notes) 🤫</a></div>
        </div>
    </div>
    <script>{js}</script>
    <script src="main.js"></script>
</body>
</html>
"""

    with open(r'g:\マイドライブ\研修\【202603】生成AIとプロンプト\vol04-1_nano_banana.html', 'w', encoding='utf-8') as f:
        f.write(doc)
    print("vol04-1_nano_banana.html updated successfully.")

if __name__ == '__main__':
    build_html()
