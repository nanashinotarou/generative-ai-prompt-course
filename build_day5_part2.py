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
                    お疲れ様でした！本日は**「テキストから動画への変換技術の基礎とカメラワーク」**について学びました。<br>
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

with open("build_day5_part2.py", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated build_day5_part2.py")
