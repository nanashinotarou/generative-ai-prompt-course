#!/usr/bin/env python3
"""Day1コンテンツ充実化: 動画内容に基づいて教材を全面的に書き換え"""

import re

path = r'g:\マイドライブ\研修\【202603】生成AIとプロンプト\vol01-1_ai_start.html'

with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# ========= 前半コンテンツを差し替え =========
old_half1_content = '''        <div id="half1" class="tab-content active">

            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-solid fa-bullseye"></i>
                    <h2>🎯 実習の目的</h2>
                </div>
                <p>Geminiの色々な使い方を体験し、AIによる画像生成の基礎知識を習得します。</p>

                <div class="box gemini">
                    <h4>Geminiにできること（基本編）</h4>
                    <ul style="padding-left:20px; line-height:2;">
                        <li><strong>アイデア出し：</strong>「〇〇についての斬新なアイデアを10個出して」</li>
                        <li><strong>文章作成・要約：</strong>「この長文を重要なポイント3つに絞って箇条書きにして」</li>
                        <li><strong>画像生成：</strong>「未来都市を飛ぶ車の画像を生成して（※具体的な指示がカギ）」</li>
                    </ul>
                </div>

                <div class="code-box">
                    <span class="code-label">プロンプト例（コピペ用）</span>
                    <span style="color:#7dd3fc;"># 役割</span><br>
                    あなたはプロのAIアシスタントです。<br><br>
                    <span style="color:#7dd3fc;"># 命令</span><br>
                    「生成AIがもたらす未来」について、<br>
                    小学生でもわかる言葉で300文字程度で説明してください。
                </div>
            </div>

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
                            <h3>Googleアカウントの準備</h3>
                            <p>ブラウザでGeminiを開き、Googleアカウントでサインインする。アカウントがない場合は新規作成してください。</p>
                            <a href="https://gemini.google.com" target="_blank" class="btn" onclick="event.stopPropagation();">
                                <i class="fa-solid fa-arrow-up-right-from-square"></i> Geminiを開く
                            </a>
                        </div>
                    </li>

                    <li class="task-item" onclick="toggleTask('t1_2', this)">
                        <div class="custom-checkbox" id="check_t1_2"><i class="fa-solid fa-check"></i></div>
                        <div class="task-content">
                            <h3>NotebookLMへのアクセス</h3>
                            <p>GoogleのAIノートブック機能「NotebookLM」を開いて確認する。</p>
                            <a href="https://notebooklm.google.com/" target="_blank" class="btn" onclick="event.stopPropagation();">
                                <i class="fa-solid fa-book-open"></i> NotebookLMを開く
                            </a>
                        </div>
                    </li>

                    <li class="task-item" onclick="toggleTask('t1_3', this)">
                        <div class="custom-checkbox" id="check_t1_3"><i class="fa-solid fa-check"></i></div>
                        <div class="task-content">
                            <h3>資料の確認</h3>
                            <p>共有されたドキュメントやプロンプトテキストを開いて確認する。</p>
                            <button class="btn btn-copy" onclick="copyText('https://docs.google.com/document/d/16k1obzkjpxKIn6bo5fPYVEEQeJXJvUDkBnPTEJMbnC8/edit?usp=sharing', event)">
                                <i class="fa-regular fa-copy"></i> URLをコピー
                            </button>
                            <a href="https://docs.google.com/document/d/16k1obzkjpxKIn6bo5fPYVEEQeJXJvUDkBnPTEJMbnC8/edit?usp=sharing" target="_blank" class="btn" onclick="event.stopPropagation();">
                                <i class="fa-solid fa-file-lines"></i> Docsを開く
                            </a>
                        </div>
                    </li>
                </ul>
            </div>

            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-brands fa-youtube" style="color:#ef4444; background:#fef2f2;"></i>
                    <h2>🎥 参考・再生動画</h2>
                </div>
                <div class="video-grid">
                    <a href="https://youtu.be/WJ1R3D0ntf8" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/WJ1R3D0ntf8/mqdefault.jpg" alt="Video 1">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                    <a href="https://youtu.be/KUNBWh9rprI" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/KUNBWh9rprI/mqdefault.jpg" alt="Video 2">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                    <a href="https://youtu.be/NBWGnzpeEHk" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/NBWGnzpeEHk/mqdefault.jpg" alt="Video 3">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                    <a href="https://youtu.be/o5kXK5JvIt8" target="_blank" class="video-thumb">
                        <img src="https://img.youtube.com/vi/o5kXK5JvIt8/mqdefault.jpg" alt="Video 4">
                        <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                    </a>
                </div>
            </div>
        </div>'''

new_half1_content = '''        <div id="half1" class="tab-content active">

            <!-- 実習の目的 -->
            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-solid fa-bullseye"></i>
                    <h2>🎯 実習の目的</h2>
                </div>
                <p>AI・人工知能の基礎を理解し、Google Geminiを実際に操作して「AIでできること」を体験します。</p>
                <div class="info-box">
                    <h4><i class="fa-solid fa-lightbulb"></i> 今日のゴール</h4>
                    <p>① AI・生成AIとは何かを説明できるようになる<br>
                    ② Geminiを使って文章生成・画像生成ができるようになる<br>
                    ③ AIに仕事を奪われないための考え方を身につける</p>
                </div>
            </div>

            <!-- 動画①: AI・人工知能とは -->
            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-brands fa-youtube" style="color:#ef4444; background:#fef2f2;"></i>
                    <h2>📺 動画① AI・人工知能とは？</h2>
                </div>
                <a href="https://youtu.be/WJ1R3D0ntf8" target="_blank" class="video-thumb" style="max-width:400px;">
                    <img src="https://img.youtube.com/vi/WJ1R3D0ntf8/mqdefault.jpg" alt="AI・人工知能とは">
                    <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                </a>
                <div class="box gemini" style="margin-top:2rem;">
                    <h4>この動画で学ぶこと</h4>
                    <ul style="padding-left:20px; line-height:2;">
                        <li><strong>AIの定義：</strong>人工知能 = 人間の知能をコンピュータで再現する技術</li>
                        <li><strong>AIの歴史：</strong>第1次〜第3次AIブーム。現在は「ディープラーニング」による第3次ブーム</li>
                        <li><strong>AIの種類：</strong>特化型AI（1つの作業に特化）と 汎用AI（人間のように何でもできる）</li>
                        <li><strong>AIの仕組み：</strong>大量のデータから「パターン」を見つけて学習する（機械学習）</li>
                        <li><strong>活用事例：</strong>画像認識、音声認識、自動翻訳、チャットボット、自動運転など</li>
                    </ul>
                </div>
            </div>

            <!-- 動画②: 生成AIとは -->
            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-brands fa-youtube" style="color:#ef4444; background:#fef2f2;"></i>
                    <h2>📺 動画② 生成AI（ジェネレーティブAI）とは？</h2>
                </div>
                <a href="https://youtu.be/KUNBWh9rprI" target="_blank" class="video-thumb" style="max-width:400px;">
                    <img src="https://img.youtube.com/vi/KUNBWh9rprI/mqdefault.jpg" alt="生成AIとは">
                    <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                </a>
                <div class="box gemini" style="margin-top:2rem;">
                    <h4>この動画で学ぶこと</h4>
                    <ul style="padding-left:20px; line-height:2;">
                        <li><strong>生成AIとは：</strong>テキスト・画像・音声・動画など「新しいコンテンツを作る」AI</li>
                        <li><strong>従来のAIとの違い：</strong>従来 = 分析・判定 → 生成AI = 創造・生成</li>
                        <li><strong>主要な種類：</strong>テキスト生成（ChatGPT, Gemini）、画像生成（Midjourney, DALL-E）、音声生成、動画生成</li>
                        <li><strong>仕組み：</strong>大規模言語モデル（LLM）が「次に来る確率の高い言葉」を予測して文章を生成</li>
                        <li><strong>活用事例：</strong>文章要約、企画書作成、プレゼン資料、SNS投稿文生成、コーディング補助</li>
                    </ul>
                </div>
                <div class="info-box">
                    <h4><i class="fa-solid fa-triangle-exclamation"></i> 注意点（ハルシネーション）</h4>
                    <p>生成AIは「もっともらしい嘘」をつくことがあります（＝ハルシネーション）。<br>
                    AIの回答は<strong>必ずファクトチェック</strong>（事実確認）してから使いましょう！</p>
                </div>
            </div>

            <!-- 動画③: AIで無くならない仕事 -->
            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-brands fa-youtube" style="color:#ef4444; background:#fef2f2;"></i>
                    <h2>📺 動画③ AIで将来なくならない仕事4選</h2>
                </div>
                <a href="https://youtu.be/NBWGnzpeEHk" target="_blank" class="video-thumb" style="max-width:400px;">
                    <img src="https://img.youtube.com/vi/NBWGnzpeEHk/mqdefault.jpg" alt="AIで無くならない仕事">
                    <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                </a>
                <div class="box gemini" style="margin-top:2rem;">
                    <h4>この動画で学ぶこと</h4>
                    <ul style="padding-left:20px; line-height:2;">
                        <li><strong>AIに代替されやすい仕事：</strong>定型的・ルーティン的な作業（データ入力、簡単な翻訳、定型メール作成）</li>
                        <li><strong>AIに代替されにくい仕事①：</strong>高度なコミュニケーション力（カウンセラー、営業、コンサルタント）</li>
                        <li><strong>AIに代替されにくい仕事②：</strong>創造性・芸術性（アーティスト、デザイナー、企画立案）</li>
                        <li><strong>AIに代替されにくい仕事③：</strong>身体を使う仕事（介護、建設、スポーツ）</li>
                        <li><strong>AIに代替されにくい仕事④：</strong>AIを管理・活用する仕事（AI活用エンジニア、プロンプトエンジニア）</li>
                    </ul>
                </div>
                <div class="info-box">
                    <h4><i class="fa-solid fa-lightbulb"></i> 重要なポイント</h4>
                    <p>AIは「敵」ではなく「道具」。<strong>AIを使いこなせる人材</strong>になることが最大の武器です。<br>
                    この研修で学ぶ「プロンプトスキル」は、まさにその第一歩です！</p>
                </div>
            </div>

            <!-- 動画④: Gemini使い方基礎 -->
            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-brands fa-youtube" style="color:#ef4444; background:#fef2f2;"></i>
                    <h2>📺 動画④ Google Gemini 使い方基礎講座</h2>
                </div>
                <a href="https://youtu.be/o5kXK5JvIt8" target="_blank" class="video-thumb" style="max-width:400px;">
                    <img src="https://img.youtube.com/vi/o5kXK5JvIt8/mqdefault.jpg" alt="Gemini使い方基礎">
                    <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                </a>
                <div class="box gemini" style="margin-top:2rem;">
                    <h4>Geminiの基本操作</h4>
                    <ul style="padding-left:20px; line-height:2;">
                        <li><strong>アクセス方法：</strong><a href="https://gemini.google.com" target="_blank" style="color:#2563eb;">gemini.google.com</a> → Googleアカウントでログイン</li>
                        <li><strong>テキスト生成：</strong>質問・指示を入力するだけで文章を生成</li>
                        <li><strong>画像生成：</strong>「〇〇の画像を作って」と入力すると画像を生成（Imagen搭載）</li>
                        <li><strong>ファイル読み取り：</strong>PDF、画像、ドキュメントをアップロードして内容を要約</li>
                        <li><strong>Google連携：</strong>Gmail、Googleドキュメント、スプレッドシートとの連携が可能</li>
                        <li><strong>拡張機能：</strong>YouTubeの動画内容要約、Google Mapsとの連携なども可能</li>
                    </ul>
                </div>

                <div class="code-box">
                    <span class="code-label">プロンプト例① テキスト生成</span>
                    <span style="color:#7dd3fc;"># 役割</span><br>
                    あなたはプロのAIアシスタントです。<br><br>
                    <span style="color:#7dd3fc;"># 命令</span><br>
                    「生成AIがもたらす未来」について、<br>
                    小学生でもわかる言葉で300文字程度で説明してください。
                </div>

                <div class="code-box">
                    <span class="code-label">プロンプト例② 画像生成</span>
                    <span style="color:#7dd3fc;"># 画像生成プロンプト</span><br>
                    未来の東京の街並みを描いてください。<br>
                    空飛ぶ車、ホログラム広告、緑あふれるビル群、<br>
                    夕焼けの空、高解像度でリアルなイラスト風
                </div>

                <div class="code-box">
                    <span class="code-label">プロンプト例③ 要約</span>
                    <span style="color:#7dd3fc;"># ファイル要約</span><br>
                    添付したPDFの内容を以下の形式で要約してください：<br>
                    ・概要（3行）<br>
                    ・重要ポイント（箇条書き5つ）<br>
                    ・次のアクション（やるべきこと3つ）
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
                            <h3>Geminiにアクセスしてログイン</h3>
                            <p>ブラウザでGeminiを開き、Googleアカウントでサインインする。アカウントがない場合は新規作成してください。</p>
                            <a href="https://gemini.google.com" target="_blank" class="btn" onclick="event.stopPropagation();">
                                <i class="fa-solid fa-arrow-up-right-from-square"></i> Geminiを開く
                            </a>
                        </div>
                    </li>

                    <li class="task-item" onclick="toggleTask('t1_2', this)">
                        <div class="custom-checkbox" id="check_t1_2"><i class="fa-solid fa-check"></i></div>
                        <div class="task-content">
                            <h3>Geminiでテキスト生成を体験</h3>
                            <p>上のプロンプト例をコピーしてGeminiに貼り付け、回答を確認する。自分なりにアレンジしてみよう！</p>
                        </div>
                    </li>

                    <li class="task-item" onclick="toggleTask('t1_3', this)">
                        <div class="custom-checkbox" id="check_t1_3"><i class="fa-solid fa-check"></i></div>
                        <div class="task-content">
                            <h3>Geminiで画像生成を体験</h3>
                            <p>「猫が宇宙を歩いている画像」など、好きなプロンプトで画像生成してみましょう。具体的な指示ほど良い結果が出ます！</p>
                        </div>
                    </li>

                    <li class="task-item" onclick="toggleTask('t1_4', this)">
                        <div class="custom-checkbox" id="check_t1_4"><i class="fa-solid fa-check"></i></div>
                        <div class="task-content">
                            <h3>NotebookLMを開く</h3>
                            <p>GoogleのAIノートブック機能「NotebookLM」を開いて確認する。PDFや記事をアップロードして要約してもらおう。</p>
                            <a href="https://notebooklm.google.com/" target="_blank" class="btn" onclick="event.stopPropagation();">
                                <i class="fa-solid fa-book-open"></i> NotebookLMを開く
                            </a>
                        </div>
                    </li>

                    <li class="task-item" onclick="toggleTask('t1_5', this)">
                        <div class="custom-checkbox" id="check_t1_5"><i class="fa-solid fa-check"></i></div>
                        <div class="task-content">
                            <h3>共有資料を確認</h3>
                            <p>共有されたドキュメントやプロンプトテキストを開いて確認する。</p>
                            <button class="btn btn-copy" onclick="copyText('https://docs.google.com/document/d/16k1obzkjpxKIn6bo5fPYVEEQeJXJvUDkBnPTEJMbnC8/edit?usp=sharing', event)">
                                <i class="fa-regular fa-copy"></i> URLをコピー
                            </button>
                            <a href="https://docs.google.com/document/d/16k1obzkjpxKIn6bo5fPYVEEQeJXJvUDkBnPTEJMbnC8/edit?usp=sharing" target="_blank" class="btn" onclick="event.stopPropagation();">
                                <i class="fa-solid fa-file-lines"></i> Docsを開く
                            </a>
                        </div>
                    </li>
                </ul>
            </div>
        </div>'''

html = html.replace(old_half1_content, new_half1_content)

# ========= 後半コンテンツを差し替え =========
old_half2_start = '        <!-- =================== 後半 =================== -->'
old_half2_end = '        <!-- Dev Notes Link -->'

# Find the positions
idx_start = html.index(old_half2_start)
idx_end = html.index(old_half2_end)

new_half2 = '''        <!-- =================== 後半 =================== -->
        <div id="half2" class="tab-content">

            <!-- 目的 -->
            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-solid fa-pen-nib"></i>
                    <h2>🎯 実習の目的</h2>
                </div>
                <p>生成AIの信頼性（ファクトチェック）と、AI画像生成ツール4種類の特徴を比較・理解します。</p>
            </div>

            <!-- 動画⑤: ファクトチェック（文科省教材） -->
            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-brands fa-youtube" style="color:#ef4444; background:#fef2f2;"></i>
                    <h2>📺 動画⑤ 生成AIの情報は全部正しい？</h2>
                </div>
                <a href="https://youtu.be/j9XJJkh2OYM" target="_blank" class="video-thumb" style="max-width:400px;">
                    <img src="https://img.youtube.com/vi/j9XJJkh2OYM/mqdefault.jpg" alt="ファクトチェック">
                    <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                </a>
                <div class="box gemini" style="margin-top:2rem;">
                    <h4>この動画で学ぶこと（文部科学省教材）</h4>
                    <ul style="padding-left:20px; line-height:2;">
                        <li><strong>生成AIの仕組み：</strong>確率的に「次に来そうな言葉」を並べているだけで、事実を理解しているわけではない</li>
                        <li><strong>ハルシネーション：</strong>「もっともらしい嘘」が混ざることがある。特に数字・日付・人名は要注意</li>
                        <li><strong>ファクトチェックの方法：</strong>複数の信頼できるソース（公式サイト、論文、ニュース）で裏付けを取る</li>
                        <li><strong>正しい使い方：</strong>AIの回答は「下書き・たたき台」として使い、最終判断は自分でする</li>
                    </ul>
                </div>
            </div>

            <!-- 動画⑥: 生成AI基本概念（Google認定資格） -->
            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-brands fa-youtube" style="color:#ef4444; background:#fef2f2;"></i>
                    <h2>📺 動画⑥ 生成AIの基本概念の概要</h2>
                </div>
                <a href="https://youtu.be/xUXyDaMqL60" target="_blank" class="video-thumb" style="max-width:400px;">
                    <img src="https://img.youtube.com/vi/xUXyDaMqL60/mqdefault.jpg" alt="生成AI基本概念">
                    <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                </a>
                <div class="box gemini" style="margin-top:2rem;">
                    <h4>この動画で学ぶこと（Google認定資格より）</h4>
                    <ul style="padding-left:20px; line-height:2;">
                        <li><strong>AI・ML・DL・生成AIの関係：</strong>AI ⊃ 機械学習(ML) ⊃ 深層学習(DL) ⊃ 生成AI</li>
                        <li><strong>大規模言語モデル（LLM）：</strong>大量のテキストデータで事前学習されたモデル。Geminiの心臓部</li>
                        <li><strong>プロンプトの重要性：</strong>入力（プロンプト）の質が、出力の質を決める</li>
                        <li><strong>モデルの種類：</strong>テキスト→テキスト、テキスト→画像、マルチモーダル（複数入出力）</li>
                        <li><strong>責任あるAI：</strong>AIは偏見（バイアス）を持つ可能性がある。公平性・透明性が大切</li>
                    </ul>
                </div>
            </div>

            <!-- 動画⑦: 画像生成AI比較 -->
            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-brands fa-youtube" style="color:#ef4444; background:#fef2f2;"></i>
                    <h2>📺 動画⑦ 2026年おすすめ画像生成AI徹底比較</h2>
                </div>
                <a href="https://youtu.be/vJLDbXaSKW4" target="_blank" class="video-thumb" style="max-width:400px;">
                    <img src="https://img.youtube.com/vi/vJLDbXaSKW4/mqdefault.jpg" alt="画像生成AI比較">
                    <div class="play-overlay"><i class="fa-solid fa-play"></i></div>
                </a>
                <div class="info-box">
                    <h4><i class="fa-solid fa-lightbulb"></i> 比較する4つのAI画像生成ツール</h4>
                    <p>① NanoBanana Pro &nbsp; ② Seedream 4.0 &nbsp; ③ Midjourney &nbsp; ④ Adobe Firefly</p>
                </div>
                <div class="box canva" style="margin-top:1.5rem;">
                    <h4>① NanoBanana Pro</h4>
                    <ul style="padding-left:20px; line-height:2;">
                        <li>日本語プロンプトに対応、日本人の顔や日本的なシーンが得意</li>
                        <li>リアル系の画像生成に強い</li>
                        <li>商用利用可能（有料プラン）</li>
                    </ul>
                </div>
                <div class="box canva" style="margin-top:1.5rem;">
                    <h4>② Seedream 4.0</h4>
                    <ul style="padding-left:20px; line-height:2;">
                        <li>Googleが開発した高品質画像生成モデル</li>
                        <li>テキストの正確な埋め込みが得意（看板、ロゴ等）</li>
                        <li>Geminiの画像生成エンジンとして採用</li>
                    </ul>
                </div>
                <div class="box canva" style="margin-top:1.5rem;">
                    <h4>③ Midjourney</h4>
                    <ul style="padding-left:20px; line-height:2;">
                        <li>アート性・美しさはトップクラス</li>
                        <li>幻想的・映画的な表現が得意</li>
                        <li>Discord/Webから利用。有料のみ（月額約1,600円〜）</li>
                    </ul>
                </div>
                <div class="box canva" style="margin-top:1.5rem;">
                    <h4>④ Adobe Firefly</h4>
                    <ul style="padding-left:20px; line-height:2;">
                        <li>商用利用に最も安全（著作権クリアな学習データ）</li>
                        <li>Photoshopとの連携で写真編集に強い</li>
                        <li>合成・摘出（背景除去、部分編集）が最も得意</li>
                    </ul>
                </div>
            </div>

            <!-- ミッション -->
            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-solid fa-tasks"></i>
                    <h2>🧰 後半のミッション</h2>
                </div>
                <ul class="task-list">
                    <li class="task-item" onclick="toggleTask('t2_1', this)">
                        <div class="custom-checkbox" id="check_t2_1"><i class="fa-solid fa-check"></i></div>
                        <div class="task-content">
                            <h3>参考動画の視聴</h3>
                            <p>後半の参考動画3本を視聴し、ファクトチェックの重要性と4つのAI画像生成ツールの特徴をつかむ。</p>
                        </div>
                    </li>

                    <li class="task-item" onclick="toggleTask('t2_2', this)">
                        <div class="custom-checkbox" id="check_t2_2"><i class="fa-solid fa-check"></i></div>
                        <div class="task-content">
                            <h3>6つのプロンプトノートの作成</h3>
                            <p>指定のドキュメントからテキストをコピーし、1つのプロンプトごとに4つのAIの特徴をまとめる（Canva, スライド等を使用）。</p>
                            <button class="btn btn-copy" onclick="copyText('https://docs.google.com/document/d/16k1obzkjpxKIn6bo5fPYVEEQeJXJvUDkBnPTEJMbnC8/edit?usp=sharing', event)">
                                <i class="fa-regular fa-copy"></i> テキストURLコピー
                            </button>
                        </div>
                    </li>

                    <li class="task-item" onclick="toggleTask('t2_3', this)">
                        <div class="custom-checkbox" id="check_t2_3"><i class="fa-solid fa-check"></i></div>
                        <div class="task-content">
                            <h3>得意分野の評価まとめ</h3>
                            <p>以下の7項目について、どのAIがオススメか特徴とともに1ページにまとめる。</p>
                            <div class="code-box" style="margin-top:0.8rem; padding:1.2rem 1.5rem;">
                                <span class="code-label">評価項目</span>
                                ①商品紹介 ②資料作成 ③実写の広告<br>
                                ④煽り画角 ⑤MVの原型 ⑥画像の大量生成<br>
                                ⑦合成や摘出
                            </div>
                        </div>
                    </li>
                </ul>
            </div>

            <!-- Quiz Area -->
            <div class="quiz-area glass-card" style="margin-top:3rem; text-align:center;">
                <h2 style="font-size:1.6rem; margin:0 0 0.5rem; color:var(--accent);">📝 理解度チェック</h2>
                <p style="color:var(--text-sub); margin-bottom:1.5rem;">Day 1 で学んだことを確認しましょう</p>
                <div id="quiz-vol01-1" style="text-align:left;">
                    <div style="text-align:center; color:var(--text-sub);">クイズを読み込み中...</div>
                </div>
            </div>
        </div>

        '''

html = html[:idx_start] + new_half2 + html[idx_end:]

# タスク数を更新（前半5 + 後半3 = 8）
html = html.replace("const totalTasks = 6;", "const totalTasks = 8;")

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Day 1 content enriched successfully!")
