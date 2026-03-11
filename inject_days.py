import sys
import re

css = """
        /* Highlight box */
        .highlight-box { background: linear-gradient(135deg, #fef3c7, #fde68a); border-radius: 16px; padding: 2rem; margin: 2rem 0; color: #92400e; box-shadow: 0 4px 15px rgba(245, 158, 11, 0.15); border: 1px solid #fcd34d; }
        .highlight-box h3 { font-size: 1.4rem; font-weight: 900; margin-top: 0; border-bottom: 2px dashed #f59e0b; padding-bottom: 10px; margin-bottom: 15px; display:flex; align-items:center; gap:8px;}

        /* Content List Grid */
        .bento-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin: 2.5rem 0;}
        .bento-item { background: #fff; border-radius: 16px; padding: 2rem; position: relative; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.03); border: 1px solid #f1f5f9; transition: transform 0.3s, box-shadow 0.3s;}
        .bento-item:hover { transform: translateY(-5px); box-shadow: 0 12px 25px rgba(0,0,0,0.06); border-color: var(--accent-light);}
        .bento-item h4 { margin: 0 0 1rem; font-size: 1.2rem; color: var(--text-main); display: flex; align-items: center; gap: 0.5rem; font-weight:800;}
        .bento-item p { font-size: 1.05rem; color: #64748b; line-height: 1.6; margin: 0 0 1rem 0; }
"""

day1_p1 = """
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
"""

day1_p2 = """
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
"""

day2_p1 = """
                <div class="highlight-box">
                    <h3><i class="fa-solid fa-book-open"></i> 読むだけでわかる！完全解説ダイジェスト</h3>
                    <p style="margin-bottom:0; line-height:1.7;">デザインツール「Canva」の基本とAI機能をマスターし、誰でもプロ級のデザインを作れるようになるためのエッセンスです。</p>
                </div>
                <div class="bento-grid">
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-wand-magic-sparkles" style="color:#a855f7;"></i> 1. CanvaのAI活用</h4>
                        <p>Magic Studio機能を活用すれば、テキストから画像生成、デザインの自動リサイズ、被写体の切り抜きなどがワンクリックで行えます。</p>
                    </div>
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-layer-group" style="color:#0ea5e9;"></i> 2. テンプレートの効率的利用</h4>
                        <p>ゼロから作るのではなく、数百万点のテンプレートから目的に合ったものを検索しカスタマイズすることで、制作時間を大幅に短縮できます。</p>
                    </div>
                </div>
"""

day2_p2 = """
                <div class="highlight-box" style="background: linear-gradient(135deg, #e0f2fe, #bae6fd); border-color: #7dd3fc; color: #0369a1; margin-top:3rem;">
                    <h3 style="color:#0284c7; border-bottom-color:#38bdf8;"><i class="fa-solid fa-bolt"></i> 読むだけでわかる！完全解説ダイジェスト</h3>
                    <p style="margin-bottom:0; line-height:1.7;">Affinity by CanvaやNano Banana等のツールの実践的な画像生成・編集プロンプトのテクニックをまとめました。</p>
                </div>
                <div class="bento-grid">
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-palette" style="color:#f59e0b;"></i> 1. プロンプト生成術</h4>
                        <p>被写体、背景、照明、カメラアングルの4要素を具体的に言語化することで、生成される画像の精度が圧倒的に上がります。</p>
                    </div>
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-crop-simple" style="color:#10b981;"></i> 2. AIツール間の連携</h4>
                        <p>Nano Bananaでリアルな人物画像を生成し、Canvaで文字入れとレイアウトを行うなど、複数ツールの組み合わせで高クオリティな制作が可能です。</p>
                    </div>
                </div>
"""

day3_p1 = """
                <div class="highlight-box">
                    <h3><i class="fa-solid fa-book-open"></i> 読むだけでわかる！完全解説ダイジェスト</h3>
                    <p style="margin-bottom:0; line-height:1.7;">構造的なプロンプト指示（Markdown記法）など、生成AIを意のままに操るための基本テクニック5選です。</p>
                </div>
                <div class="bento-grid">
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-code" style="color:#f59e0b;"></i> 1. Markdown記法</h4>
                        <p>見出し印（#）やリスト（-）を使ってプロンプトを構造化することで、AIが指示書として読み込みやすくなり、意図のズレを防ぎます。</p>
                    </div>
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-pen-nib" style="color:#3b82f6;"></i> 2. 役割と条件の指定</h4>
                        <p>「あなたはプロのWebライターです」のようにAIに明確なペルソナを与え、出力文字数やトーン等の条件を明記することが精度向上の大原則です。</p>
                    </div>
                </div>
"""

day3_p2 = """
                <div class="highlight-box" style="background: linear-gradient(135deg, #e0f2fe, #bae6fd); border-color: #7dd3fc; color: #0369a1; margin-top:3rem;">
                    <h3 style="color:#0284c7; border-bottom-color:#38bdf8;"><i class="fa-solid fa-bolt"></i> 読むだけでわかる！完全解説ダイジェスト</h3>
                    <p style="margin-bottom:0; line-height:1.7;">長文処理や複雑なタスクを失敗させないための、AIの精度爆上げテクニックです。</p>
                </div>
                <div class="bento-grid">
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-sitemap" style="color:#10b981;"></i> 1. ステップ・バイ・ステップ</h4>
                        <p>複雑な要求は一度にさせず、「まず現状分析、次に課題抽出、最後に解決策」のように段階的に思考させることで、論理的な回答を引き出せます。</p>
                    </div>
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-reply-all" style="color:#8b5cf6;"></i> 2. Few-Shot Prompting</h4>
                        <p>求める出力の「具体例（入力→出力のセット）」をいくつかプロンプト内に含めることで、望むフォーマットでの確実な出力を担保します。</p>
                    </div>
                </div>
"""

day4_p1 = """
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
"""

day4_p2 = """
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
"""

def inject_html(filepath, css_injection, part1_injection, part2_injection):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # CSS injection
    if ".bento-grid" not in content:
        content = content.replace("/* Video Grid */", css_injection + "\n        /* Video Grid */")
    
    # Inject part 1 (after first video grid, inside TAB 2)
    tab2_start = content.find("TAB 2: FIRST HALF")
    tab3_start = content.find("TAB 3: SECOND HALF")
    
    if part1_injection and "読むだけでわかる！完全解説ダイジェスト" not in content[tab2_start:tab3_start]:
        section = content[tab2_start:tab3_start]
        section = re.sub(r'(<div class="video-grid">[\s\S]*?</div>\s*</div>)', r'\1\n' + part1_injection, section, count=1)
        content = content[:tab2_start] + section + content[tab3_start:]
    
    # Inject part 2 (after second video grid, inside TAB 3)
    if part2_injection:
        tab4_start = content.find("TAB 4: SUMMARY")
        section2 = content[tab3_start:tab4_start]
        if "読むだけでわかる！完全解説ダイジェスト" not in section2:
            # Need to match video grid correctly. Look for <div class="video-grid"> then the closing </div> structure.
            # Some grids have 3 videos, some 2, some 4.
            section2 = re.sub(r'(<div class="video-grid">[\s\S]*?</div>\s*</div>)', r'\1\n' + part2_injection, section2, count=1)
            # If the above fails (e.g. no nested wrapper depending on exactly how it is), let's fallback to just replace <div class="video-grid">...</div>
            # Wait, in build_day1.py, the video grid is like:
            # <div class="video-grid">
            #    <a...</a>
            # </div>
            section2 = re.sub(r'(<div class="video-grid">[\s\S]*?</a>\s*</div>)', r'\1\n' + part2_injection, section2, count=1)
            content = content[:tab3_start] + section2 + content[tab4_start:]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

inject_html("build_day1.py", css, day1_p1, day1_p2)
inject_html("build_day2.py", css, day2_p1, day2_p2)
inject_html("build_day3.py", css, day3_p1, day3_p2)

# For day 4, they are split into build_day4.py and build_day4_part2.py
def inject_split_html(file1, file2, css_injection, part1_injection, part2_injection):
    with open(file1, "r", encoding="utf-8") as f:
        content = f.read()
    if ".bento-grid" not in content:
        content = content.replace("/* Video Grid */", css_injection + "\n        /* Video Grid */")
    
    tab2_start = content.find("TAB 2: FIRST HALF")
    if part1_injection and "読むだけでわかる！完全解説ダイジェスト" not in content:
        content = re.sub(r'(<div class="video-grid">[\s\S]*?</a>\s*</div>)', r'\1\n' + part1_injection, content, count=1)
    
    with open(file1, "w", encoding="utf-8") as f:
        f.write(content)
        
    with open(file2, "r", encoding="utf-8") as f:
        content2 = f.read()
    if part2_injection and "読むだけでわかる！完全解説ダイジェスト" not in content2:
        content2 = re.sub(r'(<div class="video-grid">[\s\S]*?</a>\s*</div>)', r'\1\n' + part2_injection, content2, count=1)
    with open(file2, "w", encoding="utf-8") as f:
        f.write(content2)

inject_split_html("build_day4.py", "build_day4_part2.py", css, day4_p1, day4_p2)
print("Injection complete")
