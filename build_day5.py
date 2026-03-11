import os

html_content = """<!DOCTYPE html>
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
        .hero .intention { background: #eff6ff; border-left: 4px solid var(--clickable); padding: 1rem 1.5rem; border-radius: 8px; margin-top: 1.5rem; text-align: left; font-weight: 500; color: #1e3a8a;}

        /* Tabs */
        .tab-container { display: flex; justify-content: center; gap: 1rem; margin-bottom: 3rem; flex-wrap: wrap; }
        .tab-btn { background: #fff; border: 2px solid #e2e8f0; color: var(--text-sub); padding: 1rem 2rem; border-radius: 40px; cursor: pointer; font-weight: 700; font-size: 0.95rem; transition: all 0.3s; }
        .tab-btn:hover { border-color: var(--clickable); color: var(--clickable); }
        .tab-btn.active { background: var(--accent); color: #fff; border-color: var(--accent); box-shadow: 0 8px 20px rgba(16, 185, 129, 0.25); }
        
        .tab-content { display: none; animation: fadeIn 0.5s ease; }
        .tab-content.active { display: block; }

        /* Glass Card */
        .glass-card { background: var(--bg-card); backdrop-filter: var(--glass-blur); border: 1px solid rgba(255,255,255,0.7); border-radius: var(--radius); padding: 2.5rem; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.03); transition: transform 0.3s, box-shadow 0.3s; }
        .glass-card:hover { transform: translateY(-2px); box-shadow: 0 15px 35px rgba(0,0,0,0.05); }
        .card-header { display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem; border-bottom: 2px solid #f1f5f9; padding-bottom: 1rem; }
        .card-header i { font-size: 1.5rem; color: var(--accent); background: var(--accent-bg); padding: 1rem; border-radius: 14px; }
        .card-header h2 { margin: 0; font-size: 1.6rem; color: var(--text-main); }

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

        /* Browser Mockup */
        .browser-mockup { background: #1e293b; border-radius: 12px; overflow: hidden; margin: 1.5rem 0; box-shadow: 0 10px 25px rgba(0,0,0,0.15); border: 1px solid #334155; }
        .browser-header { background: #0f172a; padding: 12px 16px; display: flex; gap: 8px; border-bottom: 1px solid #334155; }
        .dot { width: 12px; height: 12px; border-radius: 50%; }
        .dot.red { background: #ff5f56; } .dot.yellow { background: #ffbd2e; } .dot.green { background: #27c93f; }
        .browser-content { padding: 1.5rem; color: #f8fafc; font-family: 'Fira Code', 'Consolas', monospace; font-size: 0.9rem; line-height: 1.6; white-space: pre-wrap; position: relative;}
        
        .copy-btn { position: absolute; top: 10px; right: 10px; background: rgba(255,255,255,0.1); color: #fff; border: 1px solid rgba(255,255,255,0.2); padding: 6px 12px; border-radius: 6px; cursor: pointer; display: flex; align-items: center; gap: 6px; font-size: 0.8rem; transition: all 0.2s; }
        .copy-btn:hover { background: rgba(255,255,255,0.2); }

        /* General Buttons */
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

        .tag { background: #e0f2fe; color: #0284c7; padding: 2px 8px; border-radius: 6px; font-size: 0.8rem; font-weight: 700; margin-right: 5px;}
        
        @keyframes fadeInDown { from { opacity: 0; transform: translateY(-20px); } to { opacity: 1; transform: translateY(0); } }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        
        /* Floating Action */
        .home-btn {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: linear-gradient(135deg, var(--clickable), #3b82f6);
            color: white;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            box-shadow: 0 10px 25px rgba(14, 165, 233, 0.4);
            text-decoration: none;
            transition: all 0.3s;
            z-index: 1000;
        }
        .home-btn:hover {
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 15px 35px rgba(14, 165, 233, 0.5);
            color: white;
        }
    </style>
</head>
<body>
    <header class="fixed-header">
        <a href="index.html" class="back-link"><i class="fa-solid fa-arrow-left"></i> Course Home</a>
        <div class="progress-container">
            <div class="progress-text"><span>Day 5 Progress</span><span id="progress-percent">0%</span></div>
            <div class="progress-bar-bg"><div class="progress-bar-fill" id="progress-bar" style="width: 20%;"></div></div>
        </div>
        <div style="width:100px;"></div>
    </header>

    <div class="container">
        <div class="hero">
            <div class="day-badge">DAY 05</div>
            <h1>AI動画生成とプロンプト技術</h1>
            <p>本日の目標：テキストから動画への変換技術の基礎をマスターする。</p>
            <div class="intention">
                <strong><i class="fa-solid fa-bullseye"></i> 本日の研修ねらい：</strong><br>
                本日の研修は、<b>「テキストから動画への変換技術の基礎」</b>です。静止画だけでなく、AIによる高度な動画生成・カメラワーク・3Dツール連携を活用し、テキストベースで高品質な動画コンテンツを制作・発信できる人材になりましょう！
            </div>
        </div>

        <div class="tab-container">
            <button class="tab-btn active" onclick="switchTab('tab1')">プロンプト術 20選</button>
            <button class="tab-btn" onclick="switchTab('tab2')">カメラワーク＆3D連携</button>
            <button class="tab-btn" onclick="switchTab('tab3')">実践プレイリスト</button>
        </div>

        <div id="tab1" class="tab-content active">
            <div class="glass-card">
                <div class="card-header"><i class="fa-brands fa-youtube" style="color:#ef4444;"></i><h2>AI動画生成の精度を劇的に高めるプロンプト術20選</h2></div>
                <div class="video-grid" style="grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));">
                    <a href="https://youtu.be/gDRpdBFwg6Y" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/gDRpdBFwg6Y/maxresdefault.jpg" alt="プロンプト術20選" onerror="this.src='https://img.youtube.com/vi/gDRpdBFwg6Y/hqdefault.jpg'">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                </div>
                <p>動画で解説されている20のプロンプト要素です。AI動画の意図を正確にコントロールするための必修テクニック集です。</p>
            </div>
            
            <div class="glass-card">
                <div class="card-header"><i class="fa-solid fa-list-check"></i><h2>20のテクニック</h2></div>
"""

timestamps_20 = [
    ("01:04", "①世界観を指定", "動画全体の雰囲気や時代背景、場所のコンセプトを明確にします。"),
    ("02:20", "②表情を指定", "被写体の感情を制御し、物語性を追加します。"),
    ("03:47", "③トーン＆ジャンルを指定", "「シネマティック」「アニメ風」など映像のスタイルを決定します。"),
    ("05:04", "④キャラクターの固定", "同一人物を別のシーンでも破綻させずに登場させるテクニック。"),
    ("06:24", "⑤画角をロック", "意図しないカメラの引きや寄りを防ぎます。"),
    ("07:41", "⑥小さな動きに限定", "AIの破綻を防ぐため、最初は「まばたき」など小さな動きから指示します。"),
    ("08:54", "⑦オブジェクト数の制限", "要素が多すぎるとAIが混乱するため、画面内の主役を絞ります。"),
    ("09:56", "⑧スピードを指定", "「スローモーション」や「タイムラプス」など時間の流れを制御します。"),
    ("10:46", "⑨照明を指定", "「ゴールデンアワー」「スタジオ照明」など光と影で質感を高めます。"),
    ("11:51", "⑩開始と終了を指定", "動画の最初のフレームと最後のフレームを明示し、ストーリーを作ります。"),
    ("13:16", "⑪背景の動きを指定", "被写体だけでなく、背景の「木の揺れ」「通行人」などを制御します。"),
    ("14:24", "⑫重力・物理法則を指定", "「水しぶき」「髪のなびき」など、リアルな物理現象をプロンプトで補強。"),
    ("15:36", "⑬カメラワークを指定", "パンやズームなど、プロのカメラマンのような視点移動を追加します。"),
    ("16:38", "⑭視線の行き先を指定", "被写体がどこを見ているかを指定し、視聴者の視線を誘導します。"),
    ("17:38", "⑮表情を指定 (微細な変化)", "動画内で表情が「真顔から笑顔へ」変化するような過程を指示。"),
    ("18:33", "⑯禁止事項を指定", "「文字を入れない」「変形しない」などネガティブプロンプトの活用。"),
    ("20:24", "⑰動きを指定(テキストのみ)", "特定の動詞を用いて、複雑な動作をテキストだけで高精度に実現。"),
    ("21:29", "⑱動きを指定(モーションコントロール)", "AIツールのモーションブラシ機能などとプロンプトを併用。"),
    ("22:51", "⑲音声を指定", "生成後にリップシンク等で繋げるための「喋っている口元」の指定。"),
    ("24:36", "⑳動画の続きを指定", "生成された動画の延長(Extend)時のプロンプトのコツ。")
]

for time, title, desc in timestamps_20:
    seconds = int(time.split(":")[0]) * 60 + int(time.split(":")[1])
    html_content += f"""
            <details class="prompt-accordion">
                <summary><span class="tag">{time}</span> {title} <i class="fa-solid fa-chevron-down"></i></summary>
                <div class="prompt-content">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:10px;">
                        <p style="margin-top:0; flex-grow:1;"><strong>解説:</strong> {desc}</p>
                        <a href="https://www.youtube.com/watch?v=gDRpdBFwg6Y&t={seconds}s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 動画の {time} から見る</a>
                    </div>
                </div>
            </details>"""

html_content += """
            </div>
        </div>

        <div id="tab2" class="tab-content">
            <div class="glass-card">
                <div class="card-header"><i class="fa-brands fa-youtube" style="color:#ef4444;"></i><h2>AI動画の“動きの質”が激変。カメラワーク＆プロンプト超解説【Kling AI】</h2></div>
                <div class="video-grid" style="grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));">
                    <a href="https://youtu.be/stgEbOmqL1A" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/stgEbOmqL1A/maxresdefault.jpg" alt="カメラワーク＆プロンプト超解説" onerror="this.src='https://img.youtube.com/vi/stgEbOmqL1A/hqdefault.jpg'">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                </div>
            </div>

            <div class="glass-card">
                <div class="card-header"><i class="fa-solid fa-video"></i><h2>カメラワークと動きの制御</h2></div>
"""

camera_times = [
    ("0:37", "基本のカメラワーク", "Kling AI等で使える基本的なカメラ表現（パン、ティルト、ズーム等）。"),
    ("2:29", "カメラワークの悩み全解決", "よくある「意図しない動き」を制御し、安定させるテクニック。"),
    ("4:09", "シーンコンテキストの追加", "画面の周囲の状況や文脈を指示し、より豊かな映像にする。"),
    ("6:32", "思い通りの動画に近づける５つのポイント", "最終的なクオリティを底上げするための必須チェックリスト。")
]

for time, title, desc in camera_times:
    parts = time.split(":")
    seconds = int(parts[0]) * 60 + int(parts[1])
    html_content += f"""
            <details class="prompt-accordion">
                <summary><span class="tag">{time}</span> {title} <i class="fa-solid fa-chevron-down"></i></summary>
                <div class="prompt-content">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:10px;">
                        <p style="margin-top:0; flex-grow:1;"><strong>解説:</strong> {desc}</p>
                        <a href="https://www.youtube.com/watch?v=stgEbOmqL1A&t={seconds}s" target="_blank" class="yt-time-btn"><i class="fa-brands fa-youtube"></i> 動画の {time} から見る</a>
                    </div>
                </div>
            </details>"""

html_content += """
            </div>

            <div class="glass-card">
                <div class="card-header"><i class="fa-brands fa-youtube" style="color:#ef4444;"></i><h2>背景もアングルも“3D”で完全支配。３D生成連携</h2></div>
                <div class="video-grid" style="grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));">
                    <a href="https://youtu.be/NfM2x5RqmUI" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/NfM2x5RqmUI/maxresdefault.jpg" alt="3D生成×Gemini連携" onerror="this.src='https://img.youtube.com/vi/NfM2x5RqmUI/hqdefault.jpg'">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                </div>
                <div style="margin-top:20px; display:flex; gap:15px;">
                    <a href="https://www.hitem3d.ai/" target="_blank" class="tab-btn" style="text-decoration:none;"><i class="fa-solid fa-cube"></i> Hitem3D サイトへ</a>
                    <a href="https://www.blender.org/" target="_blank" class="tab-btn" style="text-decoration:none;"><i class="fa-solid fa-cubes"></i> Blender サイトへ</a>
                </div>
            </div>
        </div>

        <div id="tab3" class="tab-content">
            <div class="glass-card">
                <div class="card-header"><i class="fa-solid fa-list-ol"></i><h2>後半実習：プロンプト学習用再生リスト</h2></div>
                <p>以下の再生リストを視聴しながら、学んだプロンプト技術をノートにまとめましょう。</p>
                <a href="https://www.youtube.com/playlist?list=PLoQApr14fceM1VnrF1uTVceOH_56bBha0" target="_blank" class="tab-btn" style="display:inline-block; font-size:1.2rem; margin-top:10px; text-decoration:none; background:var(--accent); color:#fff;">
                    <i class="fa-brands fa-youtube"></i> 後半 実習プレイリストを開く
                </a>
                <br><br>
                <div class="intention">
                    <strong><i class="fa-solid fa-pen-to-square"></i> 実習の目的：</strong><br>
                    生成のコツを理解し、学んだ内容を自分用の「プロンプトノート」としてまとめ、後から仕事や制作ですぐに引き出せるようにしておくこと。
                </div>
            </div>
        </div>
    </div>
    
    <a href="index.html" class="home-btn" title="Back to Home"><i class="fa-solid fa-house"></i></a>

    <script>
        function switchTab(tabId) {
            document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
            
            event.currentTarget.classList.add('active');
            document.getElementById(tabId).classList.add('active');

            if (tabId === 'tab1') document.getElementById('progress-bar').style.width = '33%';
            if (tabId === 'tab2') document.getElementById('progress-bar').style.width = '66%';
            if (tabId === 'tab3') document.getElementById('progress-bar').style.width = '100%';
            
            document.getElementById('progress-percent').innerText = document.getElementById('progress-bar').style.width;
        }

        function copyPrompt(btn) {
            const pre = btn.nextElementSibling;
            const text = pre.innerText;
            navigator.clipboard.writeText(text).then(() => {
                const originalHtml = btn.innerHTML;
                btn.innerHTML = '<i class="fa-solid fa-check"></i> Copied!';
                btn.style.background = 'rgba(16, 185, 129, 0.2)';
                btn.style.borderColor = 'var(--accent)';
                btn.style.color = 'var(--accent-light)';
                setTimeout(() => {
                    btn.innerHTML = originalHtml;
                    btn.style = '';
                }, 2000);
            });
        }
    </script>
</body>
</html>
"""

with open(os.path.join(r"g:\マイドライブ\研修\【202603】生成AIとプロンプト", "vol05-1_text_to_video.html"), "w", encoding="utf-8") as f:
    f.write(html_content)

print("vol05-1_text_to_video.html created successfully.")
