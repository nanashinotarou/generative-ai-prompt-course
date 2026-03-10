import os

def build_part1():
    return """
        <!-- ================= HALF 1 (BASics) ================= -->
        <div id="half1" class="tab-content active">
            <div class="glass-card">
                <div class="card-header">
                    <i class="fa-solid fa-graduation-cap"></i>
                    <h2>画像生成のキホンとプロンプトの構造</h2>
                </div>
                <p>動画で解説されているテキストから画像への変換技術の基礎です。AIが画像を生成する際、「プロンプト」という命令文を与えます。プロンプトは明確で構造的であるほど、AIが意図通りに解釈しやすくなります。</p>
                
                <div class="bento-grid">
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-image"></i> 被写体 (Subject)</h4>
                        <p>誰が・何が主役かを明確にします。（例：ゴールデンレトリバー、一人の女性など）</p>
                    </div>
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-camera"></i> 構図・光・スタイル</h4>
                        <p>どんな雰囲気で撮られた写真（または絵）かを追加します。（例：シネマティック、ネオンライト、フラットデザイン）</p>
                    </div>
                    <div class="bento-item">
                        <h4><i class="fa-solid fa-sliders"></i> パラメーター</h4>
                        <p>アスペクト比などのシステム上の設定です。（例：--ar 16:9, --no blur）</p>
                    </div>
                </div>

                <div class="box gemini">
                    <h4><i class="fa-solid fa-diagram-project"></i> 構造的なプロンプトの書き方 (Markdown)</h4>
                    <p>箇条書きや `#, ##` を使って情報を整理すると、AIに伝わりやすくなります。</p>
                    <div class="code-box">
                        <span class="code-label">Template</span>
                        # 被写体<br>
                        - 年齢・性別: 20代の女性<br>
                        - 服装: モダンなスーツ<br><br>
                        # 環境・光<br>
                        - 場所: オフィスのカフェスペース<br>
                        - 光源: 大きな窓からの自然光<br><br>
                        # スタイル<br>
                        - 写真調, 高画質, 8k
                    </div>
                </div>
            </div>

            <!-- Drag & Drop Simulator -->
            <div class="glass-card" id="simulator-section">
                <div class="card-header">
                    <i class="fa-solid fa-flask-vial"></i>
                    <h2>体験：プロンプト調合釜（Cauldron Simulator）</h2>
                </div>
                <p>要素（チップ）を下の「魔法の釜（ドロップゾーン）」にドラッグ＆ドロップして、どんなプロンプトが完成するか試してみましょう！</p>
                
                <div class="draggable-container">
                    <div class="drag-chip subject" draggable="true" data-text="サイバーパンクな街並み,">🏙️ サイバーパンクな街並み (Subject)</div>
                    <div class="drag-chip subject" draggable="true" data-text="一匹の可愛い猫,">🐱 一匹の可愛い猫 (Subject)</div>
                    <div class="drag-chip style" draggable="true" data-text="水彩画タッチ, 淡い色合い,">🎨 水彩画タッチ (Style)</div>
                    <div class="drag-chip style" draggable="true" data-text="シネマティックライティング, 8k resolution,">🎥 シネマティック (Lighting)</div>
                    <div class="drag-chip param" draggable="true" data-text="--ar 16:9">📐 横長 (--ar)</div>
                    <div class="drag-chip param" draggable="true" data-text="--no humans">🚫 人物なし (--no)</div>
                </div>

                <div class="cauldron-container">
                    <div class="cauldron-dropzone" id="cauldron">
                        <i class="fa-solid fa-fire fa-2x"></i>
                        <span>ここにプロンプト要素をドロップ！</span>
                    </div>
                    <div class="cauldron-result">
                        <h4>完成したプロンプト:</h4>
                        <div id="cauldron-output" class="code-box" style="margin:0; min-height:80px; display:flex; align-items:center;">[ ここに生成されます ]</div>
                        <button class="btn" onclick="simulateCauldron()"><i class="fa-solid fa-wand-magic-sparkles"></i> 画像を生成する(Simulation)</button>
                    </div>
                </div>
                
                <div id="simulation-preview" style="display:none; margin-top:1.5rem; text-align:center;">
                    <div class="video-thumb" style="max-width:500px; margin:0 auto; padding:2rem; background:#1e293b; color:#10b981; border:2px dashed #34d399;">
                        <i class="fa-solid fa-image fa-3x" style="margin-bottom:1rem;"></i>
                        <h3 id="simulation-mock-text">AI Image Generated!</h3>
                    </div>
                </div>
            </div>

            <div class="mission-ticket" onclick="completeMission(this, 'm0')">
                <div class="wax-seal" style="background: radial-gradient(circle at 30% 30%, #a78bfa, #8b5cf6, #5b21b6); border-color:#4c1d95;"><i class="fa-solid fa-flask"></i></div>
                <div class="ticket-stub"><i class="fa-solid fa-ticket-simple" style="color:#8b5cf6;"></i></div>
                <div class="mission-content">
                    <h3>Mission 1: 調合完了</h3>
                    <p>プロンプト調合釜に3つ以上の要素を入れて、画像をシミュレーション生成してみましょう。</p>
                </div>
                <div class="mission-checkbox"><i class="fa-solid fa-check"></i></div>
            </div>

            <button class="next-tab-btn" onclick="switchTab('half2')">活用事例20選 へ進む <i class="fa-solid fa-arrow-right"></i></button>
        </div>
    """
