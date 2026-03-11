# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import os

html_content = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day 4 | Nano Banana Pro & Image Generation</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Noto+Sans+JP:wght@400;500;700&family=Teko:wght@500;600;700&family=Fira+Code&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --bg-body: #f8fafc;
            --bg-card: rgba(255, 255, 255, 0.95);
            --text-main: #0f172a;
            --text-sub: #475569;
            --accent: #10b981;
            --accent-light: #34d399;
            --accent-bg: #ecfdf5;
            --accent-glow: rgba(16, 185, 129, 0.25);
            --clickable: #0ea5e9;
            --clickable-bg: #e0f2fe;
            --danger: #ef4444;
            --glass-blur: blur(16px);
            --radius: 20px;
        }

        * { box-sizing: border-box; }
        html { scroll-behavior: smooth; }

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

        /* Fixed Header */
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

        /* Main Container */
        .container { max-width: 1100px; margin: 100px auto 80px; padding: 0 24px; }

        /* Hero */
        .hero { text-align: center; margin-bottom: 3rem; animation: fadeInDown 0.8s ease; }
        .day-badge { background: var(--accent); color: #fff; padding: 0.4rem 1.7rem; border-radius: 30px; font-family: 'Teko', sans-serif; font-size: 1.6rem; letter-spacing: 2px; display: inline-block; margin-bottom: 1.2rem; }
        .hero h1 { font-size: clamp(2.2rem, 5vw, 3.8rem); margin: 0 0 1rem; font-weight: 900; letter-spacing: -1px; }
        .hero p { color: var(--text-sub); font-size: 1.15rem; max-width: 800px; margin: 0 auto; line-height: 1.8; }

        /* Custom Tabs */
        .tab-nav { display: flex; justify-content: center; gap: 1rem; margin-bottom: 3rem; flex-wrap: wrap; }
        .tab-btn { background: #fff; border: 2px solid #e2e8f0; color: var(--text-sub); padding: 1.2rem 2.2rem; border-radius: 40px; cursor: pointer; font-weight: 800; font-size: 1.05rem; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); display:flex; align-items:center; gap:8px;}
        .tab-btn:hover { border-color: var(--accent-light); color: var(--accent); transform: translateY(-2px); box-shadow: 0 10px 20px rgba(0,0,0,0.05);}
        .tab-btn.active { background: var(--accent); color: #fff; border-color: var(--accent); box-shadow: 0 10px 25px var(--accent-glow); transform: translateY(-3px);}
        
        .tab-content { display: none; animation: fadeIn 0.5s ease; }
        .tab-content.active { display: block; }

        /* Glass Card */
        .glass-card { background: var(--bg-card); backdrop-filter: var(--glass-blur); border: 1px solid rgba(255,255,255,0.7); border-radius: var(--radius); padding: 2.5rem 3rem; margin-bottom: 2.5rem; box-shadow: 0 10px 30px rgba(0,0,0,0.03); transition: transform 0.3s, box-shadow 0.3s; }
        .glass-card:hover { transform: translateY(-2px); box-shadow: 0 15px 40px rgba(0,0,0,0.06); }
        .card-header { display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem; border-bottom: 2px solid #f1f5f9; padding-bottom: 1.2rem; }
        .card-header i { font-size: 1.6rem; color: var(--accent); background: var(--accent-bg); padding: 1.2rem; border-radius: 14px; }
        .card-header h2 { margin: 0; font-size: 1.8rem; color: var(--text-main); font-weight:800; letter-spacing: -0.5px;}

        /* Content Blocks */
        .info-box { background: var(--clickable-bg); border-left: 5px solid var(--clickable); padding: 1.8rem 2rem; border-radius: 0 16px 16px 0; margin: 2rem 0; }
        .info-box h4 { margin: 0 0 0.8rem; color: var(--clickable); display: flex; align-items: center; gap: 0.8rem; font-size: 1.2rem; font-weight: 800;}
        .info-box p { margin: 0; color: var(--text-main); line-height: 1.7; font-size: 1.05rem;}

        /* Video Grid */
        .video-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.8rem; margin: 2rem 0;}
        .video-thumb { position: relative; border-radius: 16px; overflow: hidden; display: block; border: 4px solid #fff; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08); transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); background: #000;}
        .video-thumb:hover { transform: translateY(-8px); box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15); border-color: var(--accent-light);}
        .video-thumb img { width: 100%; display: block; opacity: 0.85; transition: opacity 0.4s, transform 0.6s;}
        .video-thumb:hover img { opacity: 1; transform: scale(1.06);}
        .play-overlay { position: absolute; inset: 0; background: rgba(0, 0, 0, 0.15); display: flex; align-items: center; justify-content: center; transition: all 0.3s;}
        .video-thumb:hover .play-overlay { background: rgba(16, 185, 129, 0.25);}
        .play-overlay i { color: #fff; font-size: 3.5rem; text-shadow: 0 5px 20px rgba(0, 0, 0, 0.5); transition: transform 0.3s;}
        .video-thumb:hover .play-overlay i { transform: scale(1.15);}

        /* ---------------------------------
           BENTO GRID & CUSTOM UI
        --------------------------------- */
        .bento-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; margin: 2.5rem 0;}
        .bento-item { background: #fff; border-radius: 16px; padding: 2rem; position: relative; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.03); border: 1px solid #f1f5f9; transition: transform 0.3s, box-shadow 0.3s;}
        .bento-item:hover { transform: translateY(-5px); box-shadow: 0 12px 25px rgba(0,0,0,0.06); border-color: var(--accent-light);}
        .bento-item h4 { margin: 0 0 1rem; font-size: 1.2rem; color: var(--clickable); display: flex; align-items: center; gap: 0.5rem; font-weight:800;}
        .bento-item p { font-size: 1.05rem; color: #64748b; line-height: 1.6; margin: 0; }

        /* Browser Mockup / Code Box */
        .mockup-container { margin: 2.5rem 0; display: flex; justify-content: center; perspective: 1000px; }
        .browser-mockup { width: 100%; background: #1e293b; border-radius: 12px; overflow: hidden; margin: 1.5rem 0; box-shadow: 0 10px 25px rgba(0,0,0,0.15); border: 1px solid #334155; }
        .browser-header { background: #0f172a; padding: 12px 16px; display: flex; gap: 8px; border-bottom: 1px solid #334155; align-items:center;}
        .browser-dot { width: 12px; height: 12px; border-radius: 50%; }
        .browser-content { padding: 1.5rem; color: #f8fafc; font-family: 'Fira Code', 'Consolas', monospace; font-size: 0.95rem; line-height: 1.7; position: relative; white-space:pre-wrap;}
        
        .code-box { background: #1e293b; color: #e2e8f0; padding: 2.2rem 2.2rem 1.8rem; border-radius: 12px; font-family: 'Fira Code', 'Consolas', monospace; position: relative; font-size: 0.95rem; line-height: 1.8; margin: 2rem 0; border-left: 4px solid var(--accent);}
        .code-label { position: absolute; top: -14px; left: 20px; background: var(--accent); color: #fff; padding: 4px 16px; font-size: 0.85rem; font-weight: 800; border-radius: 8px; font-family:'Noto Sans JP', sans-serif;}
        
        .btn { display: inline-flex; align-items: center; gap: 0.6rem; background: var(--clickable); color: #fff; border: none; padding: 0.8rem 1.8rem; border-radius: 12px; text-decoration: none; font-size: 1.05rem; font-weight: 800; transition: all 0.2s; cursor: pointer; margin-top: 1rem; box-shadow: 0 6px 15px rgba(14, 165, 233, 0.3); }
        .btn:hover { background: #0284c7; transform: translateY(-2px); box-shadow: 0 8px 20px rgba(14, 165, 233, 0.4); }
        .btn-copy { position: absolute; top: 15px; right: 15px; background: rgba(255,255,255,0.1); color: #fff; border: 1px solid rgba(255,255,255,0.2); padding: 6px 14px; border-radius: 8px; cursor: pointer; font-size: 0.85rem; transition: all 0.2s; margin:0;}
        .btn-copy:hover { background: rgba(255,255,255,0.2); transform:none; }

        /* Accordion (Prompt List) */
        .prompt-accordion { margin-bottom: 1.2rem; border: 1px solid #e2e8f0; border-radius: 12px; background: #fff; overflow: hidden; transition: box-shadow 0.3s; }
        .prompt-accordion:hover { box-shadow: 0 8px 15px rgba(0,0,0,0.04); border-color:#cbd5e1;}
        .prompt-accordion summary { padding: 1.2rem 1.5rem; font-weight: 800; font-size: 1.1rem; cursor: pointer; display: flex; align-items: center; gap: 1rem; list-style: none; background: #f8fafc; color:var(--text-main);}
        .prompt-accordion summary::-webkit-details-marker { display: none; }
        .prompt-accordion summary i.fa-chevron-down { color: var(--text-sub); transition: transform 0.3s; margin-left: auto; }
        .prompt-accordion[open] summary i.fa-chevron-down { transform: rotate(180deg); }
        .prompt-accordion[open] summary { border-bottom: 1px solid #e2e8f0; background: #fff; color:var(--clickable);}
        .prompt-content { padding: 1.5rem; animation: slideDown 0.3s ease; }
        .tag { background: var(--clickable-bg); color: var(--clickable); padding: 4px 10px; border-radius: 6px; font-size: 0.8rem; font-weight: 800; margin-right: 5px;}
        .yt-time-btn { display: inline-flex; align-items: center; gap: 6px; background: #fee2e2; color: #b91c1c; padding: 6px 14px; border-radius: 20px; text-decoration: none; font-size: 0.85rem; font-weight: bold; transition: all 0.2s; border: 1px solid #fca5a5; white-space: nowrap; margin-bottom: 10px;}
        .yt-time-btn:hover { background: #fca5a5; color: #7f1d1d; }

        @keyframes slideDown { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }

        /* Workflow */
        .workflow { display: flex; flex-direction:column; gap: 1.5rem; position: relative; margin: 3.5rem 0 3.5rem 2rem; }
        .workflow::before { content: ""; position: absolute; top: 10px; bottom: 10px; left: 24px; width: 4px; background: #e2e8f0; z-index: 0; }
        .flow-step { display: flex; align-items: flex-start; gap: 2rem; position: relative; z-index: 1; }
        .step-icon { width: 52px; height: 52px; background: #fff; border: 4px solid var(--accent); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; color: var(--text-main); font-weight:800; transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1); box-shadow: 0 4px 15px rgba(0,0,0,0.05); flex-shrink:0;}
        .flow-step:hover .step-icon { background: var(--accent); color: #fff; transform: scale(1.15); box-shadow: 0 10px 25px var(--accent-glow); }
        .step-content { background:#fff; border:1px solid #e2e8f0; border-radius:12px; padding:1.5rem; flex-grow:1; box-shadow: 0 4px 10px rgba(0,0,0,0.02);}
        .step-content h4 { font-weight: 800; display: block; margin: 0 0 0.5rem; font-size: 1.1rem; color:var(--text-main);}
        
        /* ---------------------------------
           GAMIFICATION & CHECKLIST
        --------------------------------- */
        .mission-area { margin-top: 3rem; background: #fff; border: 2px dashed #cbd5e1; border-radius: 20px; padding: 2.5rem; position: relative; overflow: hidden; transition: all 0.4s;}
        .mission-area.completed { border-color: var(--accent); border-style: solid; background: var(--accent-bg); box-shadow: 0 10px 40px var(--accent-glow);}
        .mission-header { text-align: center; margin-bottom: 2rem; }
        .mission-header h3 { font-size: 1.6rem; color: var(--text-main); margin:0 0 0.5rem; font-weight:800; display:flex; justify-content:center; align-items:center; gap:10px;}
        .mission-header p { color: var(--text-sub); margin:0; font-size:1.05rem;}

        .task-list { list-style: none; padding: 0; margin: 0; display:flex; flex-direction:column; gap:1rem;}
        .task-item { display: flex; align-items: flex-start; gap: 1.2rem; padding: 1.5rem; border-radius: 16px; background: #f8fafc; border: 1px solid #e2e8f0; transition: all 0.3s; cursor: pointer; position: relative; z-index: 2;}
        .task-item:hover { border-color: var(--accent-light); background: #fff; box-shadow: 0 8px 20px rgba(0,0,0,0.04); transform: translateX(5px);}
        .task-item.completed { background: #d1fae5; border-color: #6ee7b7; }
        
        .custom-checkbox { width: 32px; height: 32px; border: 3px solid #cbd5e1; border-radius: 10px; display: flex; align-items: center; justify-content: center; transition: all 0.3s; flex-shrink: 0; margin-top: 2px; background: #fff; }
        .task-item.completed .custom-checkbox { background: var(--accent); border-color: var(--accent); }
        .custom-checkbox i { color: #fff; font-size: 16px; opacity: 0; transform: scale(0.5); transition: all 0.3s; }
        .task-item.completed .custom-checkbox i { opacity: 1; transform: scale(1); }
        
        .task-content { flex: 1; }
        .task-content h4 { margin: 0 0 0.5rem; font-size: 1.2rem; color: var(--text-main); font-weight:800; transition:color 0.3s;}
        .task-item.completed .task-content h4 { color: #059669; }
        .task-content p { margin: 0; font-size: 1rem; color: var(--text-sub); line-height: 1.6; }

        .wax-seal { position: absolute; top: -20px; right: -20px; width: 140px; height: 140px; background: radial-gradient(circle at 30% 30%, #fca5a5, #ef4444, #991b1b); border-radius: 50%; opacity: 0; transform: scale(3) rotate(-30deg); pointer-events: none; display: flex; align-items: center; justify-content: center; color: rgba(255,255,255,0.9); font-size: 3.5rem; box-shadow: inset 0 0 20px rgba(0,0,0,0.5), 0 10px 30px rgba(0,0,0,0.4); border: 4px solid #b91c1c; z-index: 10;}
        .wax-seal::after { content: ''; position: absolute; inset: 10px; border: 2px dotted rgba(255,255,255,0.4); border-radius: 50%; }
        .mission-area.completed .wax-seal { animation: stampIn 0.7s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards; }
        
        @keyframes stampIn { 
            0% { opacity: 0; transform: scale(3) translateY(-50px) rotate(-30deg); } 
            60% { opacity: 1; transform: scale(0.9) translateY(0) rotate(5deg); } 
            80% { transform: scale(1.1) rotate(-2deg); } 
            100% { opacity: 1; transform: scale(1) rotate(0deg); } 
        }

        #confetti, #particles { position: fixed; inset: 0; pointer-events: none; z-index: 9998; }
        @keyframes fadeInDown { from { opacity: 0; transform: translateY(-30px); } to { opacity: 1; transform: translateY(0); } }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(15px); } to { opacity: 1; transform: translateY(0); } }

        .home-btn { position: fixed; bottom: 30px; right: 30px; background: linear-gradient(135deg, var(--accent), #059669); color: white; width: 65px; height: 65px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.6rem; box-shadow: 0 10px 30px rgba(16, 185, 129, 0.4); text-decoration: none; transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); z-index: 1000; }
        .home-btn:hover { transform: translateY(-8px) scale(1.05); box-shadow: 0 15px 40px rgba(16, 185, 129, 0.6); color: white; }

        /* Cauldron Feature */
        .cauldron-container { display: flex; gap: 2rem; margin: 3rem 0; background: #fff; padding: 2.5rem; border-radius: 20px; border: 2px dashed #cbd5e1; transition:all 0.3s;}
        .cauldron-container.drag-over { border-color: var(--accent); background: var(--accent-bg); }
        .cauldron-ingredients { flex: 1; display: flex; flex-wrap:wrap; gap: 1rem; align-content:flex-start;}
        .drag-chip { padding: 10px 20px; border-radius: 30px; cursor: grab; font-weight: 800; font-size: 1rem; color: #fff; transition: transform 0.2s, box-shadow 0.2s; user-select: none; box-shadow: 0 4px 10px rgba(0,0,0,0.1); border:none;}
        .drag-chip:active { cursor: grabbing; transform: scale(0.95); }
        .drag-chip.used { opacity:0.5; pointer-events:none; filter:grayscale(1);}
        .chip-sub { background: linear-gradient(135deg, #f59e0b, #d97706); }
        .chip-style { background: linear-gradient(135deg, #ec4899, #be185d); }
        .chip-param { background: linear-gradient(135deg, #8b5cf6, #6d28d9); }

        .cauldron-pot-area { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative; min-height:200px;}
        .cauldron-dropzone { color:#94a3b8; text-align:center; font-weight:800; font-size:1.2rem;}
        .cauldron-dropzone i { font-size: 3rem; margin-bottom:10px; display:block;}
        
        .cauldron-result { margin-top: 1.5rem; width: 100%; display: none; animation: fadeIn 0.5s; padding:2rem;}
        .cauldron-out-chips { display:flex; flex-wrap:wrap; gap:8px; margin-bottom:15px;}
        .cauldron-out-chips .drag-chip { cursor:default; box-shadow:none; padding: 6px 14px; font-size:0.9rem;}

    </style>
</head>
<body>

    <canvas id="particles"></canvas>
    <canvas id="confetti"></canvas>

    <!-- Header -->
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
            <h1>Nano Banana Pro 教科書</h1>
            <p>本日の目標：テキストから画像への変換技術の基礎をマスターする。<br>プロンプトによる画像生成のキホンから、実務で使える高度な編集テクニックまでを網羅します。</p>
        </div>

        <!-- Premium Tab Navigation -->
        <div class="tab-nav">
            <button class="tab-btn active" onclick="switchTab('tab-goal')"><i class="fa-solid fa-bullseye" style="color:#f59e0b;"></i> コース目標</button>
            <button class="tab-btn" onclick="switchTab('tab-first')"><i class="fa-solid fa-image" style="color:#10b981;"></i> 前半：画像の基礎・応用</button>
            <button class="tab-btn" onclick="switchTab('tab-second')"><i class="fa-solid fa-layer-group" style="color:#0ea5e9;"></i> 後半：実践・活用テク</button>
            <button class="tab-btn" onclick="switchTab('tab-summary')"><i class="fa-solid fa-flag-checkered" style="color:#8b5cf6;"></i> 今日のまとめ</button>
        </div>

        <!-- ==========================================
             TAB 1: COURSE GOALS
        ========================================== -->
        <div id="tab-goal" class="tab-content active">
            <div class="glass-card" style="border-top: 5px solid #f59e0b;">
                <div class="card-header"><i class="fa-solid fa-compass" style="color:#f59e0b; background:#fffbeb;"></i><h2>本日の研修ねらい</h2></div>
                <div class="info-box" style="border-left-color: #f59e0b; background: #fffbeb;">
                    <h4 style="color:#b45309;"><i class="fa-solid fa-wand-magic-sparkles"></i> 思い通りのビジュアルを生み出す力</h4>
                    <p style="color:#92400e;">
                        本日は「画像生成AI」の基礎と実践的な活用方法を学びます。<br><br>
                        テキストから画像を生成する際の「プロンプトの型」を理解し、さらに生成された画像を思い通りに「加工・修正」するテクニックを習得します。動画編集やデザイン実務において、もはや他人の素材を探す時間は不要になります。自分の頭の中のビジュアルを最速で具現化できる人材になりましょう！
                    </p>
                </div>
            </div>
            <div style="text-align:center; margin-top:3rem;">
                <button class="btn" style="padding: 1rem 3rem; font-size:1.2rem; border-radius:30px; background:#f59e0b;" onclick="switchTab('tab-first'); window.scrollTo(0,0);">
                    前半の実習へ進む <i class="fa-solid fa-arrow-right"></i>
                </button>
            </div>
        </div>

        <!-- ==========================================
             TAB 2: FIRST HALF
        ========================================== -->
        <div id="tab-first" class="tab-content">
            <div class="glass-card" style="border-top: 5px solid #10b981;">
                <div class="card-header"><i class="fa-brands fa-youtube" style="color:#ef4444; background:#fef2f2;"></i><h2>前半：AI画像生成の基礎・応用</h2></div>
                <p style="font-size:1.1rem; margin-bottom:1.5rem;">画像生成の基本構造（被写体・構図・パラメーター）を理解しましょう。</p>
                
                <div class="video-grid">
                    <a href="https://youtu.be/3ATfzId9wrM" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/3ATfzId9wrM/hqdefault.jpg" alt="動画1">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                    <a href="https://youtu.be/jyZ1D9dP4fI" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/jyZ1D9dP4fI/hqdefault.jpg" alt="動画2">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                </div>

                <div class="highlight-box">
                    <h3><i class="fa-solid fa-book-open"></i> 読むだけでわかる！完全解説ダイジェスト</h3>
                    <p style="margin-bottom:0; line-height:1.7;">画像生成の更なる深掘りとして、MidjourneyやNanoBananaなどの最新ツールの実践比較です。</p>
                </div>
                <div class="bento-grid">
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-camera-retro" style="color:#0ea5e9;"></i> 1. Midjourneyの実力</h4>
                        <p>写真と見紛うレベルの写実性や、絵画のような表現力において他を圧倒しています。英語プロンプトのコツ（--ar, --v などのパラメータ）を学ぶ必要があります。</p>
                    </div>
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-people-group" style="color:#f59e0b;"></i> 2. 国産AIの強み</h4>
                        <p>海外製AIでは再現が難しい「日本らしい風景」や「自然な日本人の顔」を生成する際は、国内向けに調整されたNanoBanana等が最適です。</p>
                    </div>
                </div>


                <div class="bento-grid">
                    <div class="bento-item" style="border-top:4px solid #f59e0b;">
                        <h4><i class="fa-solid fa-image" style="color:#f59e0b;"></i> 被写体 (Subject)</h4>
                        <p>誰が・何が主役かを明確にします。年齢、性別、服装など。（例：ゴールデンレトリバー）</p>
                    </div>
                    <div class="bento-item" style="border-top:4px solid #ec4899;">
                        <h4><i class="fa-solid fa-camera" style="color:#ec4899;"></i> 構図・光・スタイル</h4>
                        <p>どんな雰囲気で撮られた写真かを追加します。（例：シネマティック、水彩画）</p>
                    </div>
                    <div class="bento-item" style="border-top:4px solid #8b5cf6;">
                        <h4><i class="fa-solid fa-sliders" style="color:#8b5cf6;"></i> パラメーター</h4>
                        <p>アスペクト比などのシステム設定です。（例：--ar 16:9）</p>
                    </div>
                </div>

                <div class="code-box">
                    <span class="code-label">Markdown プロンプト例</span>
                    # 被写体<br>- 年齢・性別: 20代の女性<br>- 服装: モダンなスーツ<br><br>
                    # 環境・光<br>- 場所: オフィスのカフェスペース<br><br>
                    # スタイル<br>- 写真調, 高画質, 8k
                    <button class="btn-copy" onclick="copyCode('prompt-ex1', this)"><i class="fa-regular fa-copy"></i> Copy</button>
                    <div id="prompt-ex1" style="display:none;"># 被写体\n- 年齢・性別: 20代の女性\n- 服装: モダンなスーツ\n\n# 環境・光\n- 場所: オフィスのカフェスペース\n\n# スタイル\n- 写真調, 高画質, 8k</div>
                </div>

                <!-- Interactive Cauldron -->
                <h3 style="color:#065f46; margin-top:3rem; font-size:1.5rem;"><i class="fa-solid fa-flask-vial"></i> 体験：プロンプト調合釜（Cauldron Simulator）</h3>
                <p>要素（チップ）を下の「魔法の釜（ドロップゾーン）」にドラッグ＆ドロップして完成させましょう！</p>
                <div class="cauldron-container" id="cauldron-drop-area">
                    <div class="cauldron-ingredients" id="ingredients-list">
                        <div class="drag-chip chip-sub" draggable="true" data-text="サイバーパンクな街並み," id="c_ing1"><i class="fa-solid fa-city"></i> サイバーパンク街 (Subject)</div>
                        <div class="drag-chip chip-style" draggable="true" data-text="水彩画タッチ, 淡い色合い," id="c_ing2"><i class="fa-solid fa-palette"></i> 水彩画タッチ (Style)</div>
                        <div class="drag-chip chip-style" draggable="true" data-text="シネマティックライティング, 8k," id="c_ing3"><i class="fa-solid fa-video"></i> シネマティック (Lighting)</div>
                        <div class="drag-chip chip-param" draggable="true" data-text="--ar 16:9" id="c_ing4"><i class="fa-solid fa-expand"></i> 横長 (--ar)</div>
                    </div>
                    <div class="cauldron-pot-area" ondrop="drop(event)" ondragover="allowDrop(event)" ondragleave="dragLeave(event)">
                        <div class="cauldron-dropzone" id="cauldron-state">
                            <i class="fa-solid fa-fire text-slate-400"></i>
                            <span id="cauldron-msg">ここにドロップ！(<span id="ing-count">0</span>/4)</span>
                        </div>
                    </div>
                </div>

                <div class="code-box cauldron-result" id="cauldron-result">
                    <span class="code-label" style="background:#10b981;">完成したプロンプト</span>
                    <div class="cauldron-out-chips" id="cauldron-out-chips"></div>
                    <div id="cauldron-out-text" style="font-family: inherit;"></div>
                    <button class="btn" style="margin-top:1.5rem; background: rgba(255,255,255,0.1); border:1px solid rgba(255,255,255,0.2); color:#fff; display:block;" onclick="simImages()"><i class="fa-solid fa-wand-magic-sparkles"></i> 擬似生成する</button>
                    <div id="sim-result" style="display:none; margin-top:1rem; color:#34d399; font-weight:bold;">✨ AI Image Generated! (Simulation)</div>
                </div>

                <!-- GAMIFIED MISSION 1 -->
                <div class="mission-area" id="mission-group-1" style="border-color: #10b981;">
                    <div class="wax-seal" style="background: radial-gradient(circle at 30% 30%, #6ee7b7, #10b981, #047857); border-color:#065f46;"><i class="fa-solid fa-check"></i></div>
                    <div class="mission-header">
                        <h3 style="color:#10b981;"><i class="fa-solid fa-clipboard-list"></i> MILESTONE 1: 画像生成の基礎</h3>
                        <p>プロンプトの構成要素をマスターしよう。</p>
                    </div>
                    <ul class="task-list">
                        <li class="task-item" onclick="toggleTask('t1_1', this, 1)">
                            <div class="custom-checkbox" id="check_t1_1"><i class="fa-solid fa-check"></i></div>
                            <div class="task-content">
                                <h4>基礎動画の視聴</h4>
                                <p>動画①②を視聴し、画像生成の基本的な考え方を理解する。</p>
                            </div>
                        </li>
                        <li class="task-item" onclick="toggleTask('t1_2', this, 1)">
                            <div class="custom-checkbox" id="check_t1_2"><i class="fa-solid fa-check"></i></div>
                            <div class="task-content">
                                <h4>調合釜シミュレーターの完了</h4>
                                <p>上のシミュレーターで4つの要素をドラッグ＆ドロップし、「擬似生成」ボタンを押す。</p>
                            </div>
                        </li>
                    </ul>
                </div>

            </div>
            <div style="text-align:center; padding: 2rem 0;">
                <button class="btn" style="padding: 1rem 3rem; font-size:1.2rem; border-radius:30px; background:#10b981;" onclick="switchTab('tab-second'); window.scrollTo(0,0);">
                    後半の実習へ進む <i class="fa-solid fa-arrow-right"></i>
                </button>
            </div>
        </div>
"""

with open("vol04-1_nano_banana.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated vol04-1_nano_banana.html")
import os

html_content = """
        <!-- ==========================================
             TAB 3: SECOND HALF
        ========================================== -->
        <div id="tab-second" class="tab-content">
            <div class="glass-card" style="border-top: 5px solid #0ea5e9;">
                <div class="card-header"><i class="fa-solid fa-layer-group" style="color:#0ea5e9; background:#e0f2fe;"></i><h2>後半：実践・画像編集テクニック</h2></div>
                <p style="font-size:1.1rem; margin-bottom:1.5rem;">生成した画像を思い通りに修正・加工する「インペイント」等の技術と、実務で使える20の活用法。</p>
                
                <div class="video-grid">
                    <a href="https://youtu.be/SP4FceXU1e4" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/SP4FceXU1e4/hqdefault.jpg" alt="動画3">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                    <a href="https://youtu.be/EcQNRpZE7Ns" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/EcQNRpZE7Ns/hqdefault.jpg" alt="動画4">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                </div>

                <h3 style="color:#0369a1; margin-top:3rem; font-size:1.5rem;"><i class="fa-solid fa-toolbox"></i> Nano Banana Pro 活用術 抜粋</h3>
                
                <!-- Accordions -->
                <details class="prompt-accordion">
                    <summary><span class="tag">Tip</span> ① キャラクターの一貫性 (Character Reference) <i class="fa-solid fa-chevron-down"></i></summary>
                    <div class="prompt-content">
                        <p style="margin-top:0;"><strong>解説:</strong> 同じ人物を違うポーズや服装で生成。「--cref」パラメータを使います。</p>
                        <div class="browser-mockup">
                            <div class="browser-header">
                                <div class="browser-dot" style="background:#ef4444"></div><div class="browser-dot" style="background:#f59e0b"></div><div class="browser-dot" style="background:#10b981"></div>
                            </div>
                            <div class="browser-content">
                                <button class="btn-copy" onclick="copyCode('p-1', this)"><i class="fa-regular fa-copy"></i> Copy</button>
                                <div id="p-1">カフェでコーヒーを飲む女性、笑顔 --cref [画像URL] --cw 100</div>
                            </div>
                        </div>
                    </div>
                </details>

                <details class="prompt-accordion">
                    <summary><span class="tag">Tip</span> ② 高度な部分修正 (Inpaint) <i class="fa-solid fa-chevron-down"></i></summary>
                    <div class="prompt-content">
                        <p style="margin-top:0;"><strong>解説:</strong> 既存画像の「一部だけ」を指定して別のものに書き換える技術。服を変えたり、不要なものを消したりできます。</p>
                        <div class="browser-mockup">
                            <div class="browser-header">
                                <div class="browser-dot" style="background:#ef4444"></div><div class="browser-dot" style="background:#f59e0b"></div><div class="browser-dot" style="background:#10b981"></div>
                            </div>
                            <div class="browser-content">
                                <button class="btn-copy" onclick="copyCode('p-2', this)"><i class="fa-regular fa-copy"></i> Copy</button>
                                <div id="p-2">(服の部分を選択して) 赤いシルクのドレス</div>
                            </div>
                        </div>
                    </div>
                </details>

                <details class="prompt-accordion">
                    <summary><span class="tag">Tip</span> ③ 構図・スタイルのコピー (Style Reference) <i class="fa-solid fa-chevron-down"></i></summary>
                    <div class="prompt-content">
                        <p style="margin-top:0;"><strong>解説:</strong> 手持ちの画像の「雰囲気や画風」だけを借りて新しい画像を作ります。「--sref」パラメータを使います。</p>
                        <div class="browser-mockup">
                            <div class="browser-header">
                                <div class="browser-dot" style="background:#ef4444"></div><div class="browser-dot" style="background:#f59e0b"></div><div class="browser-dot" style="background:#10b981"></div>
                            </div>
                            <div class="browser-content">
                                <button class="btn-copy" onclick="copyCode('p-3', this)"><i class="fa-regular fa-copy"></i> Copy</button>
                                <div id="p-3">サイバーパンクな街並み --sref [水彩画の画像URL]</div>
                            </div>
                        </div>
                    </div>
                </details>

                <details class="prompt-accordion">
                    <summary><span class="tag">Tip</span> ④ 画像の拡張 (Outpaint / Zoom) <i class="fa-solid fa-chevron-down"></i></summary>
                    <div class="prompt-content">
                        <p style="margin-top:0;"><strong>解説:</strong> 縦長で作ってしまった画像をアップスケールせずに横の背景をAIに描き足させ、16:9に変えることができます。</p>
                        <div class="browser-mockup">
                            <div class="browser-header">
                                <div class="browser-dot" style="background:#ef4444"></div><div class="browser-dot" style="background:#f59e0b"></div><div class="browser-dot" style="background:#10b981"></div>
                            </div>
                            <div class="browser-content">
                                <button class="btn-copy" onclick="copyCode('p-4', this)"><i class="fa-regular fa-copy"></i> Copy</button>
                                <div id="p-4">(Pan ➡️ ボタンをクリック)</div>
                            </div>
                        </div>
                    </div>
                </details>

                <!-- GAMIFIED MISSION 2 -->
                <div class="mission-area" id="mission-group-2" style="border-color: #0ea5e9;">
                    <div class="wax-seal" style="background: radial-gradient(circle at 30% 30%, #7dd3fc, #0ea5e9, #0369a1); border-color:#0284c7;"><i class="fa-solid fa-stamp"></i></div>
                    <div class="mission-header">
                        <h3 style="color:#0ea5e9;"><i class="fa-solid fa-book-open-reader"></i> MILESTONE 2: 応用と実践</h3>
                        <p>高度な技術で実務プロンプトを完成させよう！</p>
                    </div>
                    
                    <ul class="task-list">
                        <li class="task-item" onclick="toggleTask('t2_1', this, 2)">
                            <div class="custom-checkbox" id="check_t2_1"><i class="fa-solid fa-check"></i></div>
                            <div class="task-content">
                                <h4>活用術動画の視聴</h4>
                                <p>動画③④を視聴し、インペイントなどの加工技術を学ぶ。</p>
                            </div>
                        </li>
                        <li class="task-item" onclick="toggleTask('t2_2', this, 2)">
                            <div class="custom-checkbox" id="check_t2_2"><i class="fa-solid fa-check"></i></div>
                            <div class="task-content">
                                <h4>プロンプトのストック</h4>
                                <p>上の活用術アコーディオンから、自分が使いそうなテクニックをクリップボードにコピー（またはメモ）する。</p>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>

            <div style="text-align:center; padding: 2rem 0;">
                <button class="btn" style="padding: 1rem 3rem; font-size:1.2rem; background:#8b5cf6; border-radius:30px;" onclick="switchTab('tab-summary'); window.scrollTo(0,0);">
                    本日のまとめを見る <i class="fa-solid fa-flag-checkered"></i>
                </button>
            </div>
        </div>

        <!-- ==========================================
             TAB 4: SUMMARY
        ========================================== -->
        <div id="tab-summary" class="tab-content">
            <div class="glass-card" style="border: 2px solid #8b5cf6; background: #faf5ff;">
                <h3 style="color:#8b5cf6; font-size:1.8rem; margin-top:0; border-bottom:2px solid #ddd6fe; padding-bottom:1.5rem; display:flex; align-items:center; justify-content:center; gap:15px; font-weight:900;">
                    <i class="fa-solid fa-medal" style="font-size:2.5rem;"></i> Day 4 全行程コンプリート！
                </h3>
                <p style="font-size: 1.25rem; line-height: 2; color: #4c1d95; margin-top:2rem; text-align:center; padding: 0 2rem;">
                    お疲れ様でした！本日は<strong>「画像生成と高度加工」</strong>について学びました。<br>
                    1枚の画像をゼロから生み出すだけでなく、リファレンス（参照）機能やInpaint（部分修正）を駆使することで、完全にコントロールされた素材を手に入れることができます。<br><br>
                    次回はいよいよ、生成した画像に命を吹き込む「動画生成」の世界へ入ります！
                </p>
                
                <!-- Quiz Area -->
                <div class="glass-card" style="margin-top:3rem; background:#fff; border-color:#cbd5e1; box-shadow:none;">
                    <h2 style="font-size:1.6rem; margin:0 0 0.5rem; color:var(--text-main);"><i class="fa-solid fa-pen-nib" style="color:#0ea5e9;"></i> 📝 理解度チェック</h2>
                    <p style="color:var(--text-sub); margin-bottom:1.5rem;">Day 4 で学んだ知識を確認しましょう</p>
                    <div id="quiz-vol02-2" style="text-align:left;">
                        <div style="text-align:center; color:var(--text-sub); font-style:italic;">クイズを読み込み中...</div>
                    </div>
                </div>

                <div style="margin-top:3rem; text-align:center;">
                    <button class="btn" style="padding: 1.2rem 4rem; font-size:1.3rem; background:linear-gradient(135deg, #8b5cf6, #6d28d9); border-radius:50px; box-shadow: 0 10px 25px rgba(139, 92, 246, 0.4);" onclick="window.location.href='index.html'">
                        <i class="fa-solid fa-house"></i> 学習完了を記録してHomeへ戻る
                    </button>
                    <!-- Dev Notes Link -->
                    <div style="margin-top: 2rem;">
                        <a href="index_dev_notes.html" style="color:#94a3b8; text-decoration:none; font-size:0.85rem;"><i class="fa-solid fa-code"></i> 制作の裏側・開発者ノートはこちら</a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <a href="index.html" class="home-btn" title="Back to Home"><i class="fa-solid fa-house"></i></a>

    <!-- Scripts -->
    <script>
        // Tab Nav
        function switchTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
            document.getElementById(tabId).classList.add('active');
            
            const buttons = document.querySelectorAll('.tab-btn');
            for(let i=0; i<buttons.length; i++){
                if(buttons[i].getAttribute('onclick').includes(tabId)){
                    buttons[i].classList.add('active');
                }
            }
        }

        // Copy
        function copyCode(elementId, btn) {
            const text = document.getElementById(elementId).innerText;
            navigator.clipboard.writeText(text).then(() => {
                const orig = btn.innerHTML;
                btn.innerHTML = '<i class="fa-solid fa-check"></i>';
                btn.style.color = '#10b981';
                setTimeout(() => { btn.innerHTML = orig; btn.style.color = ''; }, 2000);
            });
        }

        // Checklist Logic
        const missionGroups = {
            1: ['t1_1', 't1_2'],
            2: ['t2_1', 't2_2']
        };
        const allTasks = [...missionGroups[1], ...missionGroups[2]];
        let state = {};

        window.addEventListener('DOMContentLoaded', () => {
            const saved = localStorage.getItem('day4_premium_prog');
            if (saved) {
                state = JSON.parse(saved);
                for (const taskId of allTasks) {
                    if (state[taskId]) {
                        const el = document.getElementById('check_' + taskId);
                        if (el) el.parentElement.classList.add('completed');
                    }
                }
            }
            checkGroups();
            updateProgress();
        });

        function toggleTask(taskId, element, groupId) {
            const done = element.classList.toggle('completed');
            state[taskId] = done;
            localStorage.setItem('day4_premium_prog', JSON.stringify(state));
            
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
            const pct = Math.round((count / allTasks.length) * 100);
            document.getElementById('progress-bar').style.width = pct + '%';
            document.getElementById('progress-percent').innerText = pct + '%';
        }

        // Drag & Drop
        let itemsInCauldron = 0;
        let pText = "";
        
        // Use a simpler approach for events.
        function allowDrop(ev) {
            ev.preventDefault();
            document.getElementById('cauldron-state').classList.add('drag-over');
        }
        function dragLeave(ev) {
            document.getElementById('cauldron-state').classList.remove('drag-over');
        }
        
        function drag(ev) {
            ev.dataTransfer.setData("text", ev.target.id);
            ev.dataTransfer.effectAllowed = "move";
        }
        
        function drop(ev) {
            ev.preventDefault();
            document.getElementById('cauldron-state').classList.remove('drag-over');

            var id = ev.dataTransfer.getData("text");
            var draggedItem = document.getElementById(id);

            if (draggedItem && !draggedItem.classList.contains('used')) {
                draggedItem.classList.add('used');
                itemsInCauldron++;
                document.getElementById('ing-count').innerText = itemsInCauldron;
                
                let text = draggedItem.getAttribute('data-text');
                pText += text + " ";
                document.getElementById('cauldron-out-text').innerText = pText;
                
                let clone = draggedItem.cloneNode(true);
                clone.removeAttribute('draggable');
                clone.classList.remove('used');
                document.getElementById('cauldron-out-chips').appendChild(clone);

                if (itemsInCauldron >= 4) {
                    document.getElementById('cauldron-result').style.display = 'block';
                    document.getElementById('cauldron-msg').innerText = "完了！擬似生成してください";
                }
            }
        }
        
        function simImages() {
           document.getElementById('sim-result').style.display = "block";
        }

        // Confetti Function
        function fireConfetti() {
            const c = document.getElementById('confetti');
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
    </script>
</body>
</html>
"""

with open("vol04-1_nano_banana.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated vol04-1_nano_banana.html")


        <!-- ==========================================
             TAB 3: SECOND HALF
        ========================================== -->
        <div id="tab-second" class="tab-content">
            <div class="glass-card" style="border-top: 5px solid #0ea5e9;">
                <div class="card-header"><i class="fa-solid fa-layer-group" style="color:#0ea5e9; background:#e0f2fe;"></i><h2>後半：実践・画像編集テクニック</h2></div>
                <p style="font-size:1.1rem; margin-bottom:1.5rem;">生成した画像を思い通りに修正・加工する「インペイント」等の技術と、実務で使える20の活用法。</p>
                
                <div class="video-grid">
                    <a href="https://youtu.be/SP4FceXU1e4" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/SP4FceXU1e4/hqdefault.jpg" alt="動画3">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                    <a href="https://youtu.be/EcQNRpZE7Ns" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/EcQNRpZE7Ns/hqdefault.jpg" alt="動画4">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                </div>

                <div class="highlight-box" style="background: linear-gradient(135deg, #e0f2fe, #bae6fd); border-color: #7dd3fc; color: #0369a1; margin-top:3rem;">
                    <h3 style="color:#0284c7; border-bottom-color:#38bdf8;"><i class="fa-solid fa-bolt"></i> 読むだけでわかる！完全解説ダイジェスト</h3>
                    <p style="margin-bottom:0; line-height:1.7;">Nano Banana Pro ＆ Imagen 3(Google) の実践活用術と裏技です。</p>
                </div>
                <div class="bento-grid">
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-user-ninja" style="color:#10b981;"></i> 1. Imagen 3のテキスト再現</h4>
                        <p>Geminiの裏側で動く画像AIは、イラスト内に「看板の文字」などを正確に出力できる機能に優れており、ポスターやバナー素材の作成に威力を発揮します。</p>
                    </div>
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-face-smile-wink" style="color:#f43f5e;"></i> 2. 表情とライティングの徹底</h4>
                        <p>プロンプトに「シネマティックライティング」「ボケみ（DOF）」「逆光」などの写真用語を盛り込むことで、出力画像のプロっぽさが劇的向上します。</p>
                    </div>
                </div>


                <h3 style="color:#0369a1; margin-top:3rem; font-size:1.5rem;"><i class="fa-solid fa-toolbox"></i> Nano Banana Pro 活用術 抜粋</h3>
                
                <!-- Accordions -->
                <details class="prompt-accordion">
                    <summary><span class="tag">Tip</span> ① キャラクターの一貫性 (Character Reference) <i class="fa-solid fa-chevron-down"></i></summary>
                    <div class="prompt-content">
                        <p style="margin-top:0;"><strong>解説:</strong> 同じ人物を違うポーズや服装で生成。「--cref」パラメータを使います。</p>
                        <div class="browser-mockup">
                            <div class="browser-header">
                                <div class="browser-dot" style="background:#ef4444"></div><div class="browser-dot" style="background:#f59e0b"></div><div class="browser-dot" style="background:#10b981"></div>
                            </div>
                            <div class="browser-content">
                                <button class="btn-copy" onclick="copyCode('p-1', this)"><i class="fa-regular fa-copy"></i> Copy</button>
                                <div id="p-1">カフェでコーヒーを飲む女性、笑顔 --cref [画像URL] --cw 100</div>
                            </div>
                        </div>
                    </div>
                </details>

                <details class="prompt-accordion">
                    <summary><span class="tag">Tip</span> ② 高度な部分修正 (Inpaint) <i class="fa-solid fa-chevron-down"></i></summary>
                    <div class="prompt-content">
                        <p style="margin-top:0;"><strong>解説:</strong> 既存画像の「一部だけ」を指定して別のものに書き換える技術。服を変えたり、不要なものを消したりできます。</p>
                        <div class="browser-mockup">
                            <div class="browser-header">
                                <div class="browser-dot" style="background:#ef4444"></div><div class="browser-dot" style="background:#f59e0b"></div><div class="browser-dot" style="background:#10b981"></div>
                            </div>
                            <div class="browser-content">
                                <button class="btn-copy" onclick="copyCode('p-2', this)"><i class="fa-regular fa-copy"></i> Copy</button>
                                <div id="p-2">(服の部分を選択して) 赤いシルクのドレス</div>
                            </div>
                        </div>
                    </div>
                </details>

                <details class="prompt-accordion">
                    <summary><span class="tag">Tip</span> ③ 構図・スタイルのコピー (Style Reference) <i class="fa-solid fa-chevron-down"></i></summary>
                    <div class="prompt-content">
                        <p style="margin-top:0;"><strong>解説:</strong> 手持ちの画像の「雰囲気や画風」だけを借りて新しい画像を作ります。「--sref」パラメータを使います。</p>
                        <div class="browser-mockup">
                            <div class="browser-header">
                                <div class="browser-dot" style="background:#ef4444"></div><div class="browser-dot" style="background:#f59e0b"></div><div class="browser-dot" style="background:#10b981"></div>
                            </div>
                            <div class="browser-content">
                                <button class="btn-copy" onclick="copyCode('p-3', this)"><i class="fa-regular fa-copy"></i> Copy</button>
                                <div id="p-3">サイバーパンクな街並み --sref [水彩画の画像URL]</div>
                            </div>
                        </div>
                    </div>
                </details>

                <details class="prompt-accordion">
                    <summary><span class="tag">Tip</span> ④ 画像の拡張 (Outpaint / Zoom) <i class="fa-solid fa-chevron-down"></i></summary>
                    <div class="prompt-content">
                        <p style="margin-top:0;"><strong>解説:</strong> 縦長で作ってしまった画像をアップスケールせずに横の背景をAIに描き足させ、16:9に変えることができます。</p>
                        <div class="browser-mockup">
                            <div class="browser-header">
                                <div class="browser-dot" style="background:#ef4444"></div><div class="browser-dot" style="background:#f59e0b"></div><div class="browser-dot" style="background:#10b981"></div>
                            </div>
                            <div class="browser-content">
                                <button class="btn-copy" onclick="copyCode('p-4', this)"><i class="fa-regular fa-copy"></i> Copy</button>
                                <div id="p-4">(Pan ➡️ ボタンをクリック)</div>
                            </div>
                        </div>
                    </div>
                </details>

                <!-- GAMIFIED MISSION 2 -->
                <div class="mission-area" id="mission-group-2" style="border-color: #0ea5e9;">
                    <div class="wax-seal" style="background: radial-gradient(circle at 30% 30%, #7dd3fc, #0ea5e9, #0369a1); border-color:#0284c7;"><i class="fa-solid fa-stamp"></i></div>
                    <div class="mission-header">
                        <h3 style="color:#0ea5e9;"><i class="fa-solid fa-book-open-reader"></i> MILESTONE 2: 応用と実践</h3>
                        <p>高度な技術で実務プロンプトを完成させよう！</p>
                    </div>
                    
                    <ul class="task-list">
                        <li class="task-item" onclick="toggleTask('t2_1', this, 2)">
                            <div class="custom-checkbox" id="check_t2_1"><i class="fa-solid fa-check"></i></div>
                            <div class="task-content">
                                <h4>活用術動画の視聴</h4>
                                <p>動画③④を視聴し、インペイントなどの加工技術を学ぶ。</p>
                            </div>
                        </li>
                        <li class="task-item" onclick="toggleTask('t2_2', this, 2)">
                            <div class="custom-checkbox" id="check_t2_2"><i class="fa-solid fa-check"></i></div>
                            <div class="task-content">
                                <h4>プロンプトのストック</h4>
                                <p>上の活用術アコーディオンから、自分が使いそうなテクニックをクリップボードにコピー（またはメモ）する。</p>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>

            <div style="text-align:center; padding: 2rem 0;">
                <button class="btn" style="padding: 1rem 3rem; font-size:1.2rem; background:#8b5cf6; border-radius:30px;" onclick="switchTab('tab-summary'); window.scrollTo(0,0);">
                    本日のまとめを見る <i class="fa-solid fa-flag-checkered"></i>
                </button>
            </div>
        </div>

        <!-- ==========================================
             TAB 4: SUMMARY
        ========================================== -->
        <div id="tab-summary" class="tab-content">
            <div class="glass-card" style="border: 2px solid #8b5cf6; background: #faf5ff;">
                <h3 style="color:#8b5cf6; font-size:1.8rem; margin-top:0; border-bottom:2px solid #ddd6fe; padding-bottom:1.5rem; display:flex; align-items:center; justify-content:center; gap:15px; font-weight:900;">
                    <i class="fa-solid fa-medal" style="font-size:2.5rem;"></i> Day 4 全行程コンプリート！
                </h3>
                <p style="font-size: 1.25rem; line-height: 2; color: #4c1d95; margin-top:2rem; text-align:center; padding: 0 2rem;">
                    お疲れ様でした！本日は<strong>「画像生成と高度加工」</strong>について学びました。<br>
                    1枚の画像をゼロから生み出すだけでなく、リファレンス（参照）機能やInpaint（部分修正）を駆使することで、完全にコントロールされた素材を手に入れることができます。<br><br>
                    次回はいよいよ、生成した画像に命を吹き込む「動画生成」の世界へ入ります！
                </p>
                
                <!-- Quiz Area -->
                <div class="glass-card" style="margin-top:3rem; background:#fff; border-color:#cbd5e1; box-shadow:none;">
                    <h2 style="font-size:1.6rem; margin:0 0 0.5rem; color:var(--text-main);"><i class="fa-solid fa-pen-nib" style="color:#0ea5e9;"></i> 📝 理解度チェック</h2>
                    <p style="color:var(--text-sub); margin-bottom:1.5rem;">Day 4 で学んだ知識を確認しましょう</p>
                    <div id="quiz-vol02-2" style="text-align:left;">
                        <div style="text-align:center; color:var(--text-sub); font-style:italic;">クイズを読み込み中...</div>
                    </div>
                </div>

                <div style="margin-top:3rem; text-align:center;">
                    <button class="btn" style="padding: 1.2rem 4rem; font-size:1.3rem; background:linear-gradient(135deg, #8b5cf6, #6d28d9); border-radius:50px; box-shadow: 0 10px 25px rgba(139, 92, 246, 0.4);" onclick="window.location.href='index.html'">
                        <i class="fa-solid fa-house"></i> 学習完了を記録してHomeへ戻る
                    </button>
                    <!-- Dev Notes Link -->
                    <div style="margin-top: 2rem;">
                        <a href="index_dev_notes.html" style="color:#94a3b8; text-decoration:none; font-size:0.85rem;"><i class="fa-solid fa-code"></i> 制作の裏側・開発者ノートはこちら</a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <a href="index.html" class="home-btn" title="Back to Home"><i class="fa-solid fa-house"></i></a>

    <!-- Scripts -->
    <script>
        // Tab Nav
        function switchTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
            document.getElementById(tabId).classList.add('active');
            
            const buttons = document.querySelectorAll('.tab-btn');
            for(let i=0; i<buttons.length; i++){
                if(buttons[i].getAttribute('onclick').includes(tabId)){
                    buttons[i].classList.add('active');
                }
            }
        }

        // Copy
        function copyCode(elementId, btn) {
            const text = document.getElementById(elementId).innerText;
            navigator.clipboard.writeText(text).then(() => {
                const orig = btn.innerHTML;
                btn.innerHTML = '<i class="fa-solid fa-check"></i>';
                btn.style.color = '#10b981';
                setTimeout(() => { btn.innerHTML = orig; btn.style.color = ''; }, 2000);
            });
        }

        // Checklist Logic
        const missionGroups = {
            1: ['t1_1', 't1_2'],
            2: ['t2_1', 't2_2']
        };
        const allTasks = [...missionGroups[1], ...missionGroups[2]];
        let state = {};

        window.addEventListener('DOMContentLoaded', () => {
            const saved = localStorage.getItem('day4_premium_prog');
            if (saved) {
                state = JSON.parse(saved);
                for (const taskId of allTasks) {
                    if (state[taskId]) {
                        const el = document.getElementById('check_' + taskId);
                        if (el) el.parentElement.classList.add('completed');
                    }
                }
            }
            checkGroups();
            updateProgress();
        });

        function toggleTask(taskId, element, groupId) {
            const done = element.classList.toggle('completed');
            state[taskId] = done;
            localStorage.setItem('day4_premium_prog', JSON.stringify(state));
            
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
            const pct = Math.round((count / allTasks.length) * 100);
            document.getElementById('progress-bar').style.width = pct + '%';
            document.getElementById('progress-percent').innerText = pct + '%';
        }

        // Drag & Drop
        let itemsInCauldron = 0;
        let pText = "";
        
        // Use a simpler approach for events.
        function allowDrop(ev) {
            ev.preventDefault();
            document.getElementById('cauldron-state').classList.add('drag-over');
        }
        function dragLeave(ev) {
            document.getElementById('cauldron-state').classList.remove('drag-over');
        }
        
        function drag(ev) {
            ev.dataTransfer.setData("text", ev.target.id);
            ev.dataTransfer.effectAllowed = "move";
        }
        
        function drop(ev) {
            ev.preventDefault();
            document.getElementById('cauldron-state').classList.remove('drag-over');

            var id = ev.dataTransfer.getData("text");
            var draggedItem = document.getElementById(id);

            if (draggedItem && !draggedItem.classList.contains('used')) {
                draggedItem.classList.add('used');
                itemsInCauldron++;
                document.getElementById('ing-count').innerText = itemsInCauldron;
                
                let text = draggedItem.getAttribute('data-text');
                pText += text + " ";
                document.getElementById('cauldron-out-text').innerText = pText;
                
                let clone = draggedItem.cloneNode(true);
                clone.removeAttribute('draggable');
                clone.classList.remove('used');
                document.getElementById('cauldron-out-chips').appendChild(clone);

                if (itemsInCauldron >= 4) {
                    document.getElementById('cauldron-result').style.display = 'block';
                    document.getElementById('cauldron-msg').innerText = "完了！擬似生成してください";
                }
            }
        }
        
        function simImages() {
           document.getElementById('sim-result').style.display = "block";
        }

        // Confetti Function
        function fireConfetti() {
            const c = document.getElementById('confetti');
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
    </script>
</body>
</html>
