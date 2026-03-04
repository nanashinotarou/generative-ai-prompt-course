#!/usr/bin/env python3
"""Day2コンテンツ充実化: Canva動画内容に基づいて教材を全面的に書き換え"""

path = r'g:\マイドライブ\研修\【202603】生成AIとプロンプト\vol02-1_canva_basics.html'

with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# ========= 前半コンテンツを差し替え =========
old_content_start = '        <div id="half1" class="tab-content active">'
old_content_end = '        <!-- Quiz Area -->'

idx_start = html.index(old_content_start)
idx_end = html.index(old_content_end)

new_content = '''        <div id="half1" class="tab-content active">

            <!-- 実習の目的 -->
            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-solid fa-bullseye"></i>
                    <h2>🎯 実習の目的</h2>
                </div>
                <p>デザインツール「Canva」の基本操作をマスターし、AI搭載の最新機能を活用できるようになります。</p>
                <div class="info-box">
                    <h4><i class="fa-solid fa-lightbulb"></i> 今日のゴール</h4>
                    <p>① Canvaの画面構成と基本操作を理解する<br>
                    ② テンプレートを活用してデザインを作成できるようになる<br>
                    ③ CanvaのAI機能を使ったコンテンツ制作を体験する</p>
                </div>
                <div class="info-box" style="margin-top:1rem;">
                    <h4><i class="fa-solid fa-right-to-bracket"></i> Canvaログイン方法</h4>
                    <p>Googleアカウントでログインするのが最も簡単です。Day1で使ったGeminiと同じGoogleアカウントを使いましょう。<br>
                    <a href="https://www.canva.com/" target="_blank" style="color:#4f46e5; font-weight:700;">→ canva.com にアクセス</a></p>
                </div>
            </div>

            <!-- 動画①: Canva使い方入門 -->
            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-brands fa-youtube" style="color:#ef4444; background:#fef2f2;"></i>
                    <h2>📺 動画① Canva使い方入門・基礎講座</h2>
                </div>
                <a href="https://youtu.be/nRds9qeaLiM" target="_blank" class="video-thumb" style="max-width:400px;">
                    <img src="https://img.youtube.com/vi/nRds9qeaLiM/mqdefault.jpg" alt="Canva基礎">
                    <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                </a>
                <div class="box canva" style="margin-top:2rem;">
                    <h4>Canvaの基本操作</h4>
                    <ul style="padding-left:20px; line-height:2;">
                        <li><strong>ホーム画面：</strong>テンプレート検索、最近のデザイン、おすすめが表示される</li>
                        <li><strong>デザイン作成：</strong>「デザインを作成」→ サイズ選択（SNS投稿, プレゼン, 動画など）</li>
                        <li><strong>テンプレート：</strong>プロ品質のテンプレートを検索して、テキストや色を変えるだけでOK</li>
                        <li><strong>要素の編集：</strong>テキスト・画像・図形をクリックして位置・大きさ・色を自由に変更</li>
                        <li><strong>レイヤー操作：</strong>要素の重なり順を「前面へ移動」「背面へ移動」で調整</li>
                        <li><strong>ページ追加：</strong>スライドや動画の場合、ページを追加して連続するコンテンツを作成</li>
                        <li><strong>ダウンロード：</strong>PNG、JPG、PDF、MP4など様々な形式で書き出し可能</li>
                    </ul>
                </div>
                <div class="box canva" style="margin-top:1.5rem;">
                    <h4>よく使うショートカット</h4>
                    <ul style="padding-left:20px; line-height:2;">
                        <li><strong>Ctrl + C / V：</strong>コピー＆ペースト</li>
                        <li><strong>Ctrl + Z：</strong>元に戻す（やり直し）</li>
                        <li><strong>Ctrl + G：</strong>グループ化（複数要素をまとめる）</li>
                        <li><strong>Ctrl + D：</strong>複製（素早くコピー）</li>
                        <li><strong>/（スラッシュ）：</strong>マジックショートカット（要素の素早い追加）</li>
                    </ul>
                </div>
            </div>

            <!-- 動画②: CanvaのAI機能 -->
            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-brands fa-youtube" style="color:#ef4444; background:#fef2f2;"></i>
                    <h2>📺 動画② CanvaのAI機能ランキング9選</h2>
                </div>
                <a href="https://youtu.be/nstHWt2_4LE" target="_blank" class="video-thumb" style="max-width:400px;">
                    <img src="https://img.youtube.com/vi/nstHWt2_4LE/mqdefault.jpg" alt="AI機能ランキング">
                    <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                </a>
                <div class="box canva" style="margin-top:2rem;">
                    <h4>CanvaのチートAI機能（2025最新アップデート含む）</h4>
                    <ul style="padding-left:20px; line-height:2;">
                        <li><strong>① マジック生成（テキスト→画像）：</strong>テキストを入力するだけでAIが画像を生成。「猫が宇宙を歩く」など</li>
                        <li><strong>② マジック消しゴム：</strong>不要なオブジェクトをワンクリックで削除。背景も自動補完</li>
                        <li><strong>③ 背景リムーバ：</strong>写真の背景を一瞬で除去。人物だけを切り抜きたい時に最強</li>
                        <li><strong>④ マジック拡張：</strong>画像の足りない部分をAIが自然に拡張。構図の変更に便利</li>
                        <li><strong>⑤ マジックリサイズ：</strong>一つのデザインを複数サイズに一括リサイズ（Instagram→YouTube→X）</li>
                        <li><strong>⑥ マジック作文（テキスト生成）：</strong>テーマを入力するとAIが文章を自動作成。キャプションやブログに</li>
                        <li><strong>⑦ テキスト→動画：</strong>テキスト入力だけでスライドショー動画を自動生成</li>
                        <li><strong>⑧ 翻訳機能：</strong>デザイン内のテキストを他言語に自動翻訳</li>
                        <li><strong>⑨ Dream Lab：</strong>高品質なAI画像生成スタジオ。スタイル指定で多彩な表現</li>
                    </ul>
                </div>
                <div class="info-box">
                    <h4><i class="fa-solid fa-star"></i> おすすめの使い方</h4>
                    <p>まずは<strong>テンプレートを選ぶ</strong> → <strong>テキストを変える</strong> → <strong>AI機能で画像を追加</strong>の3ステップが最速です。<br>
                    慣れてきたら「マジック消しゴム」「背景リムーバ」で写真編集も挑戦してみましょう！</p>
                </div>
            </div>

            <!-- 実践ステップ -->
            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-solid fa-shoe-prints"></i>
                    <h2>👣 実践ステップ</h2>
                </div>
                <div class="box canva">
                    <h4>Step 1: テンプレートでSNS投稿を作ろう</h4>
                    <ul style="padding-left:20px; line-height:2;">
                        <li>Canvaホーム → 「Instagramの投稿」をクリック</li>
                        <li>好きなテンプレートを選択</li>
                        <li>テキストを自分の内容に変更</li>
                        <li>色やフォントを変更してオリジナルにアレンジ</li>
                        <li>ダウンロード → PNG形式で保存</li>
                    </ul>
                </div>
                <div class="box canva" style="margin-top:1.5rem;">
                    <h4>Step 2: AI画像生成を試そう</h4>
                    <ul style="padding-left:20px; line-height:2;">
                        <li>左サイドバーの「アプリ」→「マジック生成」を開く</li>
                        <li>プロンプトを入力（例：「桜の下でピクニックする猫」）</li>
                        <li>スタイルを選択（写真風、水彩画風、アニメ風など）</li>
                        <li>生成された画像をデザインに配置</li>
                    </ul>
                </div>
                <div class="box canva" style="margin-top:1.5rem;">
                    <h4>Step 3: 動画を作ってみよう</h4>
                    <ul style="padding-left:20px; line-height:2;">
                        <li>「デザインを作成」→「動画」→「TikTok動画(9:16)」を選択</li>
                        <li>テンプレートを選んでテキストや画像を入れ替え</li>
                        <li>各ページにアニメーションを追加（ワイプ、フェード等）</li>
                        <li>BGM追加 → 左サイドバー「オーディオ」からフリー音源を選択</li>
                        <li>ダウンロード → MP4形式で保存</li>
                    </ul>
                </div>
            </div>

            <!-- ミッション -->
            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-solid fa-list-check"></i>
                    <h2>🧰 前半のミッション</h2>
                </div>
                <p style="margin-bottom:1.5rem; color:var(--text-sub);">
                    以下のミッションをすべてクリアしてチェックを入れましょう！進行度がアップします。
                </p>

                <ul class="task-list">
                    <li class="task-item" onclick="toggleTask('t1_1', this)">
                        <div class="custom-checkbox" id="check_t1_1"><i class="fa-solid fa-check"></i></div>
                        <div class="task-content">
                            <h3>参考動画の視聴と実習</h3>
                            <p>参考動画2本を見ながら、Canvaの基本操作とAI機能を実際に手を動かして使ってみましょう。</p>
                        </div>
                    </li>

                    <li class="task-item" onclick="toggleTask('t1_2', this)">
                        <div class="custom-checkbox" id="check_t1_2"><i class="fa-solid fa-check"></i></div>
                        <div class="task-content">
                            <h3>テンプレートでSNS投稿画像を1枚作成</h3>
                            <p>Step 1の手順に沿って、テンプレートを使ったSNS投稿画像を1枚作成しましょう。</p>
                        </div>
                    </li>

                    <li class="task-item" onclick="toggleTask('t1_3', this)">
                        <div class="custom-checkbox" id="check_t1_3"><i class="fa-solid fa-check"></i></div>
                        <div class="task-content">
                            <h3>AI画像生成を1回以上試す</h3>
                            <p>Canvaの「マジック生成」で好きなプロンプトを入力し、AI画像を生成してみましょう。</p>
                        </div>
                    </li>

                    <li class="task-item" onclick="toggleTask('t1_4', this)">
                        <div class="custom-checkbox" id="check_t1_4"><i class="fa-solid fa-check"></i></div>
                        <div class="task-content">
                            <h3>デザインの保存と提出</h3>
                            <p>作ったデザインは、必ずファイル名に自分の名前をつけてから、自分のフォルダの中に格納しましょう。</p>
                        </div>
                    </li>
                </ul>
            </div>
        </div>

        '''

html = html[:idx_start] + new_content + html[idx_end:]

# タスク数を更新（4タスクに増加）
html = html.replace("const totalTasks = 2;", "const totalTasks = 4;")

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Day 2 content enriched successfully!")
