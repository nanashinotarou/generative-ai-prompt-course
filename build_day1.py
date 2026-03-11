import os

html_content = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day 1 | Generative AI & Prompt</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Noto+Sans+JP:wght@400;500;700&family=Teko:wght@500;600;700&family=Fira+Code&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --bg-body: #f8fafc;
            --bg-card: rgba(255, 255, 255, 0.95);
            --text-main: #0f172a;
            --text-sub: #475569;
            --accent: #4f46e5;
            --accent-light: #818cf8;
            --accent-bg: #eef2ff;
            --accent-glow: rgba(79, 70, 229, 0.25);
            --teal: #0d9488;
            --teal-bg: #f0fdfa;
            --danger: #ef4444;
            --warning: #f59e0b;
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
                radial-gradient(ellipse at 10% 20%, rgba(79, 70, 229, 0.08), transparent 40%),
                radial-gradient(ellipse at 90% 80%, rgba(13, 148, 136, 0.08), transparent 40%);
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
        .back-link:hover { color: var(--accent); }

        .progress-container { flex-grow: 1; max-width: 400px; margin: 0 2rem; }
        .progress-text { display: flex; justify-content: space-between; font-size: 0.85rem; font-weight: 700; color: var(--accent); margin-bottom: 6px; }
        .progress-bar-bg { height: 10px; background: #e2e8f0; border-radius: 12px; overflow: hidden; }
        .progress-bar-fill { height: 100%; background: linear-gradient(90deg, var(--accent-light), var(--accent)); width: 0%; border-radius: 12px; transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1); }

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

        /* Tool Boxes */
        .box { padding: 2rem; border-radius: 16px; margin: 2rem 0; position: relative; padding-top: 2.8rem; box-shadow: 0 4px 15px rgba(0,0,0,0.02);}
        .box h4 { margin-top: 0; font-size: 1.25rem; font-weight: 800; }
        .box p, .box ul { margin-bottom: 0; font-size: 1.05rem;}
        
        .box.gemini { background: linear-gradient(135deg, #eff6ff, #dbeafe); border: 1px solid #bfdbfe; }
        .box.gemini::before { content: "\\f544"; font-family: "Font Awesome 6 Free"; font-weight: 900; position: absolute; top: -20px; left: 30px; background: linear-gradient(135deg, #3b82f6, #2563eb); color: #fff; width: 44px; height: 44px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; box-shadow: 0 5px 15px rgba(37, 99, 235, 0.4); }
        .box.gemini h4 { color: #1e40af; }
        
        .box.canva { background: linear-gradient(135deg, #fdf4ff, #fae8ff); border: 1px solid #e9d5ff; }
        .box.canva::before { content: "\\f53f"; font-family: "Font Awesome 6 Free"; font-weight: 900; position: absolute; top: -20px; left: 30px; background: linear-gradient(135deg, #a855f7, #7c3aed); color: #fff; width: 44px; height: 44px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; box-shadow: 0 5px 15px rgba(124, 58, 237, 0.4); }
        .box.canva h4 { color: #6b21a8; }

        .info-box { background: var(--accent-bg); border-left: 5px solid var(--accent); padding: 1.8rem 2rem; border-radius: 0 16px 16px 0; margin: 2rem 0; }
        .info-box h4 { margin: 0 0 0.8rem; color: var(--accent); display: flex; align-items: center; gap: 0.8rem; font-size: 1.2rem; font-weight: 800;}
        .info-box p { margin: 0; color: var(--text-main); line-height: 1.7; font-size: 1.05rem;}

        /* Code Box */
        .code-box { background: #1e293b; color: #e2e8f0; padding: 2.2rem 2.5rem 2rem 2.5rem; border-radius: 16px; font-family: 'Fira Code', 'Consolas', monospace; position: relative; margin: 2.5rem 0; border: 1px solid #334155; font-size: 1rem; line-height: 1.8; box-shadow: 0 15px 35px rgba(0,0,0,0.15);}
        .code-label { position: absolute; top: -14px; left: 24px; background: var(--accent); color: #fff; padding: 4px 16px; font-size: 0.85rem; font-weight: 800; border-radius: 8px; font-family: 'Noto Sans JP', sans-serif; letter-spacing: 0.5px; box-shadow: 0 4px 10px var(--accent-glow);}
        
        .copy-btn { position: absolute; top: 15px; right: 15px; background: rgba(255,255,255,0.1); color: #fff; border: 1px solid rgba(255,255,255,0.2); padding: 8px 16px; border-radius: 8px; cursor: pointer; display: flex; align-items: center; gap: 8px; font-size: 0.9rem; font-weight:bold; transition: all 0.2s; }
        .copy-btn:hover { background: rgba(255,255,255,0.2); border-color: rgba(255,255,255,0.4);}

        /* Buttons */
        .btn { display: inline-flex; align-items: center; gap: 0.6rem; background: var(--accent); color: #fff; border: none; padding: 0.8rem 1.8rem; border-radius: 12px; text-decoration: none; font-size: 1.05rem; font-weight: 800; transition: all 0.2s; cursor: pointer; margin-top: 1rem; box-shadow: 0 6px 15px var(--accent-glow); }
        .btn:hover { background: #4338ca; transform: translateY(-2px); box-shadow: 0 8px 20px var(--accent-glow); }
        .btn-outline { background: #fff; color: var(--accent); border: 2px solid var(--accent); box-shadow: none; }
        .btn-outline:hover { background: var(--accent-bg); border-color: #4338ca; color:#4338ca; transform: none; box-shadow:none;}

        
        /* Highlight box */
        .highlight-box { background: linear-gradient(135deg, #fef3c7, #fde68a); border-radius: 16px; padding: 2rem; margin: 2rem 0; color: #92400e; box-shadow: 0 4px 15px rgba(245, 158, 11, 0.15); border: 1px solid #fcd34d; }
        .highlight-box h3 { font-size: 1.4rem; font-weight: 900; margin-top: 0; border-bottom: 2px dashed #f59e0b; padding-bottom: 10px; margin-bottom: 15px; display:flex; align-items:center; gap:8px;}

        /* Content List Grid */
        .bento-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin: 2.5rem 0;}
        .bento-item { background: #fff; border-radius: 16px; padding: 2rem; position: relative; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.03); border: 1px solid #f1f5f9; transition: transform 0.3s, box-shadow 0.3s;}
        .bento-item:hover { transform: translateY(-5px); box-shadow: 0 12px 25px rgba(0,0,0,0.06); border-color: var(--accent-light);}
        .bento-item h4 { margin: 0 0 1rem; font-size: 1.2rem; color: var(--text-main); display: flex; align-items: center; gap: 0.5rem; font-weight:800;}
        .bento-item p { font-size: 1.05rem; color: #64748b; line-height: 1.6; margin: 0 0 1rem 0; }

        /* Video Grid */
        .video-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.8rem; margin: 2rem 0;}
        .video-thumb { position: relative; border-radius: 16px; overflow: hidden; display: block; border: 4px solid #fff; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08); transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); background: #000;}
        .video-thumb:hover { transform: translateY(-8px); box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15); border-color: var(--accent-light);}
        .video-thumb img { width: 100%; display: block; opacity: 0.85; transition: opacity 0.4s, transform 0.6s;}
        .video-thumb:hover img { opacity: 1; transform: scale(1.06);}
        .play-overlay { position: absolute; inset: 0; background: rgba(0, 0, 0, 0.15); display: flex; align-items: center; justify-content: center; transition: all 0.3s;}
        .video-thumb:hover .play-overlay { background: rgba(79, 70, 229, 0.25);}
        .play-overlay i { color: #fff; font-size: 3.5rem; text-shadow: 0 5px 20px rgba(0, 0, 0, 0.5); transition: transform 0.3s;}
        .video-thumb:hover .play-overlay i { transform: scale(1.15);}

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
        .task-item.completed { background: var(--teal-bg); border-color: #99f6e4; }
        
        .custom-checkbox { width: 32px; height: 32px; border: 3px solid #cbd5e1; border-radius: 10px; display: flex; align-items: center; justify-content: center; transition: all 0.3s; flex-shrink: 0; margin-top: 2px; background: #fff; }
        .task-item.completed .custom-checkbox { background: var(--teal); border-color: var(--teal); }
        .custom-checkbox i { color: #fff; font-size: 16px; opacity: 0; transform: scale(0.5); transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
        .task-item.completed .custom-checkbox i { opacity: 1; transform: scale(1); }
        
        .task-content { flex: 1; }
        .task-content h4 { margin: 0 0 0.5rem; font-size: 1.2rem; color: var(--text-main); font-weight:800; transition:color 0.3s;}
        .task-item.completed .task-content h4 { color: var(--teal); }
        .task-content p { margin: 0; font-size: 1rem; color: var(--text-sub); line-height: 1.6; }

        .btn-sm { padding: 0.6rem 1.2rem; font-size:0.9rem; margin-right: 0.5rem; border-radius: 8px;}

        /* Wax Seal Stamper */
        .wax-seal { position: absolute; top: -20px; right: -20px; width: 140px; height: 140px; background: radial-gradient(circle at 30% 30%, #fca5a5, #ef4444, #991b1b); border-radius: 50%; opacity: 0; transform: scale(3) rotate(-30deg); pointer-events: none; display: flex; align-items: center; justify-content: center; color: rgba(255,255,255,0.9); font-size: 3.5rem; box-shadow: inset 0 0 20px rgba(0,0,0,0.5), 0 10px 30px rgba(0,0,0,0.4); border: 4px solid #b91c1c; z-index: 10;}
        .wax-seal::after { content: ''; position: absolute; inset: 10px; border: 2px dotted rgba(255,255,255,0.4); border-radius: 50%; }
        .mission-area.completed .wax-seal { animation: stampIn 0.7s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards; }
        
        @keyframes stampIn { 
            0% { opacity: 0; transform: scale(3) translateY(-50px) rotate(-30deg); } 
            60% { opacity: 1; transform: scale(0.9) translateY(0) rotate(5deg); } 
            80% { transform: scale(1.1) rotate(-2deg); } 
            100% { opacity: 1; transform: scale(1) rotate(0deg); } 
        }

        /* Confetti Canvas */
        #confetti { position: fixed; inset: 0; pointer-events: none; z-index: 9998; }

        @keyframes fadeInDown { from { opacity: 0; transform: translateY(-30px); } to { opacity: 1; transform: translateY(0); } }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(15px); } to { opacity: 1; transform: translateY(0); } }

        /* Floating Action */
        .home-btn { position: fixed; bottom: 30px; right: 30px; background: linear-gradient(135deg, var(--accent), #3b82f6); color: white; width: 65px; height: 65px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.6rem; box-shadow: 0 10px 30px rgba(79, 70, 229, 0.4); text-decoration: none; transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); z-index: 1000; }
        .home-btn:hover { transform: translateY(-8px) scale(1.05); box-shadow: 0 15px 40px rgba(79, 70, 229, 0.6); color: white; }
    </style>
</head>
<body>

    <canvas id="confetti"></canvas>

    <!-- Header -->
    <header class="fixed-header">
        <a href="index.html" class="back-link"><i class="fa-solid fa-arrow-left"></i> Course Home</a>
        <div class="progress-container">
            <div class="progress-text"><span>Day 1 Progress</span><span id="progress-percent">0%</span></div>
            <div class="progress-bar-bg"><div class="progress-bar-fill" id="progress-bar"></div></div>
        </div>
        <div style="width:100px;"></div>
    </header>

    <div class="container">
        <!-- Hero -->
        <div class="hero">
            <div class="day-badge">DAY 01</div>
            <h1>AI基本操作と画像生成</h1>
            <p>本日の目標：検索型AIの基本操作と画像生成機能の紹介。<br>未来につながる最先端の生成AIに触れ、自分のアイデアを形にする第一歩を踏み出しましょう。</p>
        </div>

        <!-- Premium Tab Navigation -->
        <div class="tab-nav">
            <button class="tab-btn active" onclick="switchTab('tab-goal')"><i class="fa-solid fa-bullseye" style="color:#f59e0b;"></i> コース目標</button>
            <button class="tab-btn" onclick="switchTab('tab-first')"><i class="fa-solid fa-sun" style="color:#3b82f6;"></i> 前半：Gemini実習</button>
            <button class="tab-btn" onclick="switchTab('tab-second')"><i class="fa-solid fa-moon" style="color:#8b5cf6;"></i> 後半：画像生成比較</button>
            <button class="tab-btn" onclick="switchTab('tab-summary')"><i class="fa-solid fa-flag-checkered" style="color:#10b981;"></i> 今日のまとめ</button>
        </div>

        <!-- ==========================================
             TAB 1: COURSE GOALS
        ========================================== -->
        <div id="tab-goal" class="tab-content active">
            <div class="glass-card" style="border-top: 5px solid #f59e0b;">
                <div class="card-header"><i class="fa-solid fa-compass" style="color:#f59e0b; background:#fffbeb;"></i><h2>本日の研修ねらい</h2></div>
                <div class="info-box" style="border-left-color: #f59e0b; background: #fffbeb;">
                    <h4 style="color:#b45309;"><i class="fa-solid fa-road"></i> AIへの「指示力（プロンプト）」を身につける</h4>
                    <p style="color:#92400e;">
                        本日の研修の核心は、単なるツールの使い方を覚えることではなく、<strong>「AIに的確な指示を出し、意図した結果を引き出す力」</strong>を養うことです。<br><br>
                        これから動画作品を制作して世界に発信していくために、テキスト生成AI（Gemini）と画像生成AI（各種ツール）の特性を理解し、思考の壁打ち相手として、そして制作のアシスタントとしてAIを使いこなせる人材になりましょう！
                    </p>
                </div>
            </div>
            
            <div style="text-align:center; margin-top:3rem;">
                <button class="btn" style="padding: 1rem 3rem; font-size:1.2rem; border-radius:30px;" onclick="switchTab('tab-first'); window.scrollTo(0,0);">
                    前半の実習へ進む <i class="fa-solid fa-arrow-right"></i>
                </button>
            </div>
        </div>

        <!-- ==========================================
             TAB 2: FIRST HALF
        ========================================== -->
        <div id="tab-first" class="tab-content">
            <div class="glass-card" style="border-top: 5px solid #3b82f6;">
                <div class="card-header"><i class="fa-brands fa-youtube" style="color:#3b82f6; background:#eff6ff;"></i><h2>前半：説明と解説（動画）</h2></div>
                <p style="font-size:1.1rem; margin-bottom:1.5rem;">生成AIがどのように機能し、どう使えばよいのかを理解するための基本動画です。</p>
                
                <div class="video-grid">
                    <a href="https://youtu.be/WJ1R3D0ntf8" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/WJ1R3D0ntf8/maxresdefault.jpg" alt="動画1" onerror="this.src='https://img.youtube.com/vi/WJ1R3D0ntf8/hqdefault.jpg'">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                    <a href="https://youtu.be/KUNBWh9rprI" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/KUNBWh9rprI/maxresdefault.jpg" alt="動画2" onerror="this.src='https://img.youtube.com/vi/KUNBWh9rprI/hqdefault.jpg'">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                    <a href="https://youtu.be/NBWGnzpeEHk" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/NBWGnzpeEHk/maxresdefault.jpg" alt="動画3" onerror="this.src='https://img.youtube.com/vi/NBWGnzpeEHk/hqdefault.jpg'">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                    <a href="https://youtu.be/o5kXK5JvIt8" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/o5kXK5JvIt8/maxresdefault.jpg" alt="動画4" onerror="this.src='https://img.youtube.com/vi/o5kXK5JvIt8/hqdefault.jpg'">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                </div>
            </div>

                <div class="highlight-box">
                    <h3><i class="fa-solid fa-book-open"></i> 読むだけでわかる！完全解説ダイジェスト</h3>
                    <p style="margin-bottom:0; line-height:1.7;">時間がない方はここをチェック！AIの歴史から将来の影響、そしてGoogleのGeminiの使い方まで、前半4本の動画のエッセンスをまとめました。</p>
                </div>
                <div class="bento-grid">
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-robot" style="color:#3b82f6;"></i> 1. AI（人工知能）とは？</h4>
                        <p>人間のように学習・推論するプログラムです。特化型AIから汎用AIへ進化し、現在はディープラーニング（深層学習）が第3次AIブームを牽引しています。</p>
                    </div>
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-user-tie" style="color:#f59e0b;"></i> 2. 今後の仕事への影響</h4>
                        <p>手順が決まっている定型業務はAIに代替されやすく、コミュニケーション・創造性・柔軟な課題解決が求められる仕事は生き残るとされています。</p>
                    </div>
                    <div class="bento-item" style="grid-column: 1 / -1;">
                        <h4><i class="fa-solid fa-sparkles" style="color:#10b981;"></i> 3. Google Geminiの使い方</h4>
                        <p>文章作成、要約、翻訳、アイデア出しから画像生成までできる無料アシスタント。的確な「プロンプト（指示文）」による対話が精度を高める鍵になります。</p>
                    </div>
                </div>


            <div class="glass-card">
                <div class="card-header"><i class="fa-solid fa-laptop-code" style="color:#10b981; background:#f0fdf4;"></i><h2>前半：実習（Geminiを使ってみよう）</h2></div>
                <p style="font-size:1.1rem;">Geminiの多彩な機能を体験し、プロンプトの基礎を学びます。</p>
                
                <div class="box gemini">
                    <h4>Gemini（テキスト生成AI）にできること</h4>
                    <ul style="padding-left:20px; line-height:2.2;">
                        <li><strong>アイデア出し：</strong>「〇〇についての斬新なアイデアを10個出して」</li>
                        <li><strong>文章作成・要約：</strong>「この長文を重要なポイント3つに絞って箇条書きにして」</li>
                        <li><strong>画像生成：</strong>「未来都市を飛ぶ車の画像を生成して（※具体的な指示がカギ）」</li>
                    </ul>
                </div>

                <div class="code-box">
                    <span class="code-label">プロンプト例（コピーして使ってみよう）</span>
                    <button class="copy-btn" onclick="copyPrompt(this)"><i class="fa-regular fa-copy"></i> Copy</button>
                    <div class="code-text">
<span style="color:#7dd3fc;"># 役割</span>
あなたはプロのAIアシスタントです。

<span style="color:#7dd3fc;"># 命令</span>
「生成AIがもたらす未来」について、小学生でもわかる言葉で300文字程度で説明してください。</div>
                </div>

                <!-- GAMIFIED MISSION -->
                <div class="mission-area" id="mission-group-1">
                    <div class="wax-seal"><i class="fa-solid fa-check"></i></div>
                    <div class="mission-header">
                        <h3><i class="fa-solid fa-clipboard-list"></i> MILESTONE 1: アカウント設定と体感</h3>
                        <p>すべてのチェックを入れるとクリア報酬が発動します！</p>
                    </div>
                    
                    <ul class="task-list">
                        <li class="task-item" onclick="toggleTask('t1_1', this, 1)">
                            <div class="custom-checkbox" id="check_t1_1"><i class="fa-solid fa-check"></i></div>
                            <div class="task-content">
                                <h4>Googleアカウントの準備</h4>
                                <p>ブラウザでGeminiを開き、Googleアカウントでサインインする。</p>
                                <a href="https://gemini.google.com" target="_blank" class="btn btn-sm" onclick="event.stopPropagation();"><i class="fa-solid fa-arrow-up-right-from-square"></i> Geminiを開く</a>
                            </div>
                        </li>
                        <li class="task-item" onclick="toggleTask('t1_2', this, 1)">
                            <div class="custom-checkbox" id="check_t1_2"><i class="fa-solid fa-check"></i></div>
                            <div class="task-content">
                                <h4>NotebookLMへのアクセス</h4>
                                <p>GoogleのAIノートブック機能「NotebookLM」を開いて確認する。</p>
                                <a href="https://notebooklm.google.com/" target="_blank" class="btn btn-sm btn-outline" onclick="event.stopPropagation();"><i class="fa-solid fa-book-open"></i> NotebookLMを開く</a>
                            </div>
                        </li>
                        <li class="task-item" onclick="toggleTask('t1_3', this, 1)">
                            <div class="custom-checkbox" id="check_t1_3"><i class="fa-solid fa-check"></i></div>
                            <div class="task-content">
                                <h4>資料ドキュメントの確認</h4>
                                <p>共有されたドキュメントやプロンプトテキストを開いて確認する。</p>
                                <a href="https://docs.google.com/document/d/16k1obzkjpxKIn6bo5fPYVEEQeJXJvUDkBnPTEJMbnC8/edit?usp=sharing" target="_blank" class="btn btn-sm btn-outline" onclick="event.stopPropagation();"><i class="fa-solid fa-file-lines"></i> 共有Docsを開く</a>
                            </div>
                        </li>
                    </ul>
                </div>

            </div>
            <div style="text-align:center; padding: 2rem 0;">
                <button class="btn" style="padding: 1rem 3rem; font-size:1.2rem; border-radius:30px;" onclick="switchTab('tab-second'); window.scrollTo(0,0);">
                    後半の実習へ進む <i class="fa-solid fa-arrow-right"></i>
                </button>
            </div>
        </div>

        <!-- ==========================================
             TAB 3: SECOND HALF
        ========================================== -->
        <div id="tab-second" class="tab-content">
            <div class="glass-card" style="border-top: 5px solid #8b5cf6;">
                <div class="card-header"><i class="fa-brands fa-youtube" style="color:#8b5cf6; background:#f5f3ff;"></i><h2>後半：動画解説（ファクトチェック＆比較）</h2></div>
                <p style="font-size:1.1rem; margin-bottom:1.5rem;">生成AIの限界を知ること（ファクトチェック）、そして主要な画像生成AIの特徴を把握します。</p>
                
                <div class="video-grid">
                    <a href="https://youtu.be/j9XJJkh2OYM" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/j9XJJkh2OYM/maxresdefault.jpg" alt="動画5" onerror="this.src='https://img.youtube.com/vi/j9XJJkh2OYM/hqdefault.jpg'">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                    <a href="https://youtu.be/xUXyDaMqL60" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/xUXyDaMqL60/maxresdefault.jpg" alt="動画6" onerror="this.src='https://img.youtube.com/vi/xUXyDaMqL60/hqdefault.jpg'">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                    <a href="https://youtu.be/vJLDbXaSKW4" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/vJLDbXaSKW4/maxresdefault.jpg" alt="動画7" onerror="this.src='https://img.youtube.com/vi/vJLDbXaSKW4/hqdefault.jpg'">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                </div>

                <div class="highlight-box" style="background: linear-gradient(135deg, #e0f2fe, #bae6fd); border-color: #7dd3fc; color: #0369a1; margin-top:3rem;">
                    <h3 style="color:#0284c7; border-bottom-color:#38bdf8;"><i class="fa-solid fa-triangle-exclamation"></i> 読むだけでわかる！完全解説ダイジェスト</h3>
                    <p style="margin-bottom:0; line-height:1.7;">生成AIの「弱点」と各画像生成AIの「特徴」を把握することが後半のテーマです。</p>
                </div>
                <div class="bento-grid">
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-mask" style="color:#ef4444;"></i> 1. AIの弱点（ハルシネーション）</h4>
                        <p>AIはもっともらしい嘘をつくことがあります。特に日付や事実関係についてはAIの回答を鵜呑みにせず、必ず一次情報でファクトチェックを行うことが実務における必須スキルです。</p>
                    </div>
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-image" style="color:#8b5cf6;"></i> 2. 画像生成AIの適材適所</h4>
                        <p>機能や得意分野はAIごとに異なります。「NanoBananaPro」はリアル系、「Seedream4.0」はテキスト再現、「Midjourney」はアート性、「Adobe Firefly」は商用利用など、目的に応じたツール選択が重要です。</p>
                    </div>
                </div>


                <div class="info-box" style="border-left-color: #ef4444; background: #fef2f2;">
                    <h4 style="color:#b91c1c;"><i class="fa-solid fa-triangle-exclamation"></i> ハルシネーションとファクトチェック（動画⑤）</h4>
                    <p style="color:#7f1d1d;">生成AIは「もっともらしい嘘（ハルシネーション）」をつくことがあります。特に、数字、日付、人名には要注意です。AIの出力は必ず公式サイト等の一次情報で裏付け（ファクトチェック）を取る習慣をつけましょう。</p>
                </div>

                <h3 style="font-size: 1.5rem; margin-top:3rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;"><i class="fa-solid fa-images" style="color:#8b5cf6;"></i> 4つの画像生成AI 徹底比較</h3>
                
                <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 2rem;">
                    <div class="box canva">
                        <h4>① NanoBanana Pro</h4>
                        <ul style="padding-left:20px; line-height:2;">
                            <li>日本語プロンプトに対応</li>
                            <li>日本人の顔や日本的なシーンが得意</li>
                            <li>リアル系の画像生成に圧倒的に強い</li>
                        </ul>
                    </div>
                    <div class="box canva">
                        <h4>② Seedream 4.0</h4>
                        <ul style="padding-left:20px; line-height:2;">
                            <li>Google開発の高品質生成モデル(Gemini等に搭載)</li>
                            <li>テキストの正確な埋め込み（看板の文字等）が得意</li>
                            <li>プロンプトの意図を正確に反映する力が強い</li>
                        </ul>
                    </div>
                    <div class="box canva">
                        <h4>③ Midjourney</h4>
                        <ul style="padding-left:20px; line-height:2;">
                            <li>アート性・美しさはトップクラス</li>
                            <li>幻想的・映画的な美しいライティングが得意</li>
                            <li>Discord/Webから利用。有料のみ</li>
                        </ul>
                    </div>
                    <div class="box canva">
                        <h4>④ Adobe Firefly</h4>
                        <ul style="padding-left:20px; line-height:2;">
                            <li>商用利用に最も安全（クリーンな学習データ）</li>
                            <li>Photoshopとの連携による部分修正・拡張に強い</li>
                            <li>合成や被写体の摘出が最も得意</li>
                        </ul>
                    </div>
                </div>

                <div class="highlight-box" style="background: linear-gradient(135deg, #e0f2fe, #bae6fd); border-color: #7dd3fc; color: #0369a1; margin-top:3rem;">
                    <h3 style="color:#0284c7; border-bottom-color:#38bdf8;"><i class="fa-solid fa-triangle-exclamation"></i> 読むだけでわかる！完全解説ダイジェスト</h3>
                    <p style="margin-bottom:0; line-height:1.7;">生成AIの「弱点」と各画像生成AIの「特徴」を把握することが後半のテーマです。</p>
                </div>
                <div class="bento-grid">
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-mask" style="color:#ef4444;"></i> 1. AIの弱点（ハルシネーション）</h4>
                        <p>AIはもっともらしい嘘をつくことがあります。特に日付や事実関係についてはAIの回答を鵜呑みにせず、必ず一次情報でファクトチェックを行うことが実務における必須スキルです。</p>
                    </div>
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-image" style="color:#8b5cf6;"></i> 2. 画像生成AIの適材適所</h4>
                        <p>機能や得意分野はAIごとに異なります。「NanoBananaPro」はリアル系、「Seedream4.0」はテキスト再現、「Midjourney」はアート性、「Adobe Firefly」は商用利用など、目的に応じたツール選択が重要です。</p>
                    </div>
                </div>

            </div>

            <!-- GAMIFIED MISSION -->
            <div class="glass-card">
                <div class="card-header"><i class="fa-solid fa-pen-ruler" style="color:#10b981; background:#f0fdf4;"></i><h2>後半：実習（プロンプトノート作成）</h2></div>
                <p style="font-size:1.1rem;">各AIの特徴を自分なりにまとめ、すぐに武器として使える「魔法の書」を作ります。</p>

                <div class="mission-area" id="mission-group-2">
                    <div class="wax-seal" style="background: radial-gradient(circle at 30% 30%, #c4b5fd, #8b5cf6, #5b21b6); border-color:#4c1d95;"><i class="fa-solid fa-stamp"></i></div>
                    <div class="mission-header">
                        <h3><i class="fa-solid fa-book-open-reader"></i> MILESTONE 2: 学習ノート完成</h3>
                        <p>知識を文字に起こし、定着させよう！</p>
                    </div>
                    
                    <ul class="task-list">
                        <li class="task-item" onclick="toggleTask('t2_1', this, 2)">
                            <div class="custom-checkbox" id="check_t2_1"><i class="fa-solid fa-check"></i></div>
                            <div class="task-content">
                                <h4>各AIの特徴ノート作成</h4>
                                <p>指定のドキュメントからテキストをコピーし、1つのプロンプトごとに4つのAIの特徴をまとめる（Canva, スライド等を使用可）。</p>
                            </div>
                        </li>
                        <li class="task-item" onclick="toggleTask('t2_2', this, 2)">
                            <div class="custom-checkbox" id="check_t2_2"><i class="fa-solid fa-check"></i></div>
                            <div class="task-content">
                                <h4>得意分野の評価まとめ</h4>
                                <p>①商品紹介 ②資料作成 ③実写広告 ④煽り画角 ⑤MV原型 ⑥大量生成 ⑦合成・摘出<br>の7項目について、どのAIがオススメか1ページにまとめる。</p>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>

            <div style="text-align:center; padding: 2rem 0;">
                <button class="btn" style="padding: 1rem 3rem; font-size:1.2rem; background:#10b981; border-radius:30px;" onclick="switchTab('tab-summary'); window.scrollTo(0,0);">
                    本日のまとめを見る <i class="fa-solid fa-flag-checkered"></i>
                </button>
            </div>
        </div>

        <!-- ==========================================
             TAB 4: SUMMARY
        ========================================== -->
        <div id="tab-summary" class="tab-content">
            <div class="glass-card" style="border: 2px solid #10b981; background: #f0fdf4;">
                <h3 style="color:#10b981; font-size:1.8rem; margin-top:0; border-bottom:2px solid #a7f3d0; padding-bottom:1.5rem; display:flex; align-items:center; justify-content:center; gap:15px; font-weight:900;">
                    <i class="fa-solid fa-medal" style="font-size:2.5rem;"></i> Day 1 全行程コンプリート！
                </h3>
                <p style="font-size: 1.25rem; line-height: 2; color: #064e3b; margin-top:2rem; text-align:center; padding: 0 2rem;">
                    お疲れ様でした！本日は<strong>「テキスト生成AI（Gemini）」</strong>による思考の拡張と、<br>
                    <strong>「画像生成AI 4天王」</strong>それぞれの得意分野の違いについて学びました。<br><br>
                    プロンプトは、AIという強力な魔法使いを動かすための<strong>「呪文」</strong>です。<br>
                    今日作成したノートをもとに、明日以降も様々な魔法を実践して使いこなしていきましょう！
                </p>
                
                <div style="margin-top:3rem; text-align:center;">
                    <button class="btn" style="padding: 1.2rem 4rem; font-size:1.3rem; background:linear-gradient(135deg, #10b981, #059669); border-radius:50px; box-shadow: 0 10px 25px rgba(16, 185, 129, 0.4);" onclick="window.location.href='index.html'">
                        <i class="fa-solid fa-house"></i> 学習完了を記録してHomeへ戻る
                    </button>
                </div>
            </div>
        </div>
    </div>

    <a href="index.html" class="home-btn" title="Back to Home"><i class="fa-solid fa-house"></i></a>

    <!-- Scripts -->
    <script>
        // --- Tab Switching Navigation ---
        function switchTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
            
            document.getElementById(tabId).classList.add('active');
            
            // Find the button that corresponds to the tabId and activate it
            const buttons = document.querySelectorAll('.tab-btn');
            for(let i=0; i<buttons.length; i++){
                if(buttons[i].getAttribute('onclick').includes(tabId)){
                    buttons[i].classList.add('active');
                }
            }
        }

        // --- Copy Utility ---
        function copyPrompt(btn) {
            const pre = btn.nextElementSibling.innerText;
            navigator.clipboard.writeText(pre).then(() => {
                const orig = btn.innerHTML;
                btn.innerHTML = '<i class="fa-solid fa-check"></i> Copied!';
                btn.style.background = '#059669'; btn.style.color = '#fff'; btn.style.borderColor = '#059669';
                setTimeout(() => { btn.innerHTML = orig; btn.style.background = ''; btn.style.color = ''; btn.style.borderColor = ''; }, 2000);
            });
        }

        // --- Gamification Logic ---
        // Group tracking
        const missionGroups = {
            1: ['t1_1', 't1_2', 't1_3'],
            2: ['t2_1', 't2_2']
        };
        const allTasks = [...missionGroups[1], ...missionGroups[2]];
        let state = {};

        window.addEventListener('DOMContentLoaded', () => {
            const saved = localStorage.getItem('day1_premium_prog');
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
            localStorage.setItem('day1_premium_prog', JSON.stringify(state));
            
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
                        // Play sound and explode confetti only if triggered actively by click
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
            const pct = Math.round((count / allTasks.length) * 100);
            document.getElementById('progress-bar').style.width = pct + '%';
            document.getElementById('progress-percent').innerText = pct + '%';
        }

        function playStampSound() {
            try {
                const audio = new Audio('https://assets.mixkit.co/active_storage/sfx/2869/2869-preview.mp3');
                audio.volume = 0.5; audio.play();
            } catch(e) {}
        }

        // --- Confetti Engine ---
        function fireConfetti() {
            const c = document.getElementById('confetti');
            const ctx = c.getContext('2d');
            c.width = window.innerWidth; c.height = window.innerHeight;
            const pieces = [], colors = ['#818cf8', '#34d399', '#fbbf24', '#f87171', '#a78bfa', '#38bdf8'];
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

with open("vol01-1_ai_start.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated vol01-1_ai_start.html completely.")
