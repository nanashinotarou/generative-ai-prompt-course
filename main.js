document.addEventListener('DOMContentLoaded', () => {

    // --- HOME BUTTON (Unchanged) ---
    if (!window.location.pathname.endsWith('index.html')) {
        const btn = document.createElement('a');
        btn.href = 'index.html';
        btn.innerHTML = '<i class="fa-solid fa-house"></i>';
        Object.assign(btn.style, { position: 'fixed', bottom: '20px', right: '20px', width: '50px', height: '50px', background: '#4f46e5', color: '#fff', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '1.2rem', boxShadow: '0 4px 12px rgba(79,70,229,0.3)', textDecoration: 'none', zIndex: '999' });
        document.body.appendChild(btn);
    }

    // --- QUIZ ENGINE ---
    function initQuiz(id, data) {
        const el = document.getElementById(id);
        if (!el) return;

        // Ensure data is tiered
        data.forEach(q => { if (!q.tier) q.tier = 1; });
        const hasMultipleTiers = data.some(q => q.tier > 1);

        // Initial DOM Setup
        if (!el.querySelector('.quiz-container')) {
            el.innerHTML = `
                ${hasMultipleTiers ? `
                <div class="tier-selector" style="display:flex; justify-content:center; gap:10px; margin-bottom: 20px;">
                    <button class="tier-btn active" data-t="1">🌱 初級</button>
                    <button class="tier-btn" data-t="2">🚀 中級</button>
                    <button class="tier-btn" data-t="3">🔥 上級</button>
                </div>
                ` : ''}
                <div class="quiz-container"></div>
            `;

            // Add global tier styles if not present
            if (!document.getElementById('quiz-tier-styles')) {
                const style = document.createElement('style');
                style.id = 'quiz-tier-styles';
                style.innerHTML = `
                    .tier-btn { padding: 8px 20px; border-radius: 20px; border: 1px solid #e2e8f0; background: #fff; color: #64748b; cursor: pointer; font-weight: bold; transition: all 0.3s; font-size: 0.95rem; }
                    .tier-btn.active { background: #818cf8; color: #fff; border-color: #818cf8; box-shadow: 0 4px 15px rgba(129, 140, 248, 0.4); }
                    .tier-btn:hover:not(.active) { background: #f8fafc; border-color: #cbd5e1; }
                    @keyframes quizFadeIn { from { opacity: 0; transform: translateY(5px); } to { opacity: 1; transform: translateY(0); } }
                `;
                document.head.appendChild(style);
            }
        }

        const container = el.querySelector('.quiz-container');
        let idx = 0, score = 0, activeData = [];

        const startQuiz = (tier) => {
            idx = 0; score = 0;
            let filtered = data.filter(q => q.tier === tier);
            if (filtered.length === 0) filtered = data.filter(q => q.tier === 1);
            if (filtered.length === 0) filtered = data;

            // Fisher-Yates Shuffle
            let shuffled = [...filtered];
            for (let i = shuffled.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
            }
            activeData = shuffled;
            render();
        };

        if (hasMultipleTiers) {
            el.querySelectorAll('.tier-btn').forEach(b => {
                b.addEventListener('click', (e) => {
                    el.querySelectorAll('.tier-btn').forEach(btn => btn.classList.remove('active'));
                    e.target.classList.add('active');
                    startQuiz(parseInt(e.target.dataset.t));
                });
            });
        }

        const render = () => {
            // --- RESULT SCREEN ---
            if (idx >= activeData.length) {
                container.innerHTML = `
                    <div style="text-align:center; padding:40px 20px; background:#fff !important; border-radius:12px; border:1px solid #ddd; color:#333 !important; animation: quizFadeIn 0.5s ease-out;">
                        <h3 style="color:#333 !important; margin:0 0 15px 0;">🎯 Result: <span style="color:#818cf8; font-size:2rem;">${score}</span> / ${activeData.length * 10}</h3>
                        <p style="color:#64748b; margin-bottom: 30px;">${score === activeData.length * 10 ? '全問正解！素晴らしいです！✨' : 'もう一度チャレンジして満点を目指しましょう！💪'}</p>
                        <button class="retry-btn" style="padding:12px 30px; background:#2d3436 !important; color:#fff !important; border:none; border-radius:30px; cursor:pointer; font-weight:bold; font-size:1rem; transition: 0.3s; box-shadow: 0 4px 10px rgba(0,0,0,0.2);">もう一度挑戦する</button>
                    </div>`;

                container.querySelector('.retry-btn').addEventListener('click', () => {
                    const currentTierBtn = el.querySelector('.tier-btn.active');
                    startQuiz(currentTierBtn ? parseInt(currentTierBtn.dataset.t) : 1);
                });
                return;
            }

            const q = activeData[idx];

            // --- QUESTION SCREEN ---
            const optionsHtml = Object.entries(q.options).map(([k, v]) => `
                <button class="opt-btn" data-k="${k}" style="
                    display:block; width:100%; padding:15px 20px; margin-bottom:10px;
                    background: #ffffff !important; 
                    color: #333333 !important; 
                    border: 2px solid #e0e0e0 !important; 
                    border-radius: 8px; 
                    text-align: left; 
                    cursor: pointer; 
                    font-weight: bold;
                    font-size: 1rem;
                    transition: all 0.2s;
                ">
                    <span style="color:#00bcd4; margin-right:10px;">${k}.</span> ${v}
                </button>
            `).join('');

            container.innerHTML = `
                <div style="background:#fff; padding:20px; border-radius:10px; animation: quizFadeIn 0.3s ease-out;">
                    <p style="font-weight:bold; margin-bottom:20px; font-size:1.15rem; color:#333 !important; line-height: 1.6;">
                        <span style="display:inline-block; background:#f1f5f9; padding:3px 12px; border-radius:12px; font-size:0.8rem; color:#64748b; margin-bottom:12px; font-family:'Teko', sans-serif; letter-spacing:1px;">Q${idx + 1} OF ${activeData.length}</span><br>
                        ${q.q}
                    </p>
                    <div style="display:grid; gap:0;">
                        ${optionsHtml}
                    </div>
                    <div class="feedback-box" style="
                        display:none; 
                        margin-top:20px; 
                        padding:25px; 
                        background: #2d3436 !important; 
                        color: #ffffff !important;
                        border-radius: 12px;
                        line-height: 1.6;
                        border: 2px solid #2d3436;
                        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                        animation: quizFadeIn 0.3s ease-out;
                    "></div>
                </div>
            `;

            // Event Listeners for Options
            container.querySelectorAll('.opt-btn').forEach(b => {
                b.addEventListener('mouseover', () => { if (!b.disabled) { b.style.borderColor = '#00bcd4'; b.style.background = '#f0fbff'; } });
                b.addEventListener('mouseout', () => { if (!b.disabled) { b.style.borderColor = '#e0e0e0'; b.style.background = '#ffffff'; } });
                b.addEventListener('click', (e) => { const target = e.target.closest('.opt-btn'); check(target.dataset.k); });
            });
        };

        const check = (ans) => {
            const q = activeData[idx];
            const fb = container.querySelector('.feedback-box');
            const isCorrect = ans === q.correct;
            if (isCorrect) score += 10;

            const statusBadge = isCorrect
                ? `<span style="display:inline-block; background:#00bcd4 !important; color:#fff !important; padding:5px 15px; border-radius:20px; font-size:0.9rem; font-weight:bold; letter-spacing:1px;"><i class="fa-solid fa-circle-check"></i> CORRECT!</span>`
                : `<span style="display:inline-block; background:#ff7675 !important; color:#fff !important; padding:5px 15px; border-radius:20px; font-size:0.9rem; font-weight:bold; letter-spacing:1px;"><i class="fa-solid fa-circle-xmark"></i> INCORRECT...</span>`;

            fb.innerHTML = `
                <div style="margin-bottom:15px; border-bottom:1px solid rgba(255,255,255,0.2); padding-bottom:15px; display:flex; justify-content:space-between; align-items:center;">
                    ${statusBadge}
                </div>
                <p style="color: #ffffff !important; margin:0; font-weight:normal; font-size:1.05rem;">
                    ${q.rationale}
                </p>
                <button class="next-btn" style="
                    margin-top:20px; 
                    padding:12px 35px; 
                    background: #ffffff !important; 
                    color: #2d3436 !important; 
                    border: none; 
                    border-radius: 30px; 
                    cursor: pointer; 
                    font-weight: bold;
                    transition: 0.2s;
                ">次へ進む <i class="fa-solid fa-arrow-right"></i></button>
            `;
            fb.style.display = 'block';

            fb.querySelector('.next-btn').addEventListener('click', () => {
                idx++;
                render();
            });

            // Lock Buttons
            container.querySelectorAll('.opt-btn').forEach(b => {
                b.disabled = true;
                b.style.cursor = 'default';
                if (b.dataset.k === q.correct) {
                    b.style.background = '#00bcd4 !important'; b.style.color = '#fff !important'; b.style.borderColor = '#00bcd4 !important'; b.querySelector('span').style.color = '#fff';
                } else if (b.dataset.k === ans) {
                    b.style.background = '#ff7675 !important'; b.style.color = '#fff !important'; b.style.borderColor = '#ff7675 !important'; b.querySelector('span').style.color = '#fff';
                } else {
                    b.style.opacity = '0.4';
                }
            });
        };

        startQuiz(1);
    }

    // --- QUIZ DATA (Vol.1: Gemini & TikTok Start) ---
    initQuiz('quiz-vol01-1', [
        // 初級 (Tier 1)
        { tier: 1, q: "Geminiを使用するために必須のアカウントは？", options: { A: "TikTok", B: "Microsoft", C: "Google", D: "OpenAI" }, correct: "C", rationale: "GeminiはGoogleが提供するサービスであるため、Googleアカウントが必要です。" },
        { tier: 1, q: "今回の研修コース目標として設定されている「動画投稿数」は？", options: { A: "毎日投稿（30本）", B: "期間中に1本", C: "期間中に10本", D: "期間中に3本以上" }, correct: "D", rationale: "まずは質より量、そして慣れが必要です。「3本以上」が目標です。" },
        // 中級 (Tier 2)
        { tier: 2, q: "TikTokの「ユーザー名（@マーク以降）」を変更する際の制限として正しいものはどれですか？", options: { A: "何度でも自由に変更できる", B: "30日に1回のみ変更可能", C: "一度設定したら二度と変更できない", D: "有料プランでのみ変更可能" }, correct: "B", rationale: "ユーザー名はURLの一部にもなるため、頻繁な変更は制限されています（30日に1回）。" },
        { tier: 2, q: "TikTokのリサーチ（探索）を行う主な目的として、初期段階で最も重要なのは？", options: { A: "競合の動画に低評価を押すため", B: "流行っている曲や動画のスタイルを知り、自分の企画の参考にするため", C: "コメント欄で自分のチャンネルを宣伝するため", D: "単に時間を潰すため" }, correct: "B", rationale: "「今何がウケているか」というトレンド感覚を養うことが、伸びる動画を作る第一歩です。" },
        // 上級 (Tier 3)
        { tier: 3, q: "Geminiが得意とする「マルチモーダル」とはどういう意味ですか？", options: { A: "複数の言語を翻訳できること", B: "テキストだけでなく、画像や音声など複数の種類の情報を扱えること", C: "複数のユーザーで同時に作業できること", D: "複数のアプリを同時に起動できること" }, correct: "B", rationale: "テキスト、コード、画像、音声、動画など、異なる形式のデータを理解・生成できる能力を指します。" },
        { tier: 3, q: "生成AIに対する効果的な「プロンプト」の原則として最も適切なのは？", options: { A: "できるだけ単語のみで短く伝える", B: "役割、目的、条件などを明確に構造化して伝える", C: "敬語をたくさん使って丁寧に頼む", D: "結果が出るまで何度も同じ指示を繰り返す" }, correct: "B", rationale: "生成AIへは、前提条件や出力形式を明確に指定することで、より精度の高い回答を得ることができます。" }
    ]);

    // --- QUIZ DATA (Vol.1 Day 2: Algorithm & Canva) ---
    initQuiz('quiz-vol01-2', [
        { q: "TikTokのアルゴリズムは何方式で評価される？", options: { A: "減点方式", B: "加算方式", C: "ランダム", D: "年功序列" }, correct: "B", rationale: "TikTokは「減点」ではなく、ユーザーの好意的なアクションを「加算」していく方式です。誰にでもチャンスがあります。" },
        { q: "動画が最初にテスト配信される規模は？", options: { A: "全ユーザー", B: "1万人", C: "200〜300人", D: "フォロワーのみ" }, correct: "C", rationale: "まずは200〜300人の少人数に配信され、そこでの反応が良ければ次のステージへ拡散されます（スモールスタート）。" },
        { q: "CanvaでTikTok用動画を作る際、選ぶべきキャンバスサイズは？", options: { A: "Instagramリール動画 (9:16)", B: "YouTube動画 (16:9)", C: "正方形 (1:1)", D: "A4用紙" }, correct: "A", rationale: "TikTokやInstagramリールは「9:16（縦長）」が標準です。スマホの画面全体を使うことで没入感を高めます。" },
        { q: "動画内のテロップ（文字）で重要な「タイミング調整」とは？", options: { A: "常に表示し続けること", B: "話している内容に合わせて表示/非表示を切り替えること", C: "点滅させること", D: "半透明にすること" }, correct: "B", rationale: "「耳で聞いている言葉」と「目で見ている文字」を一致させることで、脳への負担を減らし、視聴維持率を高めることができます。" },
        { q: "今回のコース目標における「動画投稿数」は？", options: { A: "1本", B: "3本以上", C: "毎日投稿", D: "100本" }, correct: "B", rationale: "「習うより慣れろ」です。失敗を恐れず、まずは3本投稿して反応を見る体験を重視しています。" }
    ]);


    // --- SYNCHRONIZED HIGHLIGHTING (No Auto-Scroll Version) ---
    // User Agency over generic automation.

    const toggleHighlight = (id, isActive) => {
        if (!id) return;
        const targetCell = document.querySelector(`.cal-cell[data-day="${id}"]`);
        const targetItem = document.getElementById(id);

        // Toggle class only (No scrollIntoView)
        if (targetCell) targetCell.classList.toggle('active-sync', isActive);
        if (targetItem) targetItem.classList.toggle('active-sync', isActive);
    };

    // 1. Hover on Calendar
    document.querySelectorAll('.cal-cell.has-event').forEach(cell => {
        cell.addEventListener('mouseenter', () => toggleHighlight(cell.dataset.day, true));
        cell.addEventListener('mouseleave', () => toggleHighlight(cell.dataset.day, false));
    });

    // 2. Hover on List
    document.querySelectorAll('.c-item').forEach(item => {
        item.addEventListener('mouseenter', () => toggleHighlight(item.id, true));
        item.addEventListener('mouseleave', () => toggleHighlight(item.id, false));
    });

    // --- HIGHLIGHT TODAY (Valid until Apr 4, 2026) ---
    const highlightToday = () => {
        const today = new Date();
        // Check if year is 2026 (Strict constraint)
        if (today.getFullYear() !== 2026) return;

        const m = today.getMonth(); // 0=Jan, 1=Feb, 2=Mar, 3=Apr
        const d = today.getDate();
        let targetCell = null;

        if (m === 2) { // March
            // Find regular cell with this number (excluding other-month cells)
            const cells = document.querySelectorAll('.cal-cell:not(.other-month)');
            cells.forEach(c => {
                const numSpan = c.querySelector('.date-num');
                if (numSpan && parseInt(numSpan.textContent) === d) {
                    targetCell = c;
                }
            });
        } else if (m === 3 && d <= 4) { // April 1st - 4th (Next Month display)
            // Apr 1-4 are shown as .other-month cells at the end
            const cells = document.querySelectorAll('.cal-cell.other-month');
            cells.forEach(c => {
                // These cells usually just have text "1", "2" etc.
                if (parseInt(c.textContent.trim()) === d) {
                    targetCell = c;
                }
            });
        }

        if (targetCell) {
            targetCell.classList.add('is-today');
        }
    };
    highlightToday();

    // --- AUTO-UPDATE LATEST BUTTON ---
    const updateLatestButton = async () => {
        const items = Array.from(document.querySelectorAll('.c-item'));
        let latestItem = null;
        let latestVolNum = 0;

        const checks = items.map(async (item) => {
            const url = item.getAttribute('href');
            if (!url || url === '#' || url.startsWith('javascript')) return null;
            try {
                const res = await fetch(url, { method: 'HEAD' });
                // Note: Cloudflare Pages might return 200 for 404 pages if custom 404 are set up,
                // or just standard 404 depending on the setup. Adding a check for actual text size or existance.
                // However, the simpler fix: only accept URLs that actually exist in the latest commit map,
                // or just rely on a stricter check (e.g. check if response URL wasn't redirected to a 404 page).
                if (res.ok) {
                    // Stricter parsing: Ensure it's not a placeholder link by checking if it contains 'vol'
                    if (url.includes('vol')) {
                        const volNum = parseInt(item.id.replace('d', ''));
                        // Very strict: Check if the file's content actually has the structure of our created pages
                        // We will just do a quick GET to check if it's the real file if we want to be 100% sure.
                        // But since we just want to avoid treating non-existent files as "Latest", and this environment serves them as real files maybe?
                        // Let's actually do a GET and check the title.
                        const getRes = await fetch(url);
                        if (getRes.ok) {
                            const text = await getRes.text();
                            if (text.includes('class="fixed-header"')) {
                                return { item, volNum };
                            }
                        }
                    }
                }
            } catch (e) {
                // Ignore fetch errors
            }
            return null;
        });

        const results = await Promise.all(checks);

        for (const res of results) {
            if (res && res.volNum > latestVolNum) {
                latestVolNum = res.volNum;
                latestItem = res.item;
            }
        }

        if (latestItem) {
            const latestUrl = latestItem.getAttribute('href');
            const btn = document.querySelector('.shortcut-btn');
            if (btn) {
                btn.href = latestUrl;
                btn.innerHTML = `<i class="fa-solid fa-play"></i> LATEST: Vol.${latestVolNum} テキストを開く`;
                btn.dataset.day = latestItem.id;

                btn.onmouseenter = () => toggleHighlight(latestItem.id, true);
                btn.onmouseleave = () => toggleHighlight(latestItem.id, false);
            }
        }
    };
    updateLatestButton();

    // --- DAY 2 QUIZ ---
    initQuiz('quiz-vol02-1', [
        {
            tier: 1,
            q: "Canvaの自動生成AI機能で、「デザイン内の不要なものをなぞるだけで消せる」機能の名前は？",
            options: { A: "マジック生成", B: "マジック消しゴム", C: "背景リムーバ", D: "マジック拡張" },
            correct: "B",
            rationale: "「マジック消しゴム」を使えば、写真に写り込んだ不要な人やモノを簡単になぞって消去し、背景を自然に補完できます。"
        },
        {
            tier: 2,
            q: "Canvaが買収した、AI機能以外は完全無料化されたプロフェッショナル向けデザインツールの名前は？",
            options: { A: "Adobe Illustrator", B: "Nano Banana", C: "Affinity", D: "Midjourney" },
            correct: "C",
            rationale: "Canvaは「Affinity」を買収し、教育機関やNPO、無料ユーザー向けにもAI機能以外のプロ向けツール一式を完全無料で提供開始しました。"
        },
        {
            tier: 3,
            q: "無料で使えるAI画像編集ツール「Nano Banana」の最大の特徴は？",
            options: { A: "動画編集に特化している", B: "Illustratorのようなベクター描画ができる", C: "プロンプト（テキスト指示）だけで高度な画像編集が完結する", D: "音楽を自動生成できる" },
            correct: "C",
            rationale: "Nano Bananaはテキスト指示（プロンプト）だけで、不要物の消去・背景の差し替え・画像の高画質化など、プロ級の編集が可能です。"
        }
    ]);

    // --- DAY 3 QUIZ ---
    initQuiz('quiz-vol01-3', [
        {
            tier: 1,
            q: "企画リサーチをする際、TikTokアプリ内で最初に使うべき機能は？",
            options: { A: "設定画面", B: "探索（トレンド）タブでの検索", C: "プロフィールの編集", D: "課金アイテムの購入" },
            correct: "B",
            rationale: "まずは「今、何が流行っているのか」を肌で感じることが重要です。探索タブでトレンドを把握しましょう。"
        },
        {
            tier: 1,
            q: "今回の研修（3日目）で設定された、最低限の動画アップロード本数は？",
            options: { A: "1本", B: "3本以上", C: "10本", D: "30本" },
            correct: "B",
            rationale: "質にこだわりすぎず、まずは「数を出す」経験を積むために、最低3本のアウトプットを目標としています。"
        },
        {
            tier: 2,
            q: "動画の冒頭で視聴者の興味を引き、指を止めさせる要素を何と呼ぶ？",
            options: { A: "フック", B: "クロージング", C: "CTA", D: "ハッシュタグ" },
            correct: "A",
            rationale: "釣り針（Hook）のように、視聴者の心を「引っかける」ための冒頭の工夫です。ここが弱いとすぐにスクロールされてしまいます。"
        },
        {
            tier: 3,
            q: "Canvaを使って、同じデザインの動画を大量に作る機能の名前は？",
            options: { A: "マジック作文", B: "一括作成 (Bulk Create)", C: "背景除去", D: "ブランドキット" },
            correct: "B",
            rationale: "「一括作成」機能を使えば、CSVなどを取り込んでデザインを量産できます。まさに「工場」のような機能です。"
        },
        {
            tier: 3,
            q: "Canvaの一括作成で、用意したデータを流し込むために必要な操作は？",
            options: { A: "画像を削除する", B: "右クリックして「データを接続」", C: "フォントを太字にする", D: "アニメーションを削除する" },
            correct: "B",
            rationale: "テンプレート上の要素を右クリックし、流し込みたいデータの項目と「接続」することで、一気に流し込みが可能になります。"
        }
    ]);

    // --- PORTAL COMPREHENSIVE QUIZ ---
    initQuiz('quiz-portal-main', [
        // 初級 (Tier 1)
        { tier: 1, q: "Geminiを使用するために必須のアカウントは？", options: { A: "TikTok", B: "Microsoft", C: "Google", D: "OpenAI" }, correct: "C", rationale: "GeminiはGoogleが提供するサービスであるため、Googleアカウントが必要です。" },
        { tier: 1, q: "TikTokのアルゴリズムは何方式で評価される？", options: { A: "減点方式", B: "加算方式", C: "ランダム", D: "年功序列" }, correct: "B", rationale: "TikTokは「減点」ではなく、ユーザーの好意的なアクションを「加算」していく方式です。誰にでもチャンスがあります。" },
        { tier: 1, q: "企画リサーチをする際、TikTokアプリ内で最初に使うべき機能は？", options: { A: "設定画面", B: "探索（トレンド）タブでの検索", C: "プロフィールの編集", D: "課金アイテムの購入" }, correct: "B", rationale: "まずは「今、何が流行っているのか」を肌で感じることが重要です。探索タブでトレンドを把握しましょう。" },
        // 中級 (Tier 2)
        { tier: 2, q: "TikTokの「ユーザー名（@マーク以降）」を変更する際の制限として正しいものはどれですか？", options: { A: "何度でも自由に変更できる", B: "30日に1回のみ変更可能", C: "一度設定したら二度と変更できない", D: "有料プランでのみ変更可能" }, correct: "B", rationale: "ユーザー名はURLの一部にもなるため、頻繁な変更は制限されています（30日に1回）。" },
        { tier: 2, q: "Canvaの自動生成AI機能で、「デザイン内の不要なものをなぞるだけで消せる」機能の名前は？", options: { A: "マジック生成", B: "マジック消しゴム", C: "背景リムーバ", D: "マジック拡張" }, correct: "B", rationale: "「マジック消しゴム」を使えば、写真に写り込んだ不要な人やモノを簡単になぞって消去し、背景を自然に補完できます。" },
        { tier: 2, q: "動画の冒頭で視聴者の興味を引き、指を止めさせる要素を何と呼ぶ？", options: { A: "フック", B: "クロージング", C: "CTA", D: "ハッシュタグ" }, correct: "A", rationale: "釣り針（Hook）のように、視聴者の心を「引っかける」ための冒頭の工夫です。ここが弱いとすぐにスクロールされてしまいます。" },
        // 上級 (Tier 3)
        { tier: 3, q: "Geminiが得意とする「マルチモーダル」とはどういう意味ですか？", options: { A: "複数の言語を翻訳できること", B: "テキストだけでなく、画像や音声など複数の種類の情報を扱えること", C: "複数のユーザーで同時に作業できること", D: "複数のアプリを同時に起動できること" }, correct: "B", rationale: "テキスト、コード、画像、音声、動画など、異なる形式のデータを理解・生成できる能力を指します。" },
        { tier: 3, q: "無料で使えるAI画像編集ツール「Nano Banana」の最大の特徴は？", options: { A: "動画編集に特化している", B: "Illustratorのようなベクター描画ができる", C: "プロンプト（テキスト指示）だけで高度な画像編集が完結する", D: "音楽を自動生成できる" }, correct: "C", rationale: "Nano Bananaはテキスト指示（プロンプト）だけで、不要物の消去・背景の差し替え・画像の高画質化など、プロ級の編集が可能です。" },
        { tier: 3, q: "Canvaを使って、同じデザインの動画を大量に作る機能の名前は？", options: { A: "マジック作文", B: "一括作成 (Bulk Create)", C: "背景除去", D: "ブランドキット" }, correct: "B", rationale: "「一括作成」機能を使えば、CSVなどを取り込んでデザインを量産できます。まさに「工場」のような機能です。" }
    ]);


    // --- DAY 5 QUIZ ---
    initQuiz('quiz-vol01-5', [
        {
            q: "TikTokの動画において、最も推奨されるアスペクト比（縦横比）は？",
            options: { A: "16:9 (横長)", B: "1:1 (正方形)", C: "9:16 (縦長)", D: "4:3" },
            correct: "C",
            rationale: "TikTokはスマホ視聴がメインのため、「9:16」の縦全画面サイズが最も没入感が高く、推奨されています。"
        },
        {
            q: "CapCutで、動画の上に別の画像や動画を重ねる機能の名前は？",
            options: { A: "はめ込み合成 (Overlay)", B: "クロマキー", C: "フリーズ", D: "逆再生" },
            correct: "A",
            rationale: "「はめ込み合成（オーバーレイ）」を使うことで、メイン映像の上にリアクション動画や資料画像を重ねることができます。"
        },
        {
            q: "動画の一部だけを切り抜いたり、特定の形に表示させたりする機能は？",
            options: { A: "ブレンド", B: "マスク (Mask)", C: "調整", D: "フィルター" },
            correct: "B",
            rationale: "「マスク」機能を使うことで、映像を円形や長方形に切り抜いたり、画面を分割したりすることができます。"
        },
        {
            q: "動画のテンポを良くするために、会話の「無言の間」をカットする手法は？",
            options: { A: "ジャンプカット (ジェットカット)", B: "クロスフェード", C: "とことんカット", D: "マシンガンカット" },
            correct: "A",
            rationale: "「ジャンプカット」は、不要な間を極限まで削ることで、視聴者を飽きさせないリズムを生み出す必須テクニックです。"
        },
        {
            q: "本日の目標投稿本数は？",
            options: { A: "1本", B: "3本以上", C: "10本", D: "0本" },
            correct: "B",
            rationale: "習うより慣れろ、の精神で「3本以上」の投稿を目指しましょう。質より量のフェーズです。"
        }
    ]);

    // --- DAY 6 QUIZ (Placeholder) ---
    initQuiz('quiz-vol01-4', [
        {
            q: "視線を誘導する効果がある、画面を縦横3つに分ける基本的な構図は？",
            options: { A: "三分割法", B: "日の丸構図", C: "シンメトリー", D: "額縁構図" },
            correct: "A",
            rationale: "「三分割法」は、画面を縦横に3等分し、その交点や線上に被写体を配置することで、バランスの良い写真になります。"
        },
        {
            q: "丸い被写体を画面のど真ん中に配置する、シンプルで力強い構図は？",
            options: { A: "三分割法", B: "日の丸構図", C: "対角線構図", D: "放射線構図" },
            correct: "B",
            rationale: "「日の丸構図」は、被写体を中央に大胆に配置し、その存在感を強調するシンプルな構図です。"
        },
        {
            q: "CapCutでPCとスマホ間でデータを共有するために使う機能は？",
            options: { A: "Bluetooth", B: "AirDrop", C: "スペース / Space", D: "USBケーブル" },
            correct: "C",
            rationale: "CapCutの「スペース（クラウド）」機能を使えば、PCで編集したプロジェクトをクラウド経由でスマホと同期できます。"
        },
        {
            q: "今回の実習で、AI（Gemini等）で作るショート動画の台本の文字数は？",
            options: { A: "1000文字以上", B: "300文字程度", C: "140文字以内", D: "制限なし" },
            correct: "B",
            rationale: "ショート動画（1分未満）の場合、300文字程度が適切な情報量とテンポを生み出します。"
        },
        {
            q: "本コースの最終目標（再生数）は？",
            options: { A: "1本でも50回再生", B: "1万回再生", C: "フォロワー1000人", D: "収益化達成" },
            correct: "A",
            rationale: "まずは「50回再生」という小さな壁を超えることが、アルゴリズムに乗るための第一歩です。"
        }
    ]);


    // --- DAY 6 QUIZ ---
    initQuiz('quiz-vol01-6', [
        {
            q: "TikTok動画で「冒頭から視聴者を掴む」ために、Suno AIで使うべき重要タグは？",
            options: { A: "[Intro] (前奏)", B: "[Hook] または [Chorus] (サビ)", C: "[Outro] (後奏)", D: "[Verse] (Aメロ)" },
            correct: "B",
            rationale: "TikTokは「最初の3秒」が勝負です。ダラダラとした前奏を入れず、[Hook]や[Chorus]タグを使って、0秒地点からサビ（盛り上がり）を配置するのが鉄則です。"
        },
        {
            q: "Suno AI無料プラン（Basic）で作った曲を、YouTubeショート(収益化済み)で使うことは？",
            options: { A: "クレジット表記すればOK", B: "できない（商用利用不可）", C: "1分以内ならOK", D: "バレなければOK" },
            correct: "B",
            rationale: "無料プランの楽曲には商用利用権が付与されません。収益化する動画に使用する場合、必ず「Pro Plan（有料）」加入中に生成した楽曲を使用してください。"
        },
        {
            q: "SOUNDRAWにおいて、動画の構成に合わせて曲の「盛り上がり」を部分ごとに調整する機能は？",
            options: { A: "Length Adjustment", B: "Energy Map (ブロック編集)", C: "Tempo Slider", D: "Genre Filter" },
            correct: "B",
            rationale: "プロモード（Edit）の「Energy Map」を使えば、イントロは静かに(Low)、サビは激しく(High)といった調整がブロック単位で可能です。"
        },
        {
            q: "動画の「カット割り」や「動き」に合わせて、音楽のタイミングをシンクロさせる技法を何と呼ぶ？",
            options: { A: "音ハメ", B: "音ズレ", C: "フェードアウト", D: "リップシンク" },
            correct: "A",
            rationale: "「音ハメ」は、映像と音のキメを一致させることで、視聴者に快感（ドーパミン）を与える重要なテクニックです。"
        },
        {
            q: "Suno AIで「疾走感のある女性ボーカル曲」を作りたい場合、適切なスタイル指定は？",
            options: { A: "Slow Ballad, Male Vocals", B: "Future Bass, High Tempo, Female Vocals", C: "Jazz, Relaxing", D: "Acoustic, Guitar" },
            correct: "B",
            rationale: "「Future Bass」「High Tempo」「Female Vocals」などのキーワードを組み合わせることで、TikTokで人気のある疾走感・バズ系の楽曲が生成されやすくなります。"
        }
    ]);

    // --- DAY 7 QUIZ ---
    initQuiz('quiz-vol01-7', [
        {
            q: "ハッシュタグ選びの「黄金比」として、最も推奨される組み合わせは？",
            options: { A: "ビッグワードのみ (例: #TikTok)", B: "ビッグ・ミドル・スモールを混ぜる", C: "自分だけのオリジナルタグのみ", D: "ハッシュタグは付けない" },
            correct: "B",
            rationale: "「#TikTok」のような巨大なタグだけでは埋もれてしまいます。中規模・小規模なタグを混ぜることで、確実にターゲットに届けることができます。"
        },
        {
            q: "キャプション（説明文）の「1行目」に書くべき最も重要な要素は？",
            options: { A: "挨拶 (こんにちは)", B: "天気の話", C: "興味を引くフック / 結論", D: "日付" },
            correct: "C",
            rationale: "視聴者は最初の数行しか読みません。「まさかこうなるとは…」のようなフックや、動画の結論を最初に配置して、続きを読む動機を作りましょう。"
        },
        {
            q: "VREWが得意とする動画スタイルは？",
            options: { A: "映画のようなシネマティック動画", B: "ダンス動画", C: "テロップ解説動画 / 情報発信系", D: "3Dアニメーション" },
            correct: "C",
            rationale: "VREWは「音声認識」と「字幕生成」に特化しているため、セミナー切り抜きや解説動画などの「言葉中心の動画」で最強の力を発揮します。"
        },
        {
            q: "Webサイトにおけるハッシュタグのような役割を果たす「隠し説明文」を何という？",
            options: { A: "メタタグ (Meta Description)", B: "divタグ", C: "CSS", D: "JavaScript" },
            correct: "A",
            rationale: "メタタグ（description）は、Google検索結果やSNSシェア時に表示される「看板」です。適切に設定することでクリック率が上がります。"
        },
        {
            q: "VREWで動画を作る際、台本（テキスト）から画像や音声を自動生成する機能を使う場合の手順は？",
            options: { A: "「テキストから動画を作成」を選ぶ", B: "「新規プロジェクト」で一から作る", C: "「録音」ボタンを押す", D: "スマホを振る" },
            correct: "A",
            rationale: "「テキストから動画を作成」モードを選べば、台本をコピペするだけで、AIが画像・音声・字幕をすべて自動で組み上げてくれます。"
        }
    ]);

    // --- DAY 8 QUIZ ---
    initQuiz('quiz-vol01-8', [
        {
            q: "他の人の動画の横に、自分の動画を並べて投稿する機能は？",
            options: { A: "Stitch (リミックス)", B: "Duet (デュエット)", C: "Reply (返信)", D: "Save (保存)" },
            correct: "B",
            rationale: "「デュエット」は、画面を分割して元動画と共演する機能です。一緒に歌ったり、ダンスを真似たりするのに最適です。"
        },
        {
            q: "他の人の動画の一部（最大5秒）を切り抜いて、その続きを自分が撮影する機能は？",
            options: { A: "Duet (デュエット)", B: "Stitch (リミックス)", C: "Cut (カット)", D: "Crop (トリミング)" },
            correct: "B",
            rationale: "「Stitch（縫い合わせる）」は、相手の問いかけや驚きのシーンを引用し、それに「アンサー」を返す形で動画を作れます。"
        },
        {
            q: "コメント返信動画（動画で返信）を行う最大のメリットは？",
            options: { A: "画質が良くなる", B: "ネタ切れ防止 / ファンとの交流", C: "広告収入が倍になる", D: "TikTok社から表彰される" },
            correct: "B",
            rationale: "来たコメントをネタにできるため、「次に何を撮ろう？」と悩む時間がなくなります。さらにファンとの信頼関係（エンゲージメント）も深まります。"
        },
        {
            q: "Webサイトでユーザーの操作（クリックなど）を検知して反応する仕組みは？",
            options: { A: "イベントリスナー (Event Listener)", B: "ループ (Loop)", C: "変数 (Variable)", D: "データベース (Database)" },
            correct: "A",
            rationale: "「イベントリスナー」は、Webページがユーザーの呼びかけ（イベント）を「じっと待つ（Listen）」ための耳のような仕組みです。"
        },
        {
            q: "今日の目標投稿本数は？",
            options: { A: "1本", B: "10本", C: "3本以上", D: "0本" },
            correct: "C",
            rationale: "質より量です。「3本以上」を目指して、気楽にアウトプットしましょう。"
        }
    ]);

    // --- DAY 9 QUIZ ---
    initQuiz('quiz-vol01-9', [
        {
            q: "TikTokライブ配信を始めるために必要な最低フォロワー数は？",
            options: { A: "0人（誰でもOK）", B: "100人", C: "1,000人", D: "10,000人" },
            correct: "C",
            rationale: "TikTokライブは原則1,000フォロワー以上が必要です。まずはショート動画でフォロワーを増やすことを目指しましょう。"
        },
        {
            q: "ライブ配信で視聴者を引き留めるために最も効果的なテクニックは？",
            options: { A: "ずっと無言でいる", B: "コメントを読み上げて反応する", C: "画面を真っ暗にする", D: "BGMを最大音量にする" },
            correct: "B",
            rationale: "視聴者のコメントに反応することで「見てもらえている」という喜びが生まれ、滞在時間が伸びます。双方向性がライブの命です。"
        },
        {
            q: "ライブ配信中に視聴者から贈られるアイテムの名称は？",
            options: { A: "スタンプ", B: "ギフト", C: "チケット", D: "トークン" },
            correct: "B",
            rationale: "「ギフト」は視聴者が配信者に贈るバーチャルアイテムです。これを「ダイヤモンド」に換算して収益化できます。"
        },
        {
            q: "ライブ配信の推奨時間は？",
            options: { A: "5分以内", B: "30分〜1時間", C: "5時間以上", D: "24時間" },
            correct: "B",
            rationale: "30分〜1時間がおすすめです。短すぎると視聴者が集まる前に終わってしまい、長すぎると視聴者も配信者も疲れてしまいます。"
        },
        {
            q: "本日の目標投稿本数は？",
            options: { A: "1本", B: "3本以上", C: "10本", D: "0本" },
            correct: "B",
            rationale: "引き続き「3本以上」を目指しましょう。ライブは今日学んだことを活かして、将来チャレンジする目標にしましょう。"
        }
    ]);

    // --- DAY 10 QUIZ ---
    initQuiz('quiz-vol01-10', [
        {
            q: "TikTokアナリティクスで、アルゴリズムに最も影響する指標は？",
            options: { A: "いいね数", B: "コメント数", C: "平均視聴時間", D: "フォロワー数" },
            correct: "C",
            rationale: "「いいね」の数よりも「どれだけ長く見てもらえたか（平均視聴時間）」がアルゴリズムへの影響が最も大きいです。長く見てもらえる＝面白い、とAIが判断します。"
        },
        {
            q: "視聴維持率グラフで、最初の1〜2秒で大きく数値が落ちている場合、改善すべきポイントは？",
            options: { A: "動画の長さ", B: "冒頭のフック（ツカミ）", C: "ハッシュタグの数", D: "BGMの音量" },
            correct: "B",
            rationale: "冒頭で離脱されているのは「ツカミ」が弱い証拠です。「結論ファースト」や「え！？と思わせる一言」を最初に持ってきましょう。"
        },
        {
            q: "「保存」や「シェア」がアルゴリズムに与える影響は、「いいね」と比較してどうですか？",
            options: { A: "「いいね」の方が大きい", B: "同じくらい", C: "「保存・シェア」の方が大きい", D: "影響はない" },
            correct: "C",
            rationale: "「保存」は「あとで見返したい」、「シェア」は「誰かに教えたい」という強い行動です。押しやすい「いいね」よりも、アルゴリズムへの重みは大きいです。"
        },
        {
            q: "動画を改善するPDCAサイクルで、一度に変えるべき要素の数は？",
            options: { A: "全部一気に変える", B: "1つだけ", C: "ランダムに3つ", D: "変えない" },
            correct: "B",
            rationale: "一度に全部変えると「何が効果的だったか」分からなくなります。冒頭、BGM、テロップなど、1つずつ変えて数字を比較するのがコツです。"
        },
        {
            q: "トラフィックソースで「FYP（For You Page）」からの流入が多いのは、何を意味する？",
            options: { A: "フォロワーが多い", B: "ハッシュタグが効いている", C: "おすすめに載っている（バズの兆候）", D: "広告を出している" },
            correct: "C",
            rationale: "FYP（おすすめページ）からの流入は、TikTokのアルゴリズムがあなたの動画を「面白い」と判断して拡散してくれている証拠です🎉"
        }
    ]);

    // --- DAY 11 QUIZ ---
    initQuiz('quiz-vol01-11', [
        {
            q: "「クロスプラットフォーム戦略」の最大のメリットは？",
            options: { A: "1つの動画を作るだけで、複数のSNSから集客できること", B: "別のアプリのパスワードが分かること", C: "画質が3倍になること", D: "TikTokから表彰されること" },
            correct: "A",
            rationale: "動画を作る労力は同じでも、投稿先を増やすだけで再生されるチャンスが何倍にもなります。「一石三鳥」を狙いましょう。"
        },
        {
            q: "TikTokの動画を別のSNSに再投稿する際、絶対にやってはいけないことは？",
            options: { A: "同じ日に投稿する", B: "TikTokのロゴ（透かし）が入ったまま投稿する", C: "タイトルを変える", D: "音楽を変えない" },
            correct: "B",
            rationale: "他プラットフォーム（特にInstagramやYouTube）は、ライバルであるTikTokのロゴが入った動画のアルゴリズム評価を極端に下げます。必ずロゴなしの元動画を使いましょう。"
        },
        {
            q: "YouTube Shortsの「住民（視聴者）」の傾向に最も当てはまるのは？",
            options: { A: "最初の1秒で面白くなければ即スワイプ", B: "おしゃれで綺麗な映像を保存したい", C: "役に立つ知識やハウツーをじっくり見たい", D: "文字だけのニュース速報が知りたい" },
            correct: "C",
            rationale: "YouTubeは検索エコシステムが強いため、「〜のやり方」「〜選」といった、少し長めで役に立つ情報系コンテンツが安定して伸びやすいです。"
        },
        {
            q: "Instagram Reelsで最も評価（おすすめ表示）に直結しやすい、ユーザーのアクションは？",
            options: { A: "いいね", B: "あとで見返すための「保存」", C: "コメント", D: "プロフィールへの移動" },
            correct: "B",
            rationale: "Instagramは「カタログ」のように使われることが多く、「保存」数が多い投稿＝価値の高いコンテンツとして優遇されるアルゴリズムになっています。"
        },
        {
            q: "X (旧Twitter)で動画をバズらせるためのコツは？",
            options: { A: "綺麗な風景の動画だけを載せる", B: "何も文字を書かずに動画だけ投稿する", C: "動画に「ツッコミどころ」や「議論の余地」を持たせたテキストを添える", D: "30分以上の長編動画を載せる" },
            correct: "C",
            rationale: "Xは「言葉のプラットフォーム」であり、リポスト（拡散）が命です。動画本体の力だけでなく「みんなが言及（ツッコミ・議論）したくなる」文脈作りが必須です。"
        }
    ]);

    // --- DAY 12 QUIZ ---
    initQuiz('quiz-vol01-12', [
        {
            q: "他のクリエイターの動画の一部（最大5秒）を引用し、自分のリアクションや続きを撮影するTikTokの機能は？",
            options: { A: "デュエット", B: "Stitch (リミックス)", C: "シャウトアウト", D: "リポスト" },
            correct: "B",
            rationale: "「Stitch（縫い合わせる）」は相手の動画の一部を切り取って引用し、それに対するアンサーや追加情報を自分で撮影できる機能です。コラボの第一歩として最適です。"
        },
        {
            q: "コラボ相手を見つけた時、最初にすべき行動として最も適切なのは？",
            options: { A: "すぐにDMで「コラボしませんか？」と送る", B: "まず相手の動画にコメントやデュエットで交流する", C: "自分のフォロワー数をアピールする", D: "相手の動画をそのまま転載する" },
            correct: "B",
            rationale: "いきなりDMでコラボを持ちかけるのはマナー違反です。まずはコメントやデュエットで関係性を構築し、「この人は何者？」→「あ、あの面白いクリエイターだ！」と認知してもらうことが大切です。"
        },
        {
            q: "TikTokでコラボ相手を探す際、最も効果的な方法は？",
            options: { A: "フォロワー数が100万以上の人だけを狙う", B: "自分と同じジャンル・同程度の規模のクリエイターを探す", C: "全く関連のないジャンルの人とだけコラボする", D: "コラボはせず一人で頑張る" },
            correct: "B",
            rationale: "いきなり大物を狙うよりも、同じジャンル・同規模の「仲間」を見つける方が成功率が高いです。お互いのファン層が近いため、フォロワーが自然に流入しやすくなります。"
        },
        {
            q: "企業やブランドからのコラボ依頼（PR案件）を受けるために、最も近道となる行動は？",
            options: { A: "毎日企業にDMを送り続ける", B: "TikTok Creator Marketplaceに登録し、質の高いコンテンツを継続投稿する", C: "動画を一切投稿しない", D: "他人の動画を転載する" },
            correct: "B",
            rationale: "TikTok Creator Marketplaceに登録し、ジャンルを絞った質の高い投稿を続けることで、関連する企業から依頼が届くようになります。まずは「特定分野の専門家」として認知されることが重要です。"
        },
        {
            q: "本日の目標投稿本数は？",
            options: { A: "1本", B: "3本以上", C: "10本", D: "0本" },
            correct: "B",
            rationale: "引き続き「3本以上」を目標に！コラボやネットワーキングの意識を持ちながら、課題動画を完成させましょう。"
        }
    ]);

    updateLatestButton();



    // --- IMMERSIVE ENGINE (New Feature) ---
    const initImmersiveExperience = () => {
        // 1. Inject Global CSS for Animations
        const style = document.createElement('style');
        style.innerHTML = `
            /* --- SCROLL REVEAL --- */
            .reveal {
                opacity: 0;
                transform: translateY(30px);
                transition: all 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);
            }
            .reveal.active {
                opacity: 1;
                transform: translateY(0);
            }

            /* --- MARKER ANIMATION --- */
            strong {
                position: relative;
                z-index: 1;
                display: inline-block; /* Required for marker effect */
            }
            strong::after {
                content: "";
                position: absolute;
                left: 0;
                bottom: 0px;
                width: 0%;
                height: 30%;
                background: rgba(79, 70, 229, 0.2); /* Indigo highlight */
                z-index: -1;
                transition: width 0.6s ease-out;
            }
            strong.active::after {
                width: 100%;
            }

            /* --- PROGRESS BAR --- */
            .scroll-progress-container {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 4px;
                background: rgba(0,0,0,0.1);
                z-index: 9999;
            }
            .scroll-progress-bar {
                height: 100%;
                background: linear-gradient(90deg, #818cf8, #4f46e5);
                width: 0%;
                transition: width 0.1s;
            }
        `;
        document.head.appendChild(style);

        // 2. Add Progress Bar to Body
        if (!document.querySelector('.scroll-progress-container')) {
            const barContainer = document.createElement('div');
            barContainer.className = 'scroll-progress-container';
            barContainer.innerHTML = '<div class="scroll-progress-bar"></div>';
            document.body.prepend(barContainer);
        }

        // 3. Auto-Apply Reveal Classes & Observe
        const contentElements = document.querySelectorAll('.content h2, .content h3, .content p, .content .box, .content .video-list, .content .step-box, .content .roadmap-box');

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    // Optional: Stop observing once revealed
                    // observer.unobserve(entry.target); 
                }
            });
        }, { threshold: 0.1, rootMargin: "0px 0px -50px 0px" });

        contentElements.forEach(el => {
            el.classList.add('reveal');
            observer.observe(el);
        });

        // 4. Observe Strong Tags for Marker Effect
        const strongTags = document.querySelectorAll('.content strong');
        strongTags.forEach(el => observer.observe(el));

        // 5. Scroll Progress Logic
        window.addEventListener('scroll', () => {
            const scrollTop = window.scrollY;
            const docHeight = document.body.scrollHeight - window.innerHeight;
            const scrollPercent = (scrollTop / docHeight) * 100;
            const bar = document.querySelector('.scroll-progress-bar');
            if (bar) bar.style.width = scrollPercent + '%';
        });
    };

    // Initialize Immersive Engine only on content pages (not index.html for now, or check generic class)
    if (document.querySelector('.content')) {
        initImmersiveExperience();
    }

});
