<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day 1 | AI Basics & Image Generation</title>
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

        /* Navigation Sidebar */
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

        /* Components */
        .glass-card { background: var(--bg-card); border: 1px solid rgba(0,0,0,0.05); border-radius: var(--radius); padding: 2.5rem; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.02); transition: transform 0.3s, box-shadow 0.3s; }
        .glass-card:hover { transform: translateY(-2px); box-shadow: 0 15px 35px rgba(0,0,0,0.06); }
        .card-header-small { display: flex; align-items: center; gap: 10px; margin-bottom: 1.5rem; border-bottom: 1px solid #f1f5f9; padding-bottom: 1rem; font-weight: 700; font-size: 1.3rem;}
        
        .explain-box { background: #eff6ff; border-left: 4px solid var(--clickable); padding: 1.5rem; border-radius: 0 12px 12px 0; margin-bottom: 2rem; line-height: 1.7; position: relative;}
        .explain-title { font-weight: 800; color: #1e3a8a; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 8px;}
        .explain-box.concept { background: #fdf4ff; border-left-color: #d946ef; }
        .explain-box.concept .explain-title { color: #86198f; }
        .explain-box.practice { background: #f0fdf4; border-left-color: #10b981; }
        .explain-box.practice .explain-title { color: #065f46; }

        .hero { text-align: center; margin-bottom: 4rem; }
        .day-badge { background: var(--text-main); color: #fff; padding: 0.5rem 2rem; border-radius: 30px; font-family: 'Teko', sans-serif; font-size: 1.5rem; letter-spacing: 2px; display: inline-block; margin-bottom: 1.5rem; }
        .hero h1 { font-size: clamp(2.5rem, 4vw, 3.5rem); margin: 0 0 1rem; font-weight: 900; letter-spacing: -1.5px; line-height: 1.2; }

        .video-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin-top: 1rem; margin-bottom: 2rem;}
        .video-thumb { position: relative; border-radius: 16px; overflow: hidden; display: block; border: 1px solid rgba(0,0,0,0.1); box-shadow: 0 10px 25px rgba(0,0,0,0.08); transition: all 0.3s; background: #000;}
        .video-thumb:hover { transform: translateY(-5px); box-shadow: 0 20px 40px rgba(0,0,0,0.15); border-color: var(--clickable);}
        .video-thumb img { width: 100%; display: block; opacity: 0.9; transition: opacity 0.3s, transform 0.5s;}
        .video-thumb:hover img { opacity: 1; transform: scale(1.05);}
        .play-overlay { position: absolute; inset: 0; background: rgba(0,0,0,0.2); display: flex; align-items: center; justify-content: center; transition: all 0.3s;}
        .video-thumb:hover .play-overlay { background: rgba(14, 165, 233, 0.3);}
        .play-icon { width: 60px; height: 60px; background: rgba(255,255,255,0.9); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #ef4444; font-size: 1.8rem; box-shadow: 0 10px 20px rgba(0,0,0,0.2); transition: transform 0.3s;}
        .video-thumb:hover .play-icon { transform: scale(1.1); background: #fff; color: #b91c1c; }

        /* Simulator Styles for this Specific Day */
        .simulator-area { background: #1e293b; border-radius: 16px; padding: 2.5rem; color: #f8fafc; margin: 2.5rem 0; box-shadow: 0 20px 40px rgba(0,0,0,0.2); border: 1px solid #334155; }
        .sim-title { font-size: 1.5rem; font-weight: 800; margin-top: 0; margin-bottom: 0.5rem; color: #a78bfa; display: flex; align-items: center; gap: 12px; }
        .sim-desc { color: #94a3b8; font-size: 0.95rem; margin-bottom: 2rem; border-bottom: 1px solid #334155; padding-bottom: 1rem;}
        
        .chat-ui { background: #0f172a; border-radius: 12px; overflow: hidden; border: 1px solid #334155;}
        .chat-messages { height: 250px; padding: 15px; overflow-y: auto; display: flex; flex-direction: column; gap: 10px; }
        .msg { max-width: 80%; padding: 12px 16px; border-radius: 12px; font-size: 0.95rem; line-height: 1.4; animation: fadeIn 0.3s ease; }
        .msg-user { background: #38bdf8; color: #fff; align-self: flex-end; border-bottom-right-radius: 2px;}
        .msg-ai { background: #1e293b; color: #e2e8f0; align-self: flex-start; border-bottom-left-radius: 2px; border: 1px solid #334155; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        .chat-input-area { background: #1e293b; padding: 15px; border-top: 1px solid #334155; display: flex; gap: 10px;}
        .chat-select { flex-grow: 1; background: #0f172a; color: #fff; border: 1px solid #475569; padding: 10px; border-radius: 8px; outline: none;}
        .chat-btn { background: #8b5cf6; color: white; border: none; padding: 0 20px; border-radius: 8px; cursor: pointer; font-weight: bold; transition: background 0.2s; }
        .chat-btn:hover { background: #7c3aed; }
        
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

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
        
        @keyframes fadeInUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
        @keyframes stampIn { 0% { opacity: 0; transform: scale(3) translateY(-50px) rotate(-20deg); } 60% { opacity: 1; transform: scale(0.9) translateY(0) rotate(5deg); } 80% { transform: scale(1.1) rotate(-2deg); } 100% { opacity: 1; transform: scale(1) rotate(0deg); } }
        
        .home-btn { position: fixed; bottom: 30px; right: 30px; background: var(--text-main); color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; box-shadow: 0 10px 25px rgba(0,0,0,0.3); text-decoration: none; transition: all 0.3s; z-index: 1000; border: 2px solid rgba(255,255,255,0.2); }
        .home-btn:hover { transform: translateY(-5px) scale(1.05); background: var(--clickable); color: white; }
        
        .btn-link { display:inline-flex; align-items:center; gap:8px; padding:12px 24px; background:linear-gradient(135deg, var(--clickable), #3b82f6); color:#fff; text-decoration:none; border-radius:30px; font-weight:700; transition:all 0.3s; box-shadow:0 6px 15px rgba(14,165,233,0.3); margin:10px 10px 10px 0;}
        .btn-link:hover { transform:translateY(-2px); box-shadow:0 10px 20px rgba(14,165,233,0.4);}
    </style>
</head>
<body>
    <header class="fixed-header">
        <a href="index.html" class="back-link"><i class="fa-solid fa-arrow-left"></i> Course Home</a>
        <div class="progress-container">
            <div class="progress-text"><span>Day 1 Progress</span><span id="progress-percent">0%</span></div>
            <div class="progress-bar-bg"><div class="progress-bar-fill" id="progress-bar"></div></div>
        </div>
        <div style="width:100px;"></div>
    </header>

    <div class="toc-sidebar">
        <div class="toc-title">IN THIS LESSON</div>
        <nav style="display:flex; flex-direction:column; gap:8px;">
            <a href="#sec-goal" class="toc-link" onclick="updateNav(this)"><i class="fa-solid fa-bullseye" style="color:#f59e0b"></i> 本日の目標</a>
            <a href="#sec-first" class="toc-link" onclick="updateNav(this)"><i class="fa-solid fa-sun" style="color:#3b82f6"></i> 前半：検索型AI</a>
            <a href="#sec-second" class="toc-link" onclick="updateNav(this)"><i class="fa-solid fa-moon" style="color:#8b5cf6"></i> 後半：画像生成AI</a>
            <a href="#sec-summary" class="toc-link" onclick="updateNav(this)"><i class="fa-solid fa-flag-checkered" style="color:#10b981"></i> 今日のまとめ</a>
        </nav>
    </div>

    <div class="container">
        <!-- HERO -->
        <div class="hero course-section visible" style="margin-top: 2rem;">
            <div class="day-badge">DAY 01</div>
            <h1>AI基本操作と<br>画像生成</h1>
        </div>

        <!-- 1. COURSE GOAL -->
        <section id="sec-goal" class="course-section">
            <div class="section-header">
                <div class="section-icon ch-goal"><i class="fa-solid fa-bullseye"></i></div>
                <h2 class="section-title">1. 今日のコース目標</h2>
            </div>
            
            <div class="glass-card">
                <div class="explain-box concept" style="background: #fffbef; border-left-color: #f59e0b; font-size: 1.1rem;">
                    <div class="explain-title" style="color:#b45309; font-size:1.3rem;"><i class="fa-solid fa-compass"></i> 最初の一歩を確実に踏み出す</div>
                    本日の研修テーマは、<b>「検索型AIの基本操作と画像生成機能の紹介」</b>です。<br><br>
                    最終的には「プロンプトを中心に作成した動画作品を3本以上作成して公開する」という大目標に向かいますが、まずは**生成AIを触ることへのハードルを下げ、基本的なテキスト指示とプロンプトで画像を生成できる状態**を目指します。
                </div>
            </div>
        </section>

        <!-- 2. FIRST HALF -->
        <section id="sec-first" class="course-section">
            <div class="section-header">
                <div class="section-icon ch-first"><i class="fa-regular fa-sun"></i></div>
                <h2 class="section-title">2. 前半：検索型AIの基本</h2>
            </div>

            <div class="glass-card">
                <div class="card-header-small"><i class="fa-solid fa-film" style="color:#3b82f6;"></i> 再生動画についての説明と解説</div>
                
                <div class="explain-box concept">
                    <div class="explain-title"><i class="fa-solid fa-magnifying-glass"></i> ただの検索を超えた「対話」</div>
                    Google Geminiに代表される検索型AIは、単なる検索エンジンではありません。<br>
                    文書の要約、アイデア出し、さらにはコード生成まで、人間と対話しながら課題を解決するパートナーです。動画を通してGeminiのポテンシャルを確認しましょう。
                </div>

                <div class="video-grid">
                    <a href="https://youtu.be/WJ1R3D0ntf8" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/WJ1R3D0ntf8/maxresdefault.jpg" alt="動画1" onerror="this.src='https://img.youtube.com/vi/WJ1R3D0ntf8/hqdefault.jpg'">
                        <div class="play-overlay"><div class="play-icon"><i class="fa-solid fa-play" style="margin-left:4px;"></i></div></div>
                    </a>
                    <a href="https://youtu.be/KUNBWh9rprI" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/KUNBWh9rprI/maxresdefault.jpg" alt="動画2" onerror="this.src='https://img.youtube.com/vi/KUNBWh9rprI/hqdefault.jpg'">
                        <div class="play-overlay"><div class="play-icon"><i class="fa-solid fa-play" style="margin-left:4px;"></i></div></div>
                    </a>
                    <a href="https://youtu.be/NBWGnzpeEHk" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/NBWGnzpeEHk/maxresdefault.jpg" alt="動画3" onerror="this.src='https://img.youtube.com/vi/NBWGnzpeEHk/hqdefault.jpg'">
                        <div class="play-overlay"><div class="play-icon"><i class="fa-solid fa-play" style="margin-left:4px;"></i></div></div>
                    </a>
                    <a href="https://youtu.be/o5kXK5JvIt8" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/o5kXK5JvIt8/maxresdefault.jpg" alt="動画4" onerror="this.src='https://img.youtube.com/vi/o5kXK5JvIt8/hqdefault.jpg'">
                        <div class="play-overlay"><div class="play-icon"><i class="fa-solid fa-play" style="margin-left:4px;"></i></div></div>
                    </a>
                </div>
            </div>

            <!-- Practical Section -->
            <div class="glass-card">
                <div class="card-header-small"><i class="fa-solid fa-laptop-code" style="color:#10b981;"></i> 実習内容の説明と解説</div>
                
                <div class="explain-box practice">
                    <div class="explain-title"><i class="fa-brands fa-google"></i> 実感する・Geminiを使ってみよう</div>
                    動画を一通り見た後は、実際にGoogleのアカウントを使ってGeminiにログインし、自分自身の手で対話を始めてみましょう。<br>
                    また、Googleドキュメントに添付された資料を用いながら進めてください。
                </div>
                
                <div>
                    <a href="https://gemini.google.com/" target="_blank" class="btn-link"><i class="fa-brands fa-google"></i> Geminiを開く</a>
                    <a href="https://notebooklm.google.com/" target="_blank" class="btn-link" style="background:linear-gradient(135deg, #10b981, #059669);"><i class="fa-solid fa-book"></i> NotebookLMを開く</a>
                    <a href="https://docs.google.com/document/d/16k1obzkjpxKIn6bo5fPYVEEQeJXJvUDkBnPTEJMbnC8/edit?usp=sharing" target="_blank" class="btn-link" style="background:linear-gradient(135deg, #8b5cf6, #7c3aed);"><i class="fa-solid fa-file-word"></i> 共有ドキュメント</a>
                </div>

                <div class="simulator-area" style="background:#1e1e2f; border:none; box-shadow:none; margin-top:20px;">
                    <div class="sim-title" style="color:#a78bfa;"><i class="fa-solid fa-robot"></i> 疑似体験: 生成AIとのチャット感覚</div>
                    <div class="sim-desc">生成AIに投げる質問によって、返ってくる答えが変わることを体感しましょう。</div>
                    <div class="chat-ui">
                        <div class="chat-messages" id="chat-msgs">
                            <div class="msg msg-ai">こんにちは！何について質問しますか？</div>
                        </div>
                        <div class="chat-input-area">
                            <select id="chat-choice" class="chat-select">
                                <option value="q1">短く質問：「リンゴについて教えて」</option>
                                <option value="q2">具体的に質問：「リンゴの栄養素と、疲労回復に効果的な理由を小中学生向けに教えて」</option>
                            </select>
                            <button class="chat-btn" onclick="sendSimChat()"><i class="fa-solid fa-paper-plane"></i></button>
                        </div>
                    </div>
                </div>

                <div class="mission-panel" onclick="completeMission(this, 1)">
                    <div class="wax-seal" style="background:#3b82f6; border-color:#1d4ed8;"><i class="fa-solid fa-check-double"></i></div>
                    <div class="ms-icon"><i class="fa-solid fa-user-check"></i></div>
                    <div class="ms-content">
                        <h3>Mission 1: Gemini体験クリア</h3>
                        <p>Googleアカウントでログインし、検索型AIへの「具体的な質問出し」を試行した。</p>
                    </div>
                    <div class="ms-check"><i class="fa-solid fa-check"></i></div>
                </div>
            </div>
        </section>

        <!-- 3. SECOND HALF -->
        <section id="sec-second" class="course-section">
            <div class="section-header">
                <div class="section-icon ch-second"><i class="fa-regular fa-moon"></i></div>
                <h2 class="section-title">3. 後半：生成AIツールの多様性</h2>
            </div>

            <div class="glass-card">
                <div class="card-header-small"><i class="fa-solid fa-film" style="color:#8b5cf6;"></i> 再生動画についての説明と解説</div>
                
                <div class="explain-box concept" style="background: #f5f3ff; border-left-color: #8b5cf6;">
                    <div class="explain-title" style="color: #5b21b6;"><i class="fa-solid fa-wand-magic-sparkles"></i> 4つの生成AIの特徴を知る</div>
                    後半で紹介される「NanoBanana」「Seedreem4.0」「Midjourney」「Adobe Firefly」は全て画像生成が可能なAIですが、得意なこと・苦手なことが異なります。<br>
                    目的に応じて「どのツールを使うべきか（ツール選定能力）」を養うための動画群です。
                </div>

                <div class="video-grid">
                    <a href="https://youtu.be/j9XJJkh2OYM" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/j9XJJkh2OYM/maxresdefault.jpg" alt="後半動画1" onerror="this.src='https://img.youtube.com/vi/j9XJJkh2OYM/hqdefault.jpg'">
                        <div class="play-overlay"><div class="play-icon"><i class="fa-solid fa-play" style="margin-left:4px;"></i></div></div>
                    </a>
                    <a href="https://youtu.be/xUXyDaMqL60" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/xUXyDaMqL60/maxresdefault.jpg" alt="後半動画2" onerror="this.src='https://img.youtube.com/vi/xUXyDaMqL60/hqdefault.jpg'">
                        <div class="play-overlay"><div class="play-icon"><i class="fa-solid fa-play" style="margin-left:4px;"></i></div></div>
                    </a>
                    <a href="https://youtu.be/vJLDbXaSKW4" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/vJLDbXaSKW4/maxresdefault.jpg" alt="後半動画3" onerror="this.src='https://img.youtube.com/vi/vJLDbXaSKW4/hqdefault.jpg'">
                        <div class="play-overlay"><div class="play-icon"><i class="fa-solid fa-play" style="margin-left:4px;"></i></div></div>
                    </a>
                </div>
            </div>

            <!-- Practical Section -->
            <div class="glass-card">
                <div class="card-header-small"><i class="fa-solid fa-laptop-code" style="color:#10b981;"></i> 実習内容の説明と解説</div>
                
                <div class="explain-box practice">
                    <div class="explain-title"><i class="fa-solid fa-book-open"></i> プロンプト学習用のノート作成</div>
                    前半で共有したドキュメント記載の全６つのプロンプトを用いて、4つのAIそれぞれの生成結果を確認しましょう。<br>
                    CanvaやNotion等を利用し、**「商品紹介にはこれが合う」「実写作成ならこれ」といった自分なりの考察ノート**を作成してください。
                </div>

                <div class="mission-panel" onclick="completeMission(this, 2)">
                    <div class="wax-seal" style="background:#8b5cf6; border-color:#6d28d9;"><i class="fa-solid fa-book-open"></i></div>
                    <div class="ms-icon"><i class="fa-solid fa-pen-fancy"></i></div>
                    <div class="ms-content">
                        <h3>Mission 2: ツール比較ノート完成</h3>
                        <p>4つのツールの違いを分析し、最適な用途（商品紹介、資料作成等）を記載したノートを作成した。</p>
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
                    <i class="fa-solid fa-medal"></i> Day 1 コンプリート！
                </h3>
                <p style="font-size: 1.1rem; line-height: 1.8; color: #064e3b; margin-top:1.5rem;">
                    お疲れ様でした！本日はAI時代において必要不可欠な「ツールとの対話」と「画像生成AIの特徴把握」を行いました。<br><br>
                    これからは**「目的に合わせてAIを使い分ける」スキル**が非常に重要になってきます。本日作成した比較ノートは、今後の動画制作やビジネス活用における大きな武器となるでしょう！
                </p>
                <div style="margin-top:2rem; text-align:center;">
                    <button class="btn-link" style="border:none; padding:15px 40px; background:linear-gradient(135deg, #10b981, #059669); font-size:1.1rem; cursor:pointer;" onclick="finishDay()">
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
                audio.volume = 0.4; audio.play();
            } catch(e) {}
        }
        
        // Chat Simulator Logic
        function sendSimChat() {
            const val = document.getElementById('chat-choice').value;
            const msgs = document.getElementById('chat-msgs');
            
            let userTxt = val === 'q1' ? "リンゴについて教えて" : "リンゴの栄養素と、疲労回復に効果的な理由を小中学生向けに教えて";
            msgs.innerHTML += `<div class="msg msg-user">${userTxt}</div>`;
            msgs.scrollTop = msgs.scrollHeight;
            
            setTimeout(() => {
                let aiTxt = val === 'q1' 
                    ? "リンゴ（林檎）はバラ科リンゴ属の落葉高木樹、およびその果実です。世界中で栽培されています..."
                    : "こんにちは！リンゴには「クエン酸」や「リンゴ酸」という栄養素がたっぷり入っているんだ。これが体の疲れをとってくれる秘密のエナジー源だよ！スナック菓子のかわりに食べると元気になるよ！";
                msgs.innerHTML += `<div class="msg msg-ai">${aiTxt}</div>`;
                msgs.scrollTop = msgs.scrollHeight;
            }, 800);
        }

        function finishDay() {
            window.location.href = "index.html";
        }
    </script>
</body>
</html>
