import re

with open("vol10-1_ai_business.html", "r", encoding="utf-8") as f:
    text1 = f.read()
with open("vol10-2_ai_business_practice.html", "r", encoding="utf-8") as f:
    text2 = f.read()

# CSS Merging
match1 = re.search(r"<style>(.*?)</style>", text1, re.DOTALL)
match2 = re.search(r"<style>(.*?)</style>", text2, re.DOTALL)
css1 = match1.group(1) if match1 else ""
css2 = match2.group(1) if match2 else ""

# Add unique CSS rules from css2 to css1
new_css_rules = ""
for css_rule in ['.diagram-comparison', '.comparison-row', '.c-label', '.c-flow', '.d-node.goal']:
    lines = [line for line in css2.split('\n') if css_rule in line]
    if lines:
        new_css_rules += "\n" + "\n".join(lines)

final_css = css1 + new_css_rules

# Header
html_header = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day 10 | AI Business Application & Strategy</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Noto+Sans+JP:wght@400;500;700&family=Teko:wght@500;600;700&family=Fira+Code&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>""" + final_css + """
    </style>
</head>
<body>
    <canvas id="particles"></canvas><canvas id="confetti"></canvas>
    <div id="scroll-progress-container"><div id="scroll-progress-bar"></div></div>

    <header class="fixed-header">
        <a href="index.html" class="back-link"><i class="fa-solid fa-arrow-left"></i> Course Home</a>
        <div class="progress-container">
            <div class="progress-text"><span>Day 10 Progress</span><span id="progress-percent">0%</span></div>
            <div class="progress-bar-bg"><div class="progress-bar-fill" id="progress-bar"></div></div>
        </div>
        <div style="width:100px;"></div>
    </header>

    <div class="container">
        <div class="hero">
            <div class="day-badge">DAY 10</div>
            <h1>共同作業AIのビジネスへの応用</h1>
            <p>本日の目標：AIを「なんとなく便利なツール」から<strong>ビジネスの武器</strong>に変える。<br>5つのレベルで自分の現在地を把握し、ビジネス現場で即使える「Notion AI」などのAIエージェントの具体的なプロセスを手に入れましょう。</p>
        </div>

        <div class="tab-nav">
            <button class="tab-btn active" onclick="switchTab('tab-goal')"><i class="fa-solid fa-bullseye" style="color:#f59e0b;"></i> コース目標</button>
            <button class="tab-btn" onclick="switchTab('tab-first')"><i class="fa-solid fa-briefcase" style="color:#10b981;"></i> 前半：AIビジネス活用</button>
            <button class="tab-btn" onclick="switchTab('tab-second')"><i class="fa-solid fa-bolt" style="color:#0ea5e9;"></i> 後半：AIエージェント実戦</button>
            <button class="tab-btn" onclick="switchTab('tab-summary')"><i class="fa-solid fa-flag-checkered" style="color:#8b5cf6;"></i> 今日のまとめ</button>
        </div>

        <!-- TAB 1: COURSE GOALS -->
        <div id="tab-goal" class="tab-content active">
            <div class="glass-card" style="border-top: 5px solid #10b981;">
                <div class="card-header"><i class="fa-solid fa-compass" style="color:#10b981; background:#ecfdf5;"></i><h2>本日の研修ねらい</h2></div>
                <div class="info-box" style="border-left-color: #10b981; background: #ecfdf5;">
                    <h4 style="color:#059669;"><i class="fa-solid fa-stairs"></i> 【前半】「なんとなくAIを触る」からの卒業</h4>
                    <p style="color:#064e3b;">
                        AIには5つの活用レベルがあります。検索代わりに使うレベル1から、独自ツールを開発するレベル5まで――今日は「AI活用で成果を出す5階層ロードマップ」を軸に、あなたの現在地を把握し、ビジネスの鉄則を学びます。
                    </p>
                </div>
                <div class="info-box" style="border-left-color: #0ea5e9; background: #f0f9ff; margin-top:2rem;">
                    <h4 style="color:#0078d4;"><i class="fa-solid fa-robot"></i> 【後半】5階層ロードマップのその先へ</h4>
                    <p style="color:#004b87;">
                        AIが単なる「相談相手」としてではなく、手順を自ら考え目標遂行する<strong>AIエージェント</strong>の世界を体験しましょう。最新の活用事例と <strong>Notion AI</strong> の使いこなし方をマスターします。
                    </p>
                </div>

                <div class="bento-grid">
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-layer-group" style="color:#10b981;"></i> 5階層ロードマップ</h4>
                        <p>段階的にスキルアップする道筋を学び、自分の現在地と次のアクションが明確になります。</p>
                    </div>
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-shield-halved" style="color:#0d9488;"></i> ビジネスの鉄の掟</h4>
                        <p>目的設定、機密情報の取り扱い、人間による最終確認――絶対に外せない3つの原則を習得します。</p>
                    </div>
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-robot" style="color:#0ea5e9;"></i> AIエージェント事例</h4>
                        <p>リサーチ、CS、データ分析からSNS運用まで、AIが自律稼働する8つの事例を紹介します。</p>
                    </div>
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-notion" style="color:#0078d4;"></i> Notion AI 実践活用</h4>
                        <p>データベースとの強力な連携（Autofill）や社内情報のハブにAIを組み込む方法を学びます。</p>
                    </div>
                </div>
            </div>
            <div style="text-align:center; margin-top:3rem;">
                <button class="btn" style="padding: 1rem 3rem; font-size:1.2rem; border-radius:30px;" onclick="switchTab('tab-first'); window.scrollTo(0, 0);">
                    前半の実習へ進む <i class="fa-solid fa-arrow-right"></i>
                </button>
            </div>
        </div>
"""

# Tab 2 (First Half)
m1 = re.search(r'<!-- TAB 2: FIRST HALF -->(.*?)<!-- TAB 3: SUMMARY -->', text1, re.DOTALL)
if m1:
    tab_first = m1.group(1)
    tab_first = tab_first.replace(
        """<button class="btn" style="padding: 1rem 3rem; font-size:1.2rem; background:linear-gradient(135deg, #10b981, #0d9488); border-radius:30px; box-shadow: 0 5px 15px rgba(16,185,129,0.3);" onclick="switchTab('tab-summary'); window.scrollTo(0,0);">
                    本日のまとめを見る""",
        """<button class="btn" style="padding: 1rem 3rem; font-size:1.2rem; background:linear-gradient(135deg, #0ea5e9, #0284c7); border-radius:30px; box-shadow: 0 5px 15px rgba(14,165,233,0.3);" onclick="switchTab('tab-second'); window.scrollTo(0,0);">
                    後半の実習へ進む"""
    )
    html_header += "<!-- TAB 2: FIRST HALF -->\n" + tab_first

# Tab 3 (Second Half)
m2 = re.search(r'<!-- TAB 2: SECOND HALF -->(.*?)<!-- TAB 3: SUMMARY -->', text2, re.DOTALL)
if m2:
    tab_second = m2.group(1)
    tab_second = tab_second.replace(
        "id=\"tab-second\"", "id=\"tab-second\"") # Just making sure
    tab_second = tab_second.replace(
        """<button class="btn" style="padding: 1rem 3rem; font-size:1.2rem; background:linear-gradient(135deg, #10b981, #0d9488); border-radius:30px; box-shadow: 0 5px 15px rgba(16,185,129,0.3);" onclick="switchTab('tab-summary2'); window.scrollTo(0,0);">
                    全行程の修了報告へ""",
        """<button class="btn" style="padding: 1rem 3rem; font-size:1.2rem; background:linear-gradient(135deg, #8b5cf6, #6d28d9); border-radius:30px; box-shadow: 0 5px 15px rgba(139,92,246,0.3);" onclick="switchTab('tab-summary'); window.scrollTo(0,0);">
                    本日のまとめを見る"""
    )
    html_header += "<!-- TAB 3: SECOND HALF -->\n" + tab_second

# Tab 4 (Summary)
html_summary = """
        <!-- TAB 4: SUMMARY -->
        <div id="tab-summary" class="tab-content">
            <div class="glass-card" style="border: 2px solid #8b5cf6; background: linear-gradient(to bottom, #ffffff, #f5f3ff); overflow: hidden; padding: 0;">
                <div style="background: linear-gradient(135deg, #8b5cf6, #6d28d9); color: white; padding: 4rem 2rem; text-align: center; position: relative; overflow: hidden;">
                    <div style="position: absolute; top: -50px; right: -50px; font-size: 15rem; color: rgba(255,255,255,0.1); transform: rotate(15deg);"><i class="fa-solid fa-rocket"></i></div>
                    <div style="position: absolute; bottom: -30px; left: -20px; font-size: 8rem; color: rgba(255,255,255,0.1); transform: rotate(-10deg);"><i class="fa-solid fa-briefcase"></i></div>
                    <div class="wax-seal" style="background: radial-gradient(circle at 30% 30%, #fde68a, #f59e0b, #d97706); border-color:#fff; width: 100px; height: 100px; margin: 0 auto 1.5rem; position: relative; float: none; opacity:1; transform:none;"><i class="fa-solid fa-medal" style="font-size: 3rem;"></i></div>
                    <h2 style="font-size: 2.5rem; font-weight: 900; margin-bottom: 0.5rem; text-shadow: 0 2px 10px rgba(0,0,0,0.2);">DAY 10 ALL COMPLETE!</h2>
                    <p style="font-size: 1.2rem; opacity: 0.9;">AIビジネス活用の理論と実践の全工程を修了しました</p>
                </div>
                
                <div style="padding: 3rem 2rem;">
                    <h3 style="text-align: center; color: #4c1d95; font-size: 1.8rem; margin-bottom: 2.5rem;"><i class="fa-solid fa-star" style="color:#8b5cf6;"></i> あなたはAIマネージャーの第一歩を踏み出しました</h3>
                    <div class="info-box" style="border-left-color: #8b5cf6; background: #f5f3ff; margin-top: 2rem;">
                        <h4 style="color:#6d28d9;"><i class="fa-solid fa-check-double"></i> 習得したスキル</h4>
                        <p style="color:#4c1d95;">
                            ・5階層ロードマップによる自己分析と次の一手<br>
                            ・機密情報保護とファクトチェックの「鉄の掟」<br>
                            ・自ら考えて実行する「AIエージェント」の概念と事例<br>
                            ・Notion AIによるデータベースの自動化と情報活用
                        </p>
                    </div>

                    <div style="text-align: center; margin-top: 3rem; display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
                        <button class="btn" style="padding: 1.2rem 3rem; font-size: 1.2rem; background: linear-gradient(135deg, #10b981, #059669); border-radius: 50px; box-shadow: 0 10px 30px rgba(16,185,129,0.4); font-weight: 900;" onclick="window.location.href='index.html'">
                            <i class="fa-solid fa-house"></i> Homeへ戻る
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <a href="index.html" class="home-btn" title="Back to Home"><i class="fa-solid fa-house"></i></a>

    <script>
        function switchTab(tabId) { document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active')); document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active')); document.getElementById(tabId).classList.add('active'); const tabMap = {'tab-goal': 0, 'tab-first': 1, 'tab-second': 2, 'tab-summary': 3}; document.querySelectorAll('.tab-btn')[tabMap[tabId]].classList.add('active'); updateProgress(); }
        function checkQuiz(quizId, el, isCorrect) { const container = document.getElementById(quizId); if (container.dataset.answered) return; container.dataset.answered = 'true'; if (isCorrect) { el.classList.add('correct'); el.querySelector('i').style.display = 'inline'; } else { el.classList.add('wrong'); el.querySelector('i').style.display = 'inline'; container.querySelectorAll('.quiz-opt').forEach(opt => { if (opt.onclick.toString().includes('true')) { opt.classList.add('correct'); opt.querySelector('i').style.display = 'inline'; } }); } document.getElementById(quizId + '-explain').style.display = 'block'; }
        const taskState = {};
        function toggleTask(id, el, group) { taskState[id] = !taskState[id]; el.classList.toggle('completed'); updateProgress(); const groupId = 'mission-group-' + group; const groupEl = document.getElementById(groupId); const items = groupEl.querySelectorAll('.task-item'); const done = groupEl.querySelectorAll('.task-item.completed').length; if (done === items.length) { groupEl.classList.add('completed'); launchConfetti(); } else { groupEl.classList.remove('completed'); } }
        function updateProgress() { const total = document.querySelectorAll('.task-item').length; const done = document.querySelectorAll('.task-item.completed').length; const pct = total === 0 ? 0 : Math.round((done / total) * 100); document.getElementById('progress-percent').innerText = pct + '%'; document.getElementById('progress-bar').style.width = pct + '%'; }
        window.addEventListener('scroll', () => { const winScroll = document.body.scrollTop || document.documentElement.scrollTop; const height = document.documentElement.scrollHeight - document.documentElement.clientHeight; const scrolled = (winScroll / height) * 100; document.getElementById('scroll-progress-bar').style.width = scrolled + '%'; });
        function launchConfetti() { const canvas = document.getElementById('confetti'); const ctx = canvas.getContext('2d'); canvas.width = window.innerWidth; canvas.height = window.innerHeight; const particles = []; for(let i=0; i<100; i++) { particles.push({ x: canvas.width/2, y: canvas.height/2, r: Math.random()*6+2, dx: Math.random()*10-5, dy: Math.random()*-10-5, color: ['#10b981','#0d9488','#059669','#f43f5e','#fbbf24'][Math.floor(Math.random()*5)] }); } function animate() { ctx.clearRect(0,0,canvas.width,canvas.height); let active = false; particles.forEach(p => { if(p.y < canvas.height) { active = true; p.x += p.dx; p.y += p.dy; p.dy += 0.2; ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, Math.PI*2); ctx.fillStyle = p.color; ctx.fill(); } }); if(active) requestAnimationFrame(animate); else ctx.clearRect(0,0,canvas.width,canvas.height); } animate(); }
    </script>
</body>
</html>
"""

html_full = html_header + html_summary

with open("vol10-1_ai_business.html", "w", encoding="utf-8") as f:
    f.write(html_full)

print("Merged successfully!")
