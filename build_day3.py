<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day 3 | Prompt Instructions & Markdown</title>
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
            --prompt-gray: #334155;
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
                radial-gradient(circle at 10% 20%, rgba(51, 65, 85, 0.05) 0%, transparent 40%),
                radial-gradient(circle at 90% 80%, rgba(139, 92, 246, 0.05) 0%, transparent 40%);
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
        .progress-bar-fill { height: 100%; background: linear-gradient(90deg, var(--prompt-gray), var(--purple)); width: 0%; border-radius: 12px; transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1); }

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
        .ch-first { background: linear-gradient(135deg, #334155, #1e293b); }
        .ch-second { background: linear-gradient(135deg, #8b5cf6, #7c3aed); }
        .ch-wrap { background: linear-gradient(135deg, #10b981, #059669); }

        /* Components */
        .glass-card { background: var(--bg-card); border: 1px solid rgba(0,0,0,0.05); border-radius: var(--radius); padding: 2.5rem; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.02); transition: transform 0.3s, box-shadow 0.3s; }
        .glass-card:hover { transform: translateY(-2px); box-shadow: 0 15px 35px rgba(0,0,0,0.06); }
        .card-header-small { display: flex; align-items: center; gap: 10px; margin-bottom: 1.5rem; border-bottom: 1px solid #f1f5f9; padding-bottom: 1rem; font-weight: 700; font-size: 1.3rem;}
        
        .explain-box { background: #eff6ff; border-left: 4px solid var(--clickable); padding: 1.5rem; border-radius: 0 12px 12px 0; margin-bottom: 2rem; line-height: 1.7; position: relative;}
        .explain-title { font-weight: 800; color: #1e3a8a; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 8px;}
        .explain-box.concept { background: #f8fafc; border-left-color: #64748b; }
        .explain-box.concept .explain-title { color: #334155; }
        .explain-box.practice { background: #f0fdf4; border-left-color: #10b981; }
        .explain-box.practice .explain-title { color: #065f46; }

        .hero { text-align: center; margin-bottom: 4rem; }
        .day-badge { background: var(--text-main); color: #fff; padding: 0.5rem 2rem; border-radius: 30px; font-family: 'Teko', sans-serif; font-size: 1.5rem; letter-spacing: 2px; display: inline-block; margin-bottom: 1.5rem; }
        .hero h1 { font-size: clamp(2.5rem, 4vw, 3.5rem); margin: 0 0 1rem; font-weight: 900; letter-spacing: -1.5px; line-height: 1.2; }

        .video-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin-top: 1rem; margin-bottom: 2rem;}
        .video-thumb { position: relative; border-radius: 16px; overflow: hidden; display: block; border: 1px solid rgba(0,0,0,0.1); box-shadow: 0 10px 25px rgba(0,0,0,0.08); transition: all 0.3s; background: #000;}
        .video-thumb:hover { transform: translateY(-5px); box-shadow: 0 20px 40px rgba(0,0,0,0.15); border-color: var(--prompt-gray);}
        .video-thumb img { width: 100%; display: block; opacity: 0.9; transition: opacity 0.3s, transform 0.5s;}
        .video-thumb:hover img { opacity: 1; transform: scale(1.05);}
        .play-overlay { position: absolute; inset: 0; background: rgba(0,0,0,0.2); display: flex; align-items: center; justify-content: center; transition: all 0.3s;}
        .video-thumb:hover .play-overlay { background: rgba(51, 65, 85, 0.3);}
        .play-icon { width: 60px; height: 60px; background: rgba(255,255,255,0.9); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #ef4444; font-size: 1.8rem; box-shadow: 0 10px 20px rgba(0,0,0,0.2); transition: transform 0.3s;}
        .video-thumb:hover .play-icon { transform: scale(1.1); background: #fff; color: #b91c1c; }

        /* Markdown Simulator Styles */
        .simulator-area { background: #1e1e2f; border-radius: 16px; padding: 2.5rem; color: #f8fafc; margin: 2.5rem 0; box-shadow: 0 20px 40px rgba(0,0,0,0.2); border: 1px solid #334155; }
        .sim-title { font-size: 1.5rem; font-weight: 800; margin-top: 0; margin-bottom: 0.5rem; color: #38bdf8; display: flex; align-items: center; gap: 12px; }
        .sim-desc { color: #94a3b8; font-size: 0.95rem; margin-bottom: 2rem; border-bottom: 1px solid #334155; padding-bottom: 1rem;}
        
        .md-grid { display:grid; grid-template-columns: 1fr 1fr; gap:15px; }
        @media (max-width: 768px) { .md-grid { grid-template-columns: 1fr; } }
        .md-editor { background:#0f172a; border:1px solid #475569; border-radius:8px; padding:15px; font-family:'Fira Code', monospace; font-size:0.9rem; color:#a5b4fc; white-space:pre-wrap; }
        .md-preview { background:#fff; border-radius:8px; padding:15px; color:#333; font-family:sans-serif;}
        .md-preview h1 { margin-top:0; font-size:1.5rem; border-bottom:1px solid #eee; padding-bottom:5px;}
        .md-preview ul { padding-left:20px; }

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
        .home-btn:hover { transform: translateY(-5px) scale(1.05); background: var(--prompt-gray); color: white; }
        
        .btn-link { display:inline-flex; align-items:center; gap:8px; padding:12px 24px; background:linear-gradient(135deg, var(--prompt-gray), #1e293b); color:#fff; text-decoration:none; border-radius:30px; font-weight:700; transition:all 0.3s; box-shadow:0 6px 15px rgba(51,65,85,0.3); margin:10px 10px 10px 0;}
        .btn-link:hover { transform:translateY(-2px); box-shadow:0 10px 20px rgba(51,65,85,0.4);}
    </style>
</head>
<body>
    <header class="fixed-header">
        <a href="index.html" class="back-link"><i class="fa-solid fa-arrow-left"></i> Course Home</a>
        <div class="progress-container">
            <div class="progress-text"><span>Day 3 Progress</span><span id="progress-percent">0%</span></div>
            <div class="progress-bar-bg"><div class="progress-bar-fill" id="progress-bar"></div></div>
        </div>
        <div style="width:100px;"></div>
    </header>

    <div class="toc-sidebar">
        <div class="toc-title">IN THIS LESSON</div>
        <nav style="display:flex; flex-direction:column; gap:8px;">
            <a href="#sec-goal" class="toc-link" onclick="updateNav(this)"><i class="fa-solid fa-bullseye" style="color:#f59e0b"></i> 本日の目標</a>
            <a href="#sec-first" class="toc-link" onclick="updateNav(this)"><i class="fa-solid fa-code" style="color:#64748b"></i> 前半：プロンプト基本形</a>
            <a href="#sec-second" class="toc-link" onclick="updateNav(this)"><i class="fa-solid fa-code-branch" style="color:#8b5cf6"></i> 後半：プロンプト応用</a>
            <a href="#sec-summary" class="toc-link" onclick="updateNav(this)"><i class="fa-solid fa-flag-checkered" style="color:#10b981"></i> 今日のまとめ</a>
        </nav>
    </div>

    <div class="container">
        <!-- HERO -->
        <div class="hero course-section visible" style="margin-top: 2rem;">
            <div class="day-badge">DAY 03</div>
            <h1>プロンプト指示方法</h1>
        </div>

        <!-- 1. COURSE GOAL -->
        <section id="sec-goal" class="course-section">
            <div class="section-header">
                <div class="section-icon ch-goal"><i class="fa-solid fa-bullseye"></i></div>
                <h2 class="section-title">1. 今日のコース目標</h2>
            </div>
            
            <div class="glass-card">
                <div class="explain-box concept" style="background: #fffbef; border-left-color: #f59e0b; font-size: 1.1rem;">
                    <div class="explain-title" style="color:#b45309; font-size:1.3rem;"><i class="fa-solid fa-compass"></i> 言葉でAIを操る術を学ぶ</div>
                    本日の研修テーマは、<b>「生成AIのプロンプト指示方法とその応用」</b>です。<br><br>
                    効果的なプロンプト作成技術を習得し、生成AIから望むアウトプット（画像や動画の素材、テキスト等）を高い精度で引き出す能力を養います。AIを扱う上で最も重要な**「構造的なMarkdown記法」**の理解が鍵となります。
                </div>
            </div>
        </section>

        <!-- 2. FIRST HALF -->
        <section id="sec-first" class="course-section">
            <div class="section-header">
                <div class="section-icon ch-first"><i class="fa-solid fa-code"></i></div>
                <h2 class="section-title">2. 前半：プロンプトの基本形</h2>
            </div>

            <div class="glass-card">
                <div class="card-header-small"><i class="fa-solid fa-film" style="color:#64748b;"></i> 再生動画についての説明と解説</div>
                
                <div class="explain-box concept">
                    <div class="explain-title"><i class="fa-brands fa-markdown"></i> Markdownによる構造化</div>
                    AIは長文のベタ打ちより、箇条書きや見出し（Markdown記法）で「構造化」された文章を好みます。<br>
                    動画を通じてプロンプトの基本形と、Markdownの書き方を理解しましょう。
                </div>

                <div class="video-grid">
                    <a href="https://youtu.be/yKI4eBOopF4" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/yKI4eBOopF4/maxresdefault.jpg" alt="動画1" onerror="this.src='https://img.youtube.com/vi/yKI4eBOopF4/hqdefault.jpg'">
                        <div class="play-overlay"><div class="play-icon"><i class="fa-solid fa-play" style="margin-left:4px;"></i></div></div>
                    </a>
                    <a href="https://youtu.be/3tVEkHG3FyQ" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/3tVEkHG3FyQ/maxresdefault.jpg" alt="動画2" onerror="this.src='https://img.youtube.com/vi/3tVEkHG3FyQ/hqdefault.jpg'">
                        <div class="play-overlay"><div class="play-icon"><i class="fa-solid fa-play" style="margin-left:4px;"></i></div></div>
                    </a>
                    <a href="https://youtu.be/PmVtulQfOR0" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/PmVtulQfOR0/maxresdefault.jpg" alt="動画3" onerror="this.src='https://img.youtube.com/vi/PmVtulQfOR0/hqdefault.jpg'">
                        <div class="play-overlay"><div class="play-icon"><i class="fa-solid fa-play" style="margin-left:4px;"></i></div></div>
                    </a>
                    <a href="https://youtu.be/i2Z2TtUe9Kk" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/i2Z2TtUe9Kk/maxresdefault.jpg" alt="動画4" onerror="this.src='https://img.youtube.com/vi/i2Z2TtUe9Kk/hqdefault.jpg'">
                        <div class="play-overlay"><div class="play-icon"><i class="fa-solid fa-play" style="margin-left:4px;"></i></div></div>
                    </a>
                </div>

                <div>
                    <a href="https://kino-code.com/prompt-engineering-04/" target="_blank" class="btn-link"><i class="fa-solid fa-envelope"></i> メール返信プロンプト例</a>
                    <a href="https://help.docbase.io/posts/13697" target="_blank" class="btn-link" style="background:#475569;"><i class="fa-brands fa-markdown"></i> Markdown記法解説</a>
                </div>
            </div>

            <!-- Practical Section -->
            <div class="glass-card">
                <div class="card-header-small"><i class="fa-solid fa-laptop-code" style="color:#10b981;"></i> 実習内容の説明と解説</div>
                
                <div class="explain-box practice">
                    <div class="explain-title"><i class="fa-solid fa-pen"></i> ノートまとめ</div>
                    動画を見ながら、生成のコツとMarkdown記法について自分なりの理解をノートにまとめましょう。<br>
                    後からすぐにコピペできる形で保存しておくことが重要です。
                </div>

                <div class="simulator-area">
                    <div class="sim-title" style="color:#38bdf8;"><i class="fa-brands fa-markdown"></i> 疑似体験: 構造化プロンプト</div>
                    <div class="sim-desc">ベタ打ちと構造化で、どう見え方が変わるか（AIにとっての分かりやすさ）を比較します。</div>
                    
                    <div class="md-grid">
                        <div class="md-editor"># プロンプト例
あなたは優秀なライターです。
以下の条件で記事を書いてください。

## 条件
- 文字数：300字
- トピック：AIの未来
- トーン：ポジティブ</div>
                        <div class="md-preview">
                            <h1>プロンプト例</h1>
                            <p>あなたは優秀なライターです。<br>以下の条件で記事を書いてください。</p>
                            <h2>条件</h2>
                            <ul>
                                <li>文字数：300字</li>
                                <li>トピック：AIの未来</li>
                                <li>トーン：ポジティブ</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="mission-panel" onclick="completeMission(this, 1)">
                    <div class="wax-seal" style="background:#64748b; border-color:#334155;"><i class="fa-brands fa-markdown"></i></div>
                    <div class="ms-icon"><i class="fa-solid fa-file-code"></i></div>
                    <div class="ms-content">
                        <h3>Mission 1: 構造化の理解</h3>
                        <p>Markdown記法の基本（#, -, ** 等）を理解し、整理されたプロンプトの記述方法を学んだ。</p>
                    </div>
                    <div class="ms-check"><i class="fa-solid fa-check"></i></div>
                </div>
            </div>
        </section>

        <!-- 3. SECOND HALF -->
        <section id="sec-second" class="course-section">
            <div class="section-header">
                <div class="section-icon ch-second"><i class="fa-solid fa-code-branch"></i></div>
                <h2 class="section-title">3. 後半：プロンプトの応用</h2>
            </div>

            <div class="glass-card">
                <div class="card-header-small"><i class="fa-solid fa-film" style="color:#8b5cf6;"></i> 再生動画についての説明と解説</div>
                
                <div class="explain-box concept" style="background: #f5f3ff; border-left-color: #8b5cf6;">
                    <div class="explain-title" style="color: #5b21b6;"><i class="fa-solid fa-magnifying-glass-chart"></i> さらに高度な指示へ</div>
                    前半で学んだ基本形をベースに、より具体的で複雑な指示を出すための応用テクニックを学びます。<br>
                    提供される動画から、変数の使い方や、段階的な指示（ステップ・バイ・ステップ）の手法を習得しましょう。
                </div>

                <div class="video-grid">
                    <a href="https://youtu.be/hf2-6gZmFlo" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/hf2-6gZmFlo/maxresdefault.jpg" alt="後半動画1" onerror="this.src='https://img.youtube.com/vi/hf2-6gZmFlo/hqdefault.jpg'">
                        <div class="play-overlay"><div class="play-icon"><i class="fa-solid fa-play" style="margin-left:4px;"></i></div></div>
                    </a>
                    <a href="https://youtu.be/J9YtakGpqZQ" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/J9YtakGpqZQ/maxresdefault.jpg" alt="後半動画2" onerror="this.src='https://img.youtube.com/vi/J9YtakGpqZQ/hqdefault.jpg'">
                        <div class="play-overlay"><div class="play-icon"><i class="fa-solid fa-play" style="margin-left:4px;"></i></div></div>
                    </a>
                    <a href="https://youtu.be/bZkGoWuQ3vg" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/bZkGoWuQ3vg/maxresdefault.jpg" alt="後半動画3" onerror="this.src='https://img.youtube.com/vi/bZkGoWuQ3vg/hqdefault.jpg'">
                        <div class="play-overlay"><div class="play-icon"><i class="fa-solid fa-play" style="margin-left:4px;"></i></div></div>
                    </a>
                </div>
            </div>

            <!-- Practical Section -->
            <div class="glass-card">
                <div class="card-header-small"><i class="fa-solid fa-laptop-code" style="color:#10b981;"></i> 実習内容の説明と解説</div>
                
                <div class="explain-box practice">
                    <div class="explain-title"><i class="fa-solid fa-book-open"></i> プロンプト学習用のノート作成</div>
                    動画を見ながら、応用プロンプトのコツをノートにまとめましょう。<br>
                    以下のスプレッドシートにある「動画内のプロンプト一覧」も大いに活用してください。
                </div>
                
                <div>
                    <a href="https://docs.google.com/spreadsheets/d/1FK-Pocn0T-tuCLTht0rUJc622tlv1x_68xZ8lLTlJR4/edit?usp=sharing" target="_blank" class="btn-link" style="background:linear-gradient(135deg, #10b981, #059669);"><i class="fa-solid fa-table"></i> 動画内プロンプト一覧</a>
                </div>

                <div class="mission-panel" onclick="completeMission(this, 2)">
                    <div class="wax-seal" style="background:#8b5cf6; border-color:#6d28d9;"><i class="fa-solid fa-star"></i></div>
                    <div class="ms-icon"><i class="fa-solid fa-laptop-medical"></i></div>
                    <div class="ms-content">
                        <h3>Mission 2: プロンプト応用ノート完成</h3>
                        <p>応用的な生成のコツと実例をノートにまとめ、すぐに実務や課題で利用できる状態にした。</p>
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
                    <i class="fa-solid fa-medal"></i> Day 3 コンプリート！
                </h3>
                <p style="font-size: 1.1rem; line-height: 1.8; color: #064e3b; margin-top:1.5rem;">
                    お疲れ様でした！AIの思考回路に合わせた「Markdownを用いた構造化プロンプト」は、すべてのAIツールにおいて最強の武器となります。<br><br>
                    プロンプトはただの指示ではなく、**AIという優秀なアシスタントへの「ディレクション（監督指示）」**です。この基礎をしっかり押さえたことで、明日以降の画像・動画生成のクオリティが飛躍的に上がるでしょう！
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

        function finishDay() {
            window.location.href = "index.html";
        }
    </script>
</body>
</html>
