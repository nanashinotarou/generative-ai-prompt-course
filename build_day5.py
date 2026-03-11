<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day 5 | AI Video Generation & Prompting</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Noto+Sans+JP:wght@400;700&family=Teko:wght@500;600;700&family=Fira+Code&display=swap" rel="stylesheet">
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
            --clickable: #0ea5e9;
            --clickable-light: #e0f2fe;
            --danger: #ef4444;
            --warning: #f59e0b;
            --purple: #8b5cf6;
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
                radial-gradient(circle at 10% 20%, rgba(16, 185, 129, 0.05) 0%, transparent 40%),
                radial-gradient(circle at 90% 80%, rgba(14, 165, 233, 0.05) 0%, transparent 40%);
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

        /* Navigation Sidebar (Table of Contents) */
        .toc-sidebar {
            position: fixed; top: 100px; left: 20px; width: 220px; background: white; padding: 1.5rem 1rem;
            border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid #f1f5f9; z-index: 100;
        }
        .toc-title { font-size: 0.85rem; font-weight: 800; color: var(--text-sub); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 1rem; padding-left: 10px; }
        .toc-link {
            display: flex; align-items: center; gap: 10px; padding: 10px; border-radius: 8px;
            color: var(--text-main); text-decoration: none; font-weight: 600; font-size: 0.9rem; transition: all 0.2s;
        }
        .toc-link:hover { background: #f1f5f9; color: var(--clickable); }
        .toc-link.active { background: var(--clickable-light); color: var(--clickable); }
        .toc-link i { font-size: 1.1rem; width: 20px; text-align: center; }

        /* Main Content Container */
        .container { max-width: 900px; margin: 100px auto 100px; padding: 0 20px 0 240px; }
        @media (max-width: 1200px) {
            .toc-sidebar { display: none; }
            .container { padding-left: 20px; }
        }

        /* Section Styling */
        .course-section { margin-bottom: 5rem; animation: fadeInUp 0.6s ease-out forwards; opacity: 0; transform: translateY(20px); }
        .course-section.visible { opacity: 1; transform: translateY(0); }
        .section-header { display: flex; align-items: center; gap: 15px; margin-bottom: 2rem; padding-bottom: 1rem; border-bottom: 3px solid #e2e8f0; }
        .section-icon { width: 50px; height: 50px; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; color: white; background: var(--text-main); box-shadow: 0 8px 16px rgba(0,0,0,0.1); }
        .section-title { margin: 0; font-size: 2rem; font-weight: 800; letter-spacing: -0.5px; }

        .ch-goal { background: linear-gradient(135deg, #f59e0b, #d97706); }
        .ch-first { background: linear-gradient(135deg, #3b82f6, #2563eb); }
        .ch-second { background: linear-gradient(135deg, #8b5cf6, #7c3aed); }
        .ch-wrap { background: linear-gradient(135deg, #10b981, #059669); }

        /* Component: Cards */
        .glass-card { background: var(--bg-card); border: 1px solid rgba(0,0,0,0.05); border-radius: var(--radius); padding: 2.5rem; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.02); transition: transform 0.3s, box-shadow 0.3s; }
        .glass-card:hover { transform: translateY(-2px); box-shadow: 0 15px 35px rgba(0,0,0,0.06); }
        .card-header-small { display: flex; align-items: center; gap: 10px; margin-bottom: 1.5rem; border-bottom: 1px solid #f1f5f9; padding-bottom: 1rem; font-weight: 700; font-size: 1.3rem;}
        
        /* Component: Explanation Boxes */
        .explain-box { background: #eff6ff; border-left: 4px solid var(--clickable); padding: 1.5rem; border-radius: 0 12px 12px 0; margin-bottom: 2rem; line-height: 1.7; position: relative;}
        .explain-title { font-weight: 800; color: #1e3a8a; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 8px;}
        .explain-box.concept { background: #fdf4ff; border-left-color: #d946ef; }
        .explain-box.concept .explain-title { color: #86198f; }
        .explain-box.practice { background: #f0fdf4; border-left-color: #10b981; }
        .explain-box.practice .explain-title { color: #065f46; }

        /* Hero Badges */
        .hero { text-align: center; margin-bottom: 4rem; }
        .day-badge { background: var(--text-main); color: #fff; padding: 0.5rem 2rem; border-radius: 30px; font-family: 'Teko', sans-serif; font-size: 1.5rem; letter-spacing: 2px; display: inline-block; margin-bottom: 1.5rem; }
        .hero h1 { font-size: clamp(2.5rem, 5vw, 4rem); margin: 0 0 1rem; font-weight: 900; letter-spacing: -1.5px; line-height: 1.1; }

        /* Video Thumbnails */
        .video-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 1rem; margin-bottom: 2rem;}
        .video-thumb { position: relative; border-radius: 16px; overflow: hidden; display: block; border: 1px solid rgba(0,0,0,0.1); box-shadow: 0 10px 25px rgba(0,0,0,0.08); transition: all 0.3s; background: #000;}
        .video-thumb:hover { transform: translateY(-5px); box-shadow: 0 20px 40px rgba(0,0,0,0.15); border-color: var(--clickable);}
        .video-thumb img { width: 100%; display: block; opacity: 0.9; transition: opacity 0.3s, transform 0.5s;}
        .video-thumb:hover img { opacity: 1; transform: scale(1.05);}
        .play-overlay { position: absolute; inset: 0; background: rgba(0,0,0,0.2); display: flex; align-items: center; justify-content: center; transition: all 0.3s;}
        .video-thumb:hover .play-overlay { background: rgba(14, 165, 233, 0.3);}
        .play-icon { width: 70px; height: 70px; background: rgba(255,255,255,0.9); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #ef4444; font-size: 2rem; box-shadow: 0 10px 20px rgba(0,0,0,0.2); transition: transform 0.3s;}
        .video-thumb:hover .play-icon { transform: scale(1.1); background: #fff; color: #b91c1c; }

        /* Director Simulator (Interactive UI) */
        .simulator-area { background: #1e293b; border-radius: 16px; padding: 2.5rem; color: #f8fafc; margin: 2.5rem 0; box-shadow: 0 20px 40px rgba(0,0,0,0.2); border: 1px solid #334155; }
        .sim-title { font-size: 1.6rem; font-weight: 800; margin-top: 0; margin-bottom: 0.5rem; color: #38bdf8; display: flex; align-items: center; gap: 12px; }
        .sim-desc { color: #94a3b8; font-size: 0.95rem; margin-bottom: 2rem; border-bottom: 1px solid #334155; padding-bottom: 1rem;}
        
        .sim-grid { display: grid; grid-template-columns: 1fr 1.5fr; gap: 2.5rem; }
        @media (max-width: 768px) { .sim-grid { grid-template-columns: 1fr; } }
        
        .sim-controls { display: flex; flex-direction: column; gap: 1.5rem; }
        .ctrl-group { background: #0f172a; padding: 1.2rem; border-radius: 12px; border: 1px solid #334155;}
        .ctrl-label { font-size: 0.85rem; font-weight: 700; color: #cbd5e1; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;}
        .ctrl-select { width: 100%; background: #1e293b; color: #fff; border: 1px solid #475569; padding: 12px; border-radius: 8px; font-size: 1rem; cursor: pointer; outline: none; }
        .ctrl-select:focus { border-color: #38bdf8; }
        
        .sim-btn { background: linear-gradient(135deg, #38bdf8, #0284c7); color: #fff; border: none; padding: 16px; border-radius: 12px; font-weight: 800; font-size: 1.1rem; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; justify-content: center; gap: 10px; box-shadow: 0 10px 20px rgba(56, 189, 248, 0.2); margin-top: 10px;}
        .sim-btn:hover { transform: translateY(-3px); box-shadow: 0 15px 30px rgba(56, 189, 248, 0.4); }
        .sim-btn:active { transform: translateY(0); }
        
        .vp-wrapper { background: #000; border-radius: 16px; height: 320px; position: relative; overflow: hidden; border: 4px solid #0f172a; box-shadow: inset 0 0 40px rgba(0,0,0,0.9); }
        .vp-view { width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; position: relative; transition: all 2s cubic-bezier(0.25, 1, 0.5, 1); }
        .vp-subject { font-size: 6rem; position: relative; z-index: 2; text-shadow: 0 10px 20px rgba(0,0,0,0.5); transition: all 2s ease;}
        .vp-bg { position: absolute; font-size: 15rem; opacity: 0.15; color: #fff; z-index: 1; transition: all 2s cubic-bezier(0.25, 1, 0.5, 1); filter: blur(2px);}
        
        /* Camera Animations CSS Classes */
        .cam-none .vp-view { transform: none; }
        .cam-pan-right .vp-view { transform: translateX(-80px); }
        .cam-pan-left .vp-view { transform: translateX(80px); }
        .cam-zoom-in .vp-view { transform: scale(1.8); }
        .cam-zoom-out .vp-view { transform: scale(0.5); }
        
        .act-none { transform: none; }
        .act-walk { animation: walkCycle 2s infinite alternate ease-in-out; }
        .act-jump { animation: jumpCycle 1.5s infinite cubic-bezier(0.28, 0.84, 0.42, 1); }
        
        @keyframes walkCycle { 0% { transform: translateY(0) rotate(0deg); } 50% { transform: translateY(-15px) rotate(8deg); } 100% { transform: translateY(0) rotate(-8deg); } }
        @keyframes jumpCycle { 0%, 100% { transform: translateY(0) scaleY(1); } 50% { transform: translateY(-60px) scaleY(1.1); } }
        
        .sim-output { background: #000; padding: 15px; border-radius: 8px; font-family: 'Fira Code', monospace; color: #a5b4fc; margin-top: 20px; font-size: 0.95rem; text-align: center; border: 1px solid #334155; word-wrap: break-word;}

        /* Mission Checkboxes (Gamification) */
        .mission-panel { background: #fff; border: 2px dashed #cbd5e1; border-radius: 16px; padding: 2rem; margin: 2.5rem 0; display: flex; align-items: center; gap: 2rem; cursor: pointer; transition: all 0.3s; position: relative; overflow: hidden;}
        .mission-panel:hover { border-color: var(--accent); background: #f0fdf4; transform: translateY(-2px); box-shadow: 0 10px 20px rgba(16, 185, 129, 0.1); }
        .ms-icon { font-size: 3rem; color: #cbd5e1; transition: color 0.3s; }
        .mission-panel:hover .ms-icon { color: var(--accent-light); }
        .ms-content { flex-grow: 1; }
        .ms-content h3 { margin: 0 0 0.5rem; font-size: 1.4rem; color: var(--text-main); }
        .ms-content p { margin: 0; color: var(--text-sub); line-height: 1.6; }
        
        .ms-check { width: 44px; height: 44px; border: 3px solid #cbd5e1; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; background: #fff; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
        .ms-check i { color: #fff; font-size: 20px; opacity: 0; transform: scale(0); transition: all 0.4s; }
        
        .mission-panel.completed { border-color: var(--accent); background: #fff; border-style: solid;}
        .mission-panel.completed .ms-icon { color: var(--accent); }
        .mission-panel.completed .ms-check { background: var(--accent); border-color: var(--accent); transform: scale(1.1); }
        .mission-panel.completed .ms-check i { opacity: 1; transform: scale(1); }
        
        .wax-seal { position: absolute; top: 10px; right: 80px; width: 70px; height: 70px; background: radial-gradient(circle at 30% 30%, #fca5a5, #ef4444, #991b1b); border-radius: 50%; opacity: 0; transform: scale(3) rotate(-20deg); pointer-events: none; display: flex; align-items: center; justify-content: center; color: rgba(255,255,255,0.9); font-size: 1.8rem; box-shadow: inset 0 0 10px rgba(0,0,0,0.5), 0 5px 15px rgba(0,0,0,0.3); border: 2px solid #b91c1c; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.3)); z-index: 10;}
        .wax-seal::after { content: ''; position: absolute; inset: 5px; border: 1px dotted rgba(255,255,255,0.5); border-radius: 50%; }
        .mission-panel.completed .wax-seal { animation: stampIn 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards; }
        
        /* Accordion Prompts */
        .prompt-accordion { margin-bottom: 1rem; border: 1px solid #e2e8f0; border-radius: 12px; background: #fff; overflow: hidden; transition: box-shadow 0.3s; }
        .prompt-accordion:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
        .prompt-accordion summary { padding: 1.2rem 1.5rem; font-weight: 700; font-size: 1.05rem; cursor: pointer; display: flex; align-items: center; justify-content: space-between; list-style: none; background: #f8fafc; }
        .prompt-accordion summary::-webkit-details-marker { display: none; }
        .prompt-accordion summary i.fa-chevron-down { color: var(--text-sub); transition: transform 0.3s; }
        .prompt-accordion[open] summary i.fa-chevron-down { transform: rotate(180deg); color: var(--clickable); }
        .prompt-accordion[open] summary { border-bottom: 1px solid #e2e8f0; background: #fff; }
        .prompt-content { padding: 1.5rem; animation: slideDown 0.3s ease; line-height: 1.6;}
        
        .yt-time-btn { display: inline-flex; align-items: center; gap: 6px; background: #fee2e2; color: #b91c1c; padding: 6px 14px; border-radius: 20px; text-decoration: none; font-size: 0.85rem; font-weight: bold; transition: all 0.2s; border: 1px solid #fca5a5; white-space: nowrap; margin-top: 10px;}
        .yt-time-btn:hover { background: #b91c1c; color: #fff; }
        .tag { background: #e0f2fe; color: #0284c7; padding: 4px 10px; border-radius: 8px; font-size: 0.85rem; font-weight: 800; margin-right: 10px; border: 1px solid #bae6fd;}

        @keyframes fadeInUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
        @keyframes stampIn { 0% { opacity: 0; transform: scale(3) translateY(-50px) rotate(-20deg); } 60% { opacity: 1; transform: scale(0.9) translateY(0) rotate(5deg); } 80% { transform: scale(1.1) rotate(-2deg); } 100% { opacity: 1; transform: scale(1) rotate(0deg); } }
        @keyframes slideDown { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }
        
        .home-btn { position: fixed; bottom: 30px; right: 30px; background: var(--text-main); color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; box-shadow: 0 10px 25px rgba(0,0,0,0.3); text-decoration: none; transition: all 0.3s; z-index: 1000; border: 2px solid rgba(255,255,255,0.2); }
        .home-btn:hover { transform: translateY(-5px) scale(1.05); background: var(--clickable); color: white; }
    </style>
</head>
<body>
    <header class="fixed-header">
        <a href="index.html" class="back-link"><i class="fa-solid fa-arrow-left"></i> Course Home</a>
        <div class="progress-container">
            <div class="progress-text"><span>Day 5 Progress</span><span id="progress-percent">0%</span></div>
            <div class="progress-bar-bg"><div class="progress-bar-fill" id="progress-bar"></div></div>
        </div>
        <div style="width:100px;"></div>
    </header>

    <div class="toc-sidebar">
        <div class="toc-title">IN THIS LESSON</div>
        <nav style="display:flex; flex-direction:column; gap:8px;">
            <a href="#sec-goal" class="toc-link" onclick="updateNav(this)"><i class="fa-solid fa-bullseye" style="color:#f59e0b"></i> 本日の目標</a>
            <a href="#sec-first" class="toc-link" onclick="updateNav(this)"><i class="fa-solid fa-sun" style="color:#3b82f6"></i> 前半：動画生成術</a>
            <a href="#sec-second" class="toc-link" onclick="updateNav(this)"><i class="fa-solid fa-moon" style="color:#8b5cf6"></i> 後半：実践演習</a>
            <a href="#sec-summary" class="toc-link" onclick="updateNav(this)"><i class="fa-solid fa-flag-checkered" style="color:#10b981"></i> 今日のまとめ</a>
        </nav>
    </div>

    <div class="container">
        <!-- HERO -->
        <div class="hero course-section visible" style="margin-top: 2rem;">
            <div class="day-badge">DAY 05</div>
            <h1>AI動画生成と<br>プロンプト技術</h1>
        </div>

        <!-- 1. COURSE GOAL -->
        <section id="sec-goal" class="course-section">
            <div class="section-header">
                <div class="section-icon ch-goal"><i class="fa-solid fa-bullseye"></i></div>
                <h2 class="section-title">1. 今日のコース目標</h2>
            </div>
            
            <div class="glass-card">
                <div class="explain-box concept" style="background: #fffbef; border-left-color: #f59e0b; font-size: 1.1rem;">
                    <div class="explain-title" style="color:#b45309; font-size:1.3rem;"><i class="fa-solid fa-compass"></i> 目標とねらい（どんな人材になるか？）</div>
                    本日の研修テーマは、<b>「テキストから動画への変換技術の基礎」</b>です。<br><br>
                    単に静止画を動かすだけではなく、AIによる高度な**動画生成・カメラワーク・3Dツール連携**を活用し、**テキストベースで高品質な動画コンテンツを制作・発信できる「ディレクター視点を持ったクリエイター」**になることが本日の最大のねらいです。
                </div>
            </div>
        </section>

        <!-- 2. FIRST HALF -->
        <section id="sec-first" class="course-section">
            <div class="section-header">
                <div class="section-icon ch-first"><i class="fa-regular fa-sun"></i></div>
                <h2 class="section-title">2. 前半：説明と解説</h2>
            </div>

            <div class="glass-card">
                <div class="card-header-small"><i class="fa-solid fa-film" style="color:#3b82f6;"></i> 再生動画についての説明と解説</div>
                
                <div class="explain-box concept">
                    <div class="explain-title"><i class="fa-solid fa-lightbulb"></i> 動画生成は「時間」のコントロール</div>
                    静止画を動画にする際、「ただ動くだけ」ではAI特有の不自然さが出てしまいます。<br>
                    前半の動画では、動画のクオリティを劇的に引き上げるための**20のプロンプトテクニック**（表情の変化、速度制御等）と、映像に立体感をもたらす**カメラワーク（Kling AI）**、そしてプロンプトの限界を超える**3Dモデリングツール（Hitem3D等）との連携**について紐解きます。
                </div>

                <div class="video-grid">
                    <a href="https://youtu.be/gDRpdBFwg6Y" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/gDRpdBFwg6Y/maxresdefault.jpg" alt="動画1" onerror="this.src='https://img.youtube.com/vi/gDRpdBFwg6Y/hqdefault.jpg'">
                        <div class="play-overlay"><div class="play-icon"><i class="fa-solid fa-play" style="margin-left:4px;"></i></div></div>
                    </a>
                    <a href="https://youtu.be/stgEbOmqL1A" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/stgEbOmqL1A/maxresdefault.jpg" alt="動画2" onerror="this.src='https://img.youtube.com/vi/stgEbOmqL1A/hqdefault.jpg'">
                        <div class="play-overlay"><div class="play-icon"><i class="fa-solid fa-play" style="margin-left:4px;"></i></div></div>
                    </a>
                    <a href="https://youtu.be/NfM2x5RqmUI" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/NfM2x5RqmUI/maxresdefault.jpg" alt="動画3" onerror="this.src='https://img.youtube.com/vi/NfM2x5RqmUI/hqdefault.jpg'">
                        <div class="play-overlay"><div class="play-icon"><i class="fa-solid fa-play" style="margin-left:4px;"></i></div></div>
                    </a>
                </div>

                <!-- 20 Prompts Accordion -->
                <h4 style="margin-top:3rem; margin-bottom:1rem; border-bottom:2px solid #f1f5f9; padding-bottom:10px;"><i class="fa-solid fa-bookmark" style="color:#3b82f6;"></i> スポンジのように吸収！20のテクニックリファレンス</h4>

                <details class="prompt-accordion">
                    <summary><div><span class="tag">01:04</span> ①世界観を指定</div> <i class="fa-solid fa-chevron-down"></i></summary>
                    <div class="prompt-content">
                        <strong>解説:</strong> 動画全体の雰囲気や時代背景、場所のコンセプトを明確に。<br>
                        <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=64s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 動画の 01:04 から見る</a>
                    </div>
                </details>
                <details class="prompt-accordion">
                    <summary><div><span class="tag">02:20</span> ②表情を指定</div> <i class="fa-solid fa-chevron-down"></i></summary>
                    <div class="prompt-content">
                        <strong>解説:</strong> 被写体の感情を制御し、「笑顔から驚きへ」など物語性を追加。<br>
                        <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=140s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 動画の 02:20 から見る</a>
                    </div>
                </details>
                <details class="prompt-accordion">
                    <summary><div><span class="tag">05:04</span> ④キャラクターの固定</div> <i class="fa-solid fa-chevron-down"></i></summary>
                    <div class="prompt-content">
                        <strong>解説:</strong> 同一人物を別のシーンでも破綻させずに登場させるテクニック。<br>
                        <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=304s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 動画の 05:04 から見る</a>
                    </div>
                </details>
                <details class="prompt-accordion">
                    <summary><div><span class="tag">09:56</span> ⑧スピードを指定</div> <i class="fa-solid fa-chevron-down"></i></summary>
                    <div class="prompt-content">
                        <strong>解説:</strong> 「スローモーション」や「タイムラプス」など時間の流れを制御。<br>
                        <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=596s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 動画の 09:56 から見る</a>
                    </div>
                </details>
                <details class="prompt-accordion">
                    <summary><div><span class="tag">15:36</span> ⑬カメラワークを指定</div> <i class="fa-solid fa-chevron-down"></i></summary>
                    <div class="prompt-content">
                        <strong>解説:</strong> パンやズームなど視点移動を追加し、映像に躍動感を。<br>
                        <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=936s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 動画の 15:36 から見る</a>
                    </div>
                </details>
                <details class="prompt-accordion">
                    <summary><div><span class="tag">20:24</span> ⑰動きを指定(テキストのみ)</div> <i class="fa-solid fa-chevron-down"></i></summary>
                    <div class="prompt-content">
                        <strong>解説:</strong> 特定の動詞を用いて、複雑な動作をテキストだけで高精度に実現。<br>
                        <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=1224s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 動画の 20:24 から見る</a>
                    </div>
                </details>
            </div>

            <!-- Practical Section -->
            <div class="glass-card">
                <div class="card-header-small"><i class="fa-solid fa-laptop-code" style="color:#10b981;"></i> 実習内容の説明と解説</div>
                
                <div class="explain-box practice">
                    <div class="explain-title"><i class="fa-solid fa-hammer"></i> 知識を「体感」に変える</div>
                    ただ動画を見るだけではカメラの挙動は身につきません。<br>
                    以下の「AIディレクター・シミュレーター」を使って、プロンプトでカメラ（Pan/Zoom）と被写体（Walk/Jump）を指定した際に、画面にどのような視覚効果が生まれるのかを擬似的に体感してください。
                </div>

                <!-- Director Simulator -->
                <div class="simulator-area">
                    <div class="sim-title"><i class="fa-solid fa-clapperboard"></i> AIディレクター・シミュレーター</div>
                    <div class="sim-desc">カメラの動き（撮影者の視点移動）と、被写体のアクションを組み立てて映像演出を作りましょう。</div>
                    
                    <div class="sim-grid">
                        <div class="sim-controls">
                            <div class="ctrl-group">
                                <label class="ctrl-label"><i class="fa-solid fa-camera"></i> カメラワーク</label>
                                <select id="sim-camera" class="ctrl-select">
                                    <option value="cam-none">固定 (Fix / None)</option>
                                    <option value="cam-pan-right">パン右 (Pan Right) - 風景を流す</option>
                                    <option value="cam-pan-left">パン左 (Pan Left) - 被写体を追う</option>
                                    <option value="cam-zoom-in">ズームイン (Zoom In) - 注目させる</option>
                                    <option value="cam-zoom-out">ズームアウト (Zoom Out) - 状況を見せる</option>
                                </select>
                            </div>
                            <div class="ctrl-group">
                                <label class="ctrl-label"><i class="fa-solid fa-person-running"></i> 被写体アクション</label>
                                <select id="sim-action" class="ctrl-select">
                                    <option value="act-none">静止 (Idle)</option>
                                    <option value="act-walk">歩く (Walking)</option>
                                    <option value="act-jump">ジャンプする (Jumping)</option>
                                </select>
                            </div>
                            <button class="sim-btn" onclick="runSimulator()"><i class="fa-solid fa-play"></i> Director, ACTION!</button>
                        </div>
                        
                        <div class="vp-wrapper">
                            <div class="vp-view" id="sim-viewport">
                                <i class="fa-solid fa-city vp-bg" style="left: -10%;"></i>
                                <div class="vp-subject" id="sim-subject">🐕</div>
                                <i class="fa-solid fa-tree vp-bg" style="right: -10%;"></i>
                            </div>
                        </div>
                    </div>
                    
                    <div class="sim-output" id="sim-prompt-out">
                        // シミュレートを実行すると、ここにプロンプト言語が出力されます
                    </div>
                </div>

                <div class="mission-panel" onclick="completeMission(this, 1)">
                    <div class="wax-seal" style="background:#3b82f6; border-color:#1d4ed8;"><i class="fa-solid fa-check-double"></i></div>
                    <div class="ms-icon"><i class="fa-solid fa-clipboard-check"></i></div>
                    <div class="ms-content">
                        <h3>Mission 1: 前半実習クリア</h3>
                        <p>動画を視聴し、シミュレーターを通じてカメラワークとプロンプトの相関関係を体感した。</p>
                    </div>
                    <div class="ms-check"><i class="fa-solid fa-check"></i></div>
                </div>
            </div>
        </section>

        <!-- 3. SECOND HALF -->
        <section id="sec-second" class="course-section">
            <div class="section-header">
                <div class="section-icon ch-second"><i class="fa-regular fa-moon"></i></div>
                <h2 class="section-title">3. 後半：説明と解説</h2>
            </div>

            <div class="glass-card">
                <div class="card-header-small"><i class="fa-solid fa-film" style="color:#8b5cf6;"></i> 再生動画についての説明と解説</div>
                
                <div class="explain-box concept" style="background: #f5f3ff; border-left-color: #8b5cf6;">
                    <div class="explain-title" style="color: #5b21b6;"><i class="fa-solid fa-layer-group"></i> 圧倒的な数の作例に触れる</div>
                    後半のプレイリスト動画群では、特定のツールに縛られず、様々なジャンル・シチュエーションでのプロンプトの記述例が大量に示されます。<br>
                    **良い動画を作るためには、良いプロンプトの「手札」をどれだけ持っているかが勝負**です。映像がどのように言語化されているかに注目して視聴してください。
                </div>

                <div style="text-align:center; padding: 2rem 0;">
                    <a href="https://www.youtube.com/playlist?list=PLoQApr14fceM1VnrF1uTVceOH_56bBha0" target="_blank" class="tab-btn" style="display:inline-block; font-size:1.3rem; padding: 1.2rem 3rem; text-decoration:none; background:linear-gradient(135deg, #8b5cf6, #ec4899); color:#fff; border:none; box-shadow: 0 10px 25px rgba(236, 72, 153, 0.4); border-radius:30px;">
                        <i class="fa-brands fa-youtube"></i> 後半 実習プレイリストを開く
                    </a>
                </div>
            </div>

            <!-- Practical Section -->
            <div class="glass-card">
                <div class="card-header-small"><i class="fa-solid fa-laptop-code" style="color:#10b981;"></i> 実習内容の説明と解説</div>
                
                <div class="explain-box practice">
                    <div class="explain-title"><i class="fa-solid fa-pen-to-square"></i> プロンプト秘伝のタレを調合する</div>
                    動画を見るだけではすぐに忘れてしまいます。実作業を行う際、「あの動画のプロンプトなんだっけ？」と探し回る時間は無駄です。<br>
                    この実習では、**自分用の「プロンプトノート（体系化されたドキュメント）」を作成**し、即座に現場の武器として引き出せるライブラリを構築することが目的です。<br>
                    ツールはNotion、Googleドキュメント等ご自身が使いやすいもので構いません。
                </div>

                <div class="mission-panel" onclick="completeMission(this, 2)">
                    <div class="wax-seal" style="background:#8b5cf6; border-color:#6d28d9;"><i class="fa-solid fa-book-open"></i></div>
                    <div class="ms-icon"><i class="fa-solid fa-book-bookmark"></i></div>
                    <div class="ms-content">
                        <h3>Mission 2: 後半実習クリア</h3>
                        <p>後半のプレイリストを視聴し、動画から得られたノウハウをまとめた「生成AIプロンプトノート」を作成した。</p>
                    </div>
                    <div class="ms-check"><i class="fa-solid fa-check"></i></div>
                </div>
            </div>
        </section>

        <!-- 4. SUMMARY -->
        <section id="sec-summary" class="course-section">
            <div class="section-header">
                <div class="section-icon ch-wrap"><i class="fa-solid fa-flag-checkered"></i></div>
                <h2 class="section-title">4. 今日のまとめ</h2>
            </div>

            <div class="glass-card" style="border: 2px solid var(--accent); background: #f0fdf4;">
                <h3 style="color:var(--accent); font-size:1.5rem; margin-top:0; border-bottom:1px solid #a7f3d0; padding-bottom:1rem; display:flex; align-items:center; gap:10px;">
                    <i class="fa-solid fa-medal"></i> Day 5 コンプリート！
                </h3>
                <p style="font-size: 1.1rem; line-height: 1.8; color: #064e3b; margin-top:1.5rem;">
                    お疲れ様でした！本日は「テキストから動画」を生み出すための本質に迫りました。<br><br>
                    単語を並べるだけでなく、<strong>時間軸（モーション、カメラ、速度）を言語でコントロールする</strong>という新たな思考回路が身についたはずです。<br>
                    作成した「プロンプトノート」は、これからのAI動画制作における最強の相棒となります。明日以降もどんどんアップデートしていきましょう！
                </p>
                <div style="margin-top:2rem; text-align:center;">
                    <button class="sim-btn" style="display:inline-flex; width:auto; border-radius:30px; padding:15px 40px; background:linear-gradient(135deg, #10b981, #059669);" onclick="finishDay()">
                        <i class="fa-solid fa-check-circle"></i> 学習完了を記録してHomeへ
                    </button>
                </div>
            </div>
        </section>

    </div>
    
    <a href="index.html" class="home-btn" title="Back to Home"><i class="fa-solid fa-house"></i></a>

    <script>
        // Scroll Animation
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    
                    // Update Progress Bar based on visible sections
                    const sections = ['sec-goal', 'sec-first', 'sec-second', 'sec-summary'];
                    const idx = sections.indexOf(entry.target.id);
                    if(idx !== -1) {
                        const pct = ((idx + 1) / 4) * 100;
                        document.getElementById('progress-bar').style.width = pct + '%';
                        document.getElementById('progress-percent').innerText = Math.round(pct) + '%';
                    }
                }
            });
        }, { threshold: 0.1 });

        document.querySelectorAll('.course-section').forEach((sec) => {
            observer.observe(sec);
        });

        // Sidebar Navigation highlighting
        function updateNav(el) {
            document.querySelectorAll('.toc-link').forEach(link => link.classList.remove('active'));
            el.classList.add('active');
        }

        // Mission Logic
        function completeMission(el, misId) {
            if(el.classList.contains('completed')) return;
            el.classList.add('completed');
            
            try {
                const audio = new Audio('https://assets.mixkit.co/active_storage/sfx/2869/2869-preview.mp3');
                audio.volume = 0.4;
                audio.play();
            } catch(e) {}
        }
        
        // Simulator Logic
        function runSimulator() {
            const viewport = document.getElementById('sim-viewport');
            const subject = document.getElementById('sim-subject');
            const camSel = document.getElementById('sim-camera');
            const actSel = document.getElementById('sim-action');
            const promptOut = document.getElementById('sim-prompt-out');
            
            // Re-trigger animation by removing classes, forcing reflow
            viewport.className = 'vp-view';
            subject.className = 'vp-subject';
            void viewport.offsetWidth; 
            
            // Apply new classes
            viewport.classList.add(camSel.value);
            subject.classList.add(actSel.value);
            
            // Generate pseudo prompt
            let camText = camSel.options[camSel.selectedIndex].text.split('(')[0].trim();
            let actText = actSel.options[actSel.selectedIndex].text.split('(')[0].trim();
            
            promptOut.innerHTML = `カメラ指示: <span style="color:#fde047;">${camText}</span>, アクション: <span style="color:#fde047;">${actText}</span>, 4k, cinematic video`;
        }

        function finishDay() {
            window.location.href = "index.html";
        }
    </script>
</body>
</html>
