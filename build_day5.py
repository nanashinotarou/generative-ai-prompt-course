# -*- coding: utf-8 -*-
import os

html_content = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day 5 | AI Video Generation & Prompting</title>
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

        /* Content List Grid */
        .bento-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin: 2.5rem 0;}
        .bento-item { background: #fff; border-radius: 16px; padding: 2rem; position: relative; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.03); border: 1px solid #f1f5f9; transition: transform 0.3s, box-shadow 0.3s;}
        .bento-item:hover { transform: translateY(-5px); box-shadow: 0 12px 25px rgba(0,0,0,0.06); border-color: var(--accent-light);}
        .bento-item h4 { margin: 0 0 1rem; font-size: 1.2rem; color: var(--text-main); display: flex; align-items: center; gap: 0.5rem; font-weight:800;}
        .bento-item p { font-size: 1.05rem; color: #64748b; line-height: 1.6; margin: 0; }

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
        
        .btn { display: inline-flex; align-items: center; gap: 0.6rem; background: var(--clickable); color: #fff; border: none; padding: 0.8rem 1.8rem; border-radius: 12px; text-decoration: none; font-size: 1.05rem; font-weight: 800; transition: all 0.2s; cursor: pointer; margin-top: 1rem; box-shadow: 0 6px 15px rgba(14, 165, 233, 0.3); }
        .btn:hover { background: #0284c7; transform: translateY(-2px); box-shadow: 0 8px 20px rgba(14, 165, 233, 0.4); }
    </style>
</head>
<body>

    <canvas id="particles"></canvas>
    <canvas id="confetti"></canvas>

    <!-- Header -->
    <header class="fixed-header">
        <a href="index.html" class="back-link"><i class="fa-solid fa-arrow-left"></i> Course Home</a>
        <div class="progress-container">
            <div class="progress-text"><span>Day 5 Progress</span><span id="progress-percent">0%</span></div>
            <div class="progress-bar-bg"><div class="progress-bar-fill" id="progress-bar"></div></div>
        </div>
        <div style="width:100px;"></div>
    </header>

    <div class="container">
        <!-- Hero -->
        <div class="hero">
            <div class="day-badge">DAY 05</div>
            <h1>AI動画生成とプロンプト技術</h1>
            <p>本日の目標：テキストから動画への変換技術の基礎をマスターする。<br>静止画を動かすだけでなく、完全なテキストから高度な動画を生成し、カメラワークまでコントロールしてみましょう。</p>
        </div>

        <!-- Premium Tab Navigation -->
        <div class="tab-nav">
            <button class="tab-btn active" onclick="switchTab('tab-goal')"><i class="fa-solid fa-bullseye" style="color:#f59e0b;"></i> コース目標</button>
            <button class="tab-btn" onclick="switchTab('tab-first')"><i class="fa-solid fa-video" style="color:#10b981;"></i> 前半：プロンプト術20選</button>
            <button class="tab-btn" onclick="switchTab('tab-second')"><i class="fa-solid fa-film" style="color:#0ea5e9;"></i> 後半：実践・カメラワーク</button>
            <button class="tab-btn" onclick="switchTab('tab-summary')"><i class="fa-solid fa-flag-checkered" style="color:#8b5cf6;"></i> 今日のまとめ</button>
        </div>

        <!-- ==========================================
             TAB 1: COURSE GOALS
        ========================================== -->
        <div id="tab-goal" class="tab-content active">
            <div class="glass-card" style="border-top: 5px solid #f59e0b;">
                <div class="card-header"><i class="fa-solid fa-compass" style="color:#f59e0b; background:#fffbeb;"></i><h2>本日の研修ねらい</h2></div>
                <div class="info-box" style="border-left-color: #f59e0b; background: #fffbeb;">
                    <h4 style="color:#b45309;"><i class="fa-solid fa-film"></i> テキストベースの映像ディレクターになる</h4>
                    <p style="color:#92400e;">
                        本日の研修は、<b>「テキストから動画への変換技術の基礎」</b>です。<br><br>
                        静止画の生成技術はもはや普及段階にありますが、いま最も注目され、実務での革新をもたらしているのが「AI動画生成」です。
                        本日は、AIに意図した通りの動画を作らせるための「動画特有のプロンプト要素20選」と、映像の質を決定づける「カメラワークの制御」について学びます。<br>
                        これらの技術を活用し、高品質な動画コンテンツを一人でディレクション・制作・発信できる人材になりましょう！
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
                <div class="card-header"><i class="fa-brands fa-youtube" style="color:#ef4444; background:#fef2f2;"></i><h2>前半：AI動画生成の精度を劇的に高めるプロンプト術20選</h2></div>
                <p style="font-size:1.1rem; margin-bottom:1.5rem;">動画生成AIで思い通りの映像を作るには、静止画とは一味違うコツが必要です。動画の意図を正確にコントロールするための必修テクニック集です。</p>
                
                <div class="video-grid" style="grid-template-columns: 1fr; max-width:800px; margin: 0 auto 3rem auto;">
                    <a href="https://youtu.be/gDRpdBFwg6Y" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/gDRpdBFwg6Y/maxresdefault.jpg" alt="動画1" onerror="this.src='https://img.youtube.com/vi/gDRpdBFwg6Y/hqdefault.jpg'">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                </div>

                <h3 style="color:#065f46; margin-top:3rem; font-size:1.5rem;"><i class="fa-solid fa-list-ol"></i> 20のテクニック 詳細解説</h3>
                
                <!-- 20 Accordions grouped logically for better premium UI -->
                <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap:1rem;">
                    <div>
                        <details class="prompt-accordion">
                            <summary><span class="tag">01:04</span> ① 世界観を指定 <i class="fa-solid fa-chevron-down"></i></summary>
                            <div class="prompt-content">
                                <p style="margin-top:0;">動画全体の雰囲気や時代背景、場所のコンセプトを明確にします。</p>
                                <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=64s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 01:04 から見る</a>
                            </div>
                        </details>
                        <details class="prompt-accordion">
                            <summary><span class="tag">02:20</span> ② 表情を指定 <i class="fa-solid fa-chevron-down"></i></summary>
                            <div class="prompt-content">
                                <p style="margin-top:0;">被写体の感情を制御し、物語性を追加します。</p>
                                <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=140s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 02:20 から見る</a>
                            </div>
                        </details>
                        <details class="prompt-accordion">
                            <summary><span class="tag">03:47</span> ③ トーン＆ジャンルを指定 <i class="fa-solid fa-chevron-down"></i></summary>
                            <div class="prompt-content">
                                <p style="margin-top:0;">「シネマティック」「アニメ風」など映像のスタイルを決定します。</p>
                                <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=227s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 03:47 から見る</a>
                            </div>
                        </details>
                        <details class="prompt-accordion">
                            <summary><span class="tag">05:04</span> ④ キャラクターの固定 <i class="fa-solid fa-chevron-down"></i></summary>
                            <div class="prompt-content">
                                <p style="margin-top:0;">同一人物を別のシーンでも破綻させずに登場させるテクニック。</p>
                                <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=304s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 05:04 から見る</a>
                            </div>
                        </details>
                        <details class="prompt-accordion">
                            <summary><span class="tag">06:24</span> ⑤ 画角をロック <i class="fa-solid fa-chevron-down"></i></summary>
                            <div class="prompt-content">
                                <p style="margin-top:0;">意図しないカメラの引きや寄りを防ぎます。</p>
                                <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=384s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 06:24 から見る</a>
                            </div>
                        </details>
                        <details class="prompt-accordion">
                            <summary><span class="tag">07:41</span> ⑥ 小さな動きに限定 <i class="fa-solid fa-chevron-down"></i></summary>
                            <div class="prompt-content">
                                <p style="margin-top:0;">AIの破綻を防ぐため、最初は「まばたき」など小さな動きから指示します。</p>
                                <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=461s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 07:41 から見る</a>
                            </div>
                        </details>
                        <details class="prompt-accordion">
                            <summary><span class="tag">08:54</span> ⑦ オブジェクト数の制限 <i class="fa-solid fa-chevron-down"></i></summary>
                            <div class="prompt-content">
                                <p style="margin-top:0;">要素が多すぎるとAIが混乱するため、画面内の主役を絞ります。</p>
                                <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=534s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 08:54 から見る</a>
                            </div>
                        </details>
                        <details class="prompt-accordion">
                            <summary><span class="tag">09:56</span> ⑧ スピードを指定 <i class="fa-solid fa-chevron-down"></i></summary>
                            <div class="prompt-content">
                                <p style="margin-top:0;">「スローモーション」や「タイムラプス」など時間の流れを制御します。</p>
                                <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=596s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 09:56 から見る</a>
                            </div>
                        </details>
                        <details class="prompt-accordion">
                            <summary><span class="tag">10:46</span> ⑨ 照明を指定 <i class="fa-solid fa-chevron-down"></i></summary>
                            <div class="prompt-content">
                                <p style="margin-top:0;">「ゴールデンアワー」「スタジオ照明」など光と影で質感を高めます。</p>
                                <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=646s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 10:46 から見る</a>
                            </div>
                        </details>
                        <details class="prompt-accordion">
                            <summary><span class="tag">11:51</span> ⑩ 開始と終了を指定 <i class="fa-solid fa-chevron-down"></i></summary>
                            <div class="prompt-content">
                                <p style="margin-top:0;">動画の最初のフレームと最後のフレームを明示し、ストーリーを作ります。</p>
                                <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=711s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 11:51 から見る</a>
                            </div>
                        </details>
                    </div>
                    <div>
                        <details class="prompt-accordion">
                            <summary><span class="tag">13:16</span> ⑪ 背景の動きを指定 <i class="fa-solid fa-chevron-down"></i></summary>
                            <div class="prompt-content">
                                <p style="margin-top:0;">被写体だけでなく、背景の「木の揺れ」「通行人」などを制御します。</p>
                                <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=796s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 13:16 から見る</a>
                            </div>
                        </details>
                        <details class="prompt-accordion">
                            <summary><span class="tag">14:24</span> ⑫ 重力・物理法則を指定 <i class="fa-solid fa-chevron-down"></i></summary>
                            <div class="prompt-content">
                                <p style="margin-top:0;">「水しぶき」「髪のなびき」など、リアルな物理現象をプロンプトで補強。</p>
                                <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=864s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 14:24 から見る</a>
                            </div>
                        </details>
                        <details class="prompt-accordion">
                            <summary><span class="tag">15:36</span> ⑬ カメラワークを指定 <i class="fa-solid fa-chevron-down"></i></summary>
                            <div class="prompt-content">
                                <p style="margin-top:0;">パンやズームなど、プロのカメラマンのような視点移動を追加します。</p>
                                <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=936s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 15:36 から見る</a>
                            </div>
                        </details>
                        <details class="prompt-accordion">
                            <summary><span class="tag">16:38</span> ⑭ 視線の行き先を指定 <i class="fa-solid fa-chevron-down"></i></summary>
                            <div class="prompt-content">
                                <p style="margin-top:0;">被写体がどこを見ているかを指定し、視聴者の視線を誘導します。</p>
                                <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=998s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 16:38 から見る</a>
                            </div>
                        </details>
                        <details class="prompt-accordion">
                            <summary><span class="tag">17:38</span> ⑮ 表情を指定 (微細に) <i class="fa-solid fa-chevron-down"></i></summary>
                            <div class="prompt-content">
                                <p style="margin-top:0;">動画内で表情が「真顔から笑顔へ」変化するような過程を指示。</p>
                                <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=1058s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 17:38 から見る</a>
                            </div>
                        </details>
                        <details class="prompt-accordion">
                            <summary><span class="tag">18:33</span> ⑯ 禁止事項を指定 <i class="fa-solid fa-chevron-down"></i></summary>
                            <div class="prompt-content">
                                <p style="margin-top:0;">「文字を入れない」「変形しない」などネガティブプロンプトの活用。</p>
                                <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=1113s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 18:33 から見る</a>
                            </div>
                        </details>
                        <details class="prompt-accordion">
                            <summary><span class="tag">20:24</span> ⑰ 動きを指定(テキストのみ) <i class="fa-solid fa-chevron-down"></i></summary>
                            <div class="prompt-content">
                                <p style="margin-top:0;">特定の動詞を用いて、複雑な動作をテキストだけで高精度に実現。</p>
                                <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=1224s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 20:24 から見る</a>
                            </div>
                        </details>
                        <details class="prompt-accordion">
                            <summary><span class="tag">21:29</span> ⑱ 動きを指定(モーションコントロール) <i class="fa-solid fa-chevron-down"></i></summary>
                            <div class="prompt-content">
                                <p style="margin-top:0;">AIツールのモーションブラシ機能などとプロンプトを併用。</p>
                                <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=1289s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 21:29 から見る</a>
                            </div>
                        </details>
                        <details class="prompt-accordion">
                            <summary><span class="tag">22:51</span> ⑲ 音声を指定 <i class="fa-solid fa-chevron-down"></i></summary>
                            <div class="prompt-content">
                                <p style="margin-top:0;">生成後にリップシンク等で繋げるための「喋っている口元」の指定。</p>
                                <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=1371s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 22:51 から見る</a>
                            </div>
                        </details>
                        <details class="prompt-accordion">
                            <summary><span class="tag">24:36</span> ⑳ 動画の続きを指定 <i class="fa-solid fa-chevron-down"></i></summary>
                            <div class="prompt-content">
                                <p style="margin-top:0;">生成された動画の延長(Extend)時のプロンプトのコツ。</p>
                                <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t=1476s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 24:36 から見る</a>
                            </div>
                        </details>
                    </div>
                </div>

                <!-- GAMIFIED MISSION 1 -->
                <div class="mission-area" id="mission-group-1" style="border-color: #10b981;">
                    <div class="wax-seal" style="background: radial-gradient(circle at 30% 30%, #6ee7b7, #10b981, #047857); border-color:#065f46;"><i class="fa-solid fa-check"></i></div>
                    <div class="mission-header">
                        <h3 style="color:#10b981;"><i class="fa-solid fa-clipboard-list"></i> MILESTONE 1: プロンプト基礎</h3>
                        <p>20のテクニックのうち、まずは全体像を把握しよう。</p>
                    </div>
                    <ul class="task-list">
                        <li class="task-item" onclick="toggleTask('t1_1', this, 1)">
                            <div class="custom-checkbox" id="check_t1_1"><i class="fa-solid fa-check"></i></div>
                            <div class="task-content">
                                <h4>プロンプト術の視聴</h4>
                                <p>提示された動画を視聴し、AI動画特有のプロンプト作成のコツを理解する。</p>
                            </div>
                        </li>
                        <li class="task-item" onclick="toggleTask('t1_2', this, 1)">
                            <div class="custom-checkbox" id="check_t1_2"><i class="fa-solid fa-check"></i></div>
                            <div class="task-content">
                                <h4>テクニックの確認</h4>
                                <p>自分の作りたい映像に合わせて、どのアプローチが有効か2〜3個目星をつける。</p>
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

with open("vol05-1_text_to_video.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated vol05-1_text_to_video.html")
import os

html_content = """
        <!-- ==========================================
             TAB 3: SECOND HALF
        ========================================== -->
        <div id="tab-second" class="tab-content">
            <div class="glass-card" style="border-top: 5px solid #0ea5e9;">
                <div class="card-header"><i class="fa-solid fa-film" style="color:#0ea5e9; background:#e0f2fe;"></i><h2>後半：カメラワーク＆3D連携・実践プレイリスト</h2></div>
                <p style="font-size:1.1rem; margin-bottom:1.5rem;">AI動画の“動きの質”を激変させる実践編です。</p>
                
                <h3 style="color:#0369a1; margin-top:2rem; font-size:1.4rem;"><i class="fa-solid fa-video"></i> カメラワークと動きの制御</h3>
                <div class="video-grid" style="grid-template-columns: 1fr; max-width:800px; margin: 0 auto 3rem auto;">
                    <a href="https://youtu.be/stgEbOmqL1A" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/stgEbOmqL1A/maxresdefault.jpg" alt="カメラワーク動画" onerror="this.src='https://img.youtube.com/vi/stgEbOmqL1A/hqdefault.jpg'">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                </div>

                <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:1rem;">
                    <details class="prompt-accordion">
                        <summary><span class="tag">0:37</span> 基本のカメラワーク <i class="fa-solid fa-chevron-down"></i></summary>
                        <div class="prompt-content">
                            <p style="margin-top:0;">Kling AI等で使える基本的なカメラ表現（パン、ティルト、ズーム等）。</p>
                            <a href="https://www.youtube.com/watch?v=stgEbOmqL1A&t=37s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 0:37 から見る</a>
                        </div>
                    </details>
                    <details class="prompt-accordion">
                        <summary><span class="tag">2:29</span> カメラワークの悩み全解決 <i class="fa-solid fa-chevron-down"></i></summary>
                        <div class="prompt-content">
                            <p style="margin-top:0;">よくある「意図しない動き」を制御し、安定させるテクニック。</p>
                            <a href="https://www.youtube.com/watch?v=stgEbOmqL1A&t=149s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 2:29 から見る</a>
                        </div>
                    </details>
                    <details class="prompt-accordion">
                        <summary><span class="tag">4:09</span> シーンコンテキストの追加 <i class="fa-solid fa-chevron-down"></i></summary>
                        <div class="prompt-content">
                            <p style="margin-top:0;">画面の周囲の状況や文脈を指示し、より豊かな映像にする。</p>
                            <a href="https://www.youtube.com/watch?v=stgEbOmqL1A&t=249s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 4:09 から見る</a>
                        </div>
                    </details>
                    <details class="prompt-accordion">
                        <summary><span class="tag">6:32</span> ５つのポイント <i class="fa-solid fa-chevron-down"></i></summary>
                        <div class="prompt-content">
                            <p style="margin-top:0;">最終的なクオリティを底上げするための必須チェックリスト。</p>
                            <a href="https://www.youtube.com/watch?v=stgEbOmqL1A&t=392s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 6:32 から見る</a>
                        </div>
                    </details>
                </div>

                <hr style="border:0; border-top:1px solid #e2e8f0; margin: 3rem 0;">

                <h3 style="color:#0369a1; font-size:1.4rem;"><i class="fa-solid fa-cube"></i> 背景もアングルも“3D”で完全支配。３D生成連携</h3>
                <div class="video-grid" style="grid-template-columns: 1fr; max-width:800px; margin: 0 auto 1.5rem auto;">
                    <a href="https://youtu.be/NfM2x5RqmUI" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/NfM2x5RqmUI/maxresdefault.jpg" alt="3D生成×Gemini連携" onerror="this.src='https://img.youtube.com/vi/NfM2x5RqmUI/hqdefault.jpg'">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                </div>
                <div style="display:flex; justify-content:center; gap:15px; flex-wrap:wrap; margin-bottom: 3rem;">
                    <a href="https://www.hitem3d.ai/" target="_blank" class="btn" style="background:#1e293b;"><i class="fa-solid fa-cube"></i> Hitem3D サイトへ</a>
                    <a href="https://www.blender.org/" target="_blank" class="btn" style="background:#ea580c;"><i class="fa-solid fa-cubes"></i> Blender サイトへ</a>
                </div>

                <div class="info-box" style="border-left-color: #0ea5e9; background: #f0f9ff; margin-top:2rem;">
                    <h4 style="color:#0369a1;"><i class="fa-solid fa-list-ol"></i> プロンプト学習用・実践プレイリスト</h4>
                    <p style="color:#0c4a6e; margin-bottom:1rem;">
                        生成のコツを理解し、学んだ内容を自分用の「プロンプトノート」としてまとめ、後から仕事や制作ですぐに引き出せるようにしておくことが目標です。以下の再生リストを視聴しながら、学んだ技術をストックしましょう。
                    </p>
                    <a href="https://www.youtube.com/playlist?list=PLoQApr14fceM1VnrF1uTVceOH_56bBha0" target="_blank" class="btn" style="background:#0ea5e9; box-shadow: 0 4px 15px rgba(14, 165, 233, 0.3);">
                        <i class="fa-brands fa-youtube"></i> 実践プレイリストを開く
                    </a>
                </div>

                <!-- GAMIFIED MISSION 2 -->
                <div class="mission-area" id="mission-group-2" style="border-color: #0ea5e9;">
                    <div class="wax-seal" style="background: radial-gradient(circle at 30% 30%, #7dd3fc, #0ea5e9, #0369a1); border-color:#0284c7;"><i class="fa-solid fa-stamp"></i></div>
                    <div class="mission-header">
                        <h3 style="color:#0ea5e9;"><i class="fa-solid fa-clapperboard"></i> MILESTONE 2: 動画のディレクション</h3>
                        <p>カメラワークと実践的なアプローチを習得しよう。</p>
                    </div>
                    
                    <ul class="task-list">
                        <li class="task-item" onclick="toggleTask('t2_1', this, 2)">
                            <div class="custom-checkbox" id="check_t2_1"><i class="fa-solid fa-check"></i></div>
                            <div class="task-content">
                                <h4>カメラワークの学習</h4>
                                <p>動画を視聴し、パン、ティルト、ズームなどの基本的なカメラ制御を理解する。</p>
                            </div>
                        </li>
                        <li class="task-item" onclick="toggleTask('t2_2', this, 2)">
                            <div class="custom-checkbox" id="check_t2_2"><i class="fa-solid fa-check"></i></div>
                            <div class="task-content">
                                <h4>3Dツール連携の確認</h4>
                                <p>Hitem3Dなどのツールとの組み合わせによる、アングル完全支配の概念を知る。</p>
                            </div>
                        </li>
                        <li class="task-item" onclick="toggleTask('t2_3', this, 2)">
                            <div class="custom-checkbox" id="check_t2_3"><i class="fa-solid fa-check"></i></div>
                            <div class="task-content">
                                <h4>実践プレイリストの視聴</h4>
                                <p>プレイリストから興味のある作例を選び、プロンプトの組み立て方を自分なりにメモする。</p>
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
                    <i class="fa-solid fa-medal" style="font-size:2.5rem;"></i> Day 5 全行程コンプリート！
                </h3>
                <p style="font-size: 1.25rem; line-height: 2; color: #4c1d95; margin-top:2rem; text-align:center; padding: 0 2rem;">
                    お疲れ様でした！本日は<strong>「テキストから動画への変換技術の基礎とカメラワーク」</strong>について学びました。<br>
                    世界観の設定から、微細な表情の制御、プロの映像作家のようなカメラワークまで、AIを活用して頭の中の映像を具現化するためのディレクション術を習得できたはずです。<br><br>
                    <strong>これで、Day1からDay5まで続いた「生成AIとプロンプト基礎研修」はすべて修了となります。</strong><br>
                    ここからは、学んだ技術を自分自身の業務や制作活動で存分に発揮してください！
                </p>

                <div style="margin-top:4rem; text-align:center;">
                    <button class="btn" style="padding: 1.2rem 4rem; font-size:1.3rem; background:linear-gradient(135deg, #8b5cf6, #6d28d9); border-radius:50px; box-shadow: 0 10px 25px rgba(139, 92, 246, 0.4);" onclick="window.location.href='index.html'">
                        <i class="fa-solid fa-award"></i> 全コース修了を記録してHomeへ戻る
                    </button>
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
        function copyPrompt(btn) {
            const pre = btn.nextElementSibling;
            if(!pre) return;
            const text = pre.innerText;
            navigator.clipboard.writeText(text).then(() => {
                const originalHtml = btn.innerHTML;
                btn.innerHTML = '<i class="fa-solid fa-check"></i>';
                btn.style.color = '#10b981';
                setTimeout(() => { btn.innerHTML = originalHtml; btn.style.color = ''; }, 2000);
            });
        }

        // Checklist Logic
        const missionGroups = {
            1: ['t1_1', 't1_2'],
            2: ['t2_1', 't2_2', 't2_3']
        };
        const allTasks = [...missionGroups[1], ...missionGroups[2]];
        let state = {};

        window.addEventListener('DOMContentLoaded', () => {
            const saved = localStorage.getItem('day5_premium_prog');
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
            localStorage.setItem('day5_premium_prog', JSON.stringify(state));
            
            updateProgress();
            checkGroups(groupId);
        }

        function checkGroups(triggerGroupId = null) {
            let allMissionsDone = true;
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
                        allMissionsDone = false;
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

with open("vol05-1_text_to_video.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated vol05-1_text_to_video.html")
