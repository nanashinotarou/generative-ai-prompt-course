#!/usr/bin/env python3
import re

path = r'g:\マイドライブ\研修\【202603】生成AIとプロンプト\vol02-1_canva_basics.html'

with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. タブの追加
old_tabs = '''        <div class="tab-container">
            <button class="tab-btn active" onclick="switchTab('half1')">前半：Canvaの使い方を覚えよう</button>
        </div>'''
new_tabs = '''        <div class="tab-container">
            <button class="tab-btn active" onclick="switchTab('half1')">前半：Canvaの使い方を覚えよう</button>
            <button class="tab-btn" onclick="switchTab('half2')">後半：プロンプト学習用ノートを作ろう</button>
        </div>'''
html = html.replace(old_tabs, new_tabs)

# 2. totalTasks の更新 (4 -> 7)
html = html.replace('const totalTasks = 4;', 'const totalTasks = 7;')

# 3. 後半コンテンツの挿入
old_quiz_area = '                <!-- Quiz Area -->'
new_half_2 = '''        <!-- =================== 後半 =================== -->
        <div id="half2" class="tab-content">
            
            <!-- 目的 -->
            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-solid fa-bullseye"></i>
                    <h2>🎯 実習の目的</h2>
                </div>
                <p>画像生成プロンプトのコツを覚え、後からすぐに使えるように「自分だけのプロンプトノート」を作成します。</p>
            </div>

            <!-- 動画③: Affinity by Canva -->
            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-brands fa-youtube" style="color:#ef4444; background:#fef2f2;"></i>
                    <h2>📺 動画③ Canva最強アプデ「Affinity by Canva」爆誕！</h2>
                </div>
                <a href="https://youtu.be/ThbMYDqI0VY" target="_blank" class="video-thumb" style="max-width:400px;">
                    <img src="https://img.youtube.com/vi/ThbMYDqI0VY/mqdefault.jpg" alt="Affinity by Canva">
                    <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                </a>
                <div class="box canva" style="margin-top:2rem;">
                    <h4>この動画で学ぶこと</h4>
                    <ul style="padding-left:20px; line-height:2;">
                        <li><strong>Affinityとは：</strong>Canvaが買収したプロ向けのクリエイティブスイート（AI機能以外は完全無料化）</li>
                        <li><strong>Affinity Designer：</strong>Illustratorのようなベクター描画ツール</li>
                        <li><strong>Affinity Photo：</strong>Photoshopのような高度な写真編集・合成ツール</li>
                        <li><strong>Affinity Publisher：</strong>InDesignのようなページレイアウトツール</li>
                    </ul>
                </div>
            </div>

            <!-- 動画④: Nano Banana -->
            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-brands fa-youtube" style="color:#ef4444; background:#fef2f2;"></i>
                    <h2>📺 動画④ 無料AI「Nano Banana」画像編集テク15選</h2>
                </div>
                <a href="https://youtu.be/JiUFPy97nEU" target="_blank" class="video-thumb" style="max-width:400px;">
                    <img src="https://img.youtube.com/vi/JiUFPy97nEU/mqdefault.jpg" alt="Nano Bananaテクニック">
                    <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                </a>
                <div class="box canva" style="margin-top:2rem;">
                    <h4>この動画で学ぶこと</h4>
                    <ul style="padding-left:20px; line-height:2;">
                        <li><strong>高精度な画像編集：</strong>プロンプトだけで不要な人やモノを完璧に消去</li>
                        <li><strong>背景の変更：</strong>写真の「背景だけ」を自由自在に変更する技術</li>
                        <li><strong>画質向上：</strong>古い写真やぼやけた画像をAIで鮮明に高画質化（アップスケール）</li>
                        <li>無料AIツールを組み合わせてプロ級の仕上がりにする方法</li>
                    </ul>
                </div>
            </div>

            <!-- 実習ミッション -->
            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-solid fa-person-digging"></i>
                    <h2>🧰 実習：プロンプト学習用のノートを作ろう</h2>
                </div>
                <p style="margin-bottom:1.5rem; color:var(--text-sub);">
                    以下のミッションを順番にクリアして、画像生成のコツを自分のものにしましょう！
                </p>

                <ul class="task-list">
                    <!-- タスク1 -->
                    <li class="task-item" onclick="toggleTask('t2_1', this)">
                        <div class="custom-checkbox" id="check_t2_1"><i class="fa-solid fa-check"></i></div>
                        <div class="task-content">
                            <h3>プロンプトのまとめノートを作成</h3>
                            <p>Nano Bananaで使える画像生成プロンプトをノートにまとめよう。以下のリストから気に入ったプロンプトをピックアップし、Canvaやドキュメントに保存します。</p>
                            <div style="margin-top:10px;">
                                <button class="btn btn-copy" onclick="copyText('https://docs.google.com/spreadsheets/d/1bRG2ciyDl2DHQLjIY4k8bJrUzuvD0orX1UFA0yqY1xU/edit?usp=sharing', event)">
                                    <i class="fa-regular fa-copy"></i> URLコピー
                                </button>
                                <a href="https://docs.google.com/spreadsheets/d/1bRG2ciyDl2DHQLjIY4k8bJrUzuvD0orX1UFA0yqY1xU/edit?usp=sharing" target="_blank" class="btn" style="background:#10b981; border-color:#10b981;" onclick="event.stopPropagation();">
                                    <i class="fa-solid fa-table"></i> プロンプト一覧表を開く
                                </a>
                            </div>
                        </div>
                    </li>

                    <!-- タスク2 -->
                    <li class="task-item" onclick="toggleTask('t2_2', this)">
                        <div class="custom-checkbox" id="check_t2_2"><i class="fa-solid fa-check"></i></div>
                        <div class="task-content">
                            <h3>画像素材をダウンロードして加工</h3>
                            <p>加工用の画像素材をドライブからダウンロードし、Nano Bananaなどで実際に背景変更や不要物消去などのプロンプト編集を試してみましょう。</p>
                            <div style="margin-top:10px;">
                                <a href="https://drive.google.com/drive/folders/1lcq-8fEZLzjv0fs9EdYg3AuKvm_aGQF3?usp=sharing" target="_blank" class="btn" onclick="event.stopPropagation();">
                                    <i class="fa-brands fa-google-drive"></i> 加工用画像素材を開く
                                </a>
                            </div>
                        </div>
                    </li>

                    <!-- タスク3 -->
                    <li class="task-item" onclick="toggleTask('t2_3', this)">
                        <div class="custom-checkbox" id="check_t2_3"><i class="fa-solid fa-check"></i></div>
                        <div class="task-content">
                            <h3>【発展】追加ツールを触ってみよう</h3>
                            <p>時間が余った人は、以下のツールにも触れてみましょう。</p>
                            <div class="info-box" style="margin-top:10px;">
                                <strong>Affinity by Canva</strong>（ダウンロード版 Mac/Winのみ）<br>
                                AI機能以外全部無料<br>
                                <a href="https://www.affinity.studio/ja_jp" target="_blank" style="color:#2563eb;" onclick="event.stopPropagation();">→ 公式サイトへ</a><br><br>
                                
                                <strong>AIEASE</strong>（毎日無料クレジット +5）<br>
                                <a href="https://www.aiease.ai/" target="_blank" style="color:#2563eb;" onclick="event.stopPropagation();">→ 公式サイトへ</a>
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
        </div>

                <!-- Quiz Area -->'''

html = html.replace(old_quiz_area, new_half_2)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Day2 後半コンテンツの追加が完了しました")
