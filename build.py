import re

with open(r'..\【202603】生成AIとプロンプト\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Colors
html = html.replace('#5c6bc0', '#00897b')
html = html.replace('#3949ab', '#00695c')
html = html.replace('#9fa8da', '#4db6ac')
html = html.replace('rgba(92, 107, 192,', 'rgba(0, 137, 123,')
html = html.replace('rgba(57, 73, 171,', 'rgba(0, 105, 92,')
html = html.replace('#f0f4ff', '#e0f2f1') # old light blue to new light teal

# 2. Text/Titles
html = html.replace('DX Training Feb 2026 | TikTok Marketing', 'DX Training Mar 2026 | Generative AI & Prompt')
html = html.replace('TIKTOK <span>MARKETING</span>', 'GENERATIVE AI <span>& PROMPT</span>')
html = html.replace('February 2026 Curriculum', 'March 2026 Curriculum')

# 3. Calendar Grid Replacement
calendar_grid = '''<div class="calendar-grid">
                <div class="day-name">Sun</div>
                <div class="day-name">Mon</div>
                <div class="day-name">Tue</div>
                <div class="day-name">Wed</div>
                <div class="day-name">Thu</div>
                <div class="day-name">Fri</div>
                <div class="day-name">Sat</div>

                <div class="cal-cell"><span class="date-num">1</span></div>
                <div class="cal-cell"><span class="date-num">2</span></div>
                <div class="cal-cell has-event" data-day="d01" onclick="window.location.href='vol01-1.html'">
                    <span class="date-num">3</span><span class="ev-pill">DAY 01</span>
                    <div class="cal-popup">Vol.1 AI基本操作<br>(Click to Open)</div>
                </div>
                <div class="cal-cell has-event" data-day="d02" onclick="window.location.href='vol01-2.html'">
                    <span class="date-num">4</span><span class="ev-pill">DAY 02</span>
                    <div class="cal-popup">Vol.2 Canva基本<br>(Click to Open)</div>
                </div>
                <div class="cal-cell has-event" data-day="d03" onclick="window.location.href='vol01-3.html'">
                    <span class="date-num">5</span><span class="ev-pill">DAY 03</span>
                    <div class="cal-popup">Vol.3 プロンプト指示<br>(Click to Open)</div>
                </div>
                <div class="cal-cell"><span class="date-num">6</span></div>
                <div class="cal-cell"><span class="date-num">7</span></div>

                <div class="cal-cell"><span class="date-num">8</span></div>
                <div class="cal-cell"><span class="date-num">9</span></div>
                <div class="cal-cell has-event" data-day="d04" onclick="window.location.href='vol01-4.html'">
                    <span class="date-num">10</span><span class="ev-pill">DAY 04</span>
                    <div class="cal-popup">Vol.4 画像生成基礎</div>
                </div>
                <div class="cal-cell has-event" data-day="d05" onclick="window.location.href='vol01-5.html'">
                    <span class="date-num">11</span><span class="ev-pill">DAY 05</span>
                    <div class="cal-popup">Vol.5 動画生成基礎</div>
                </div>
                <div class="cal-cell has-event" data-day="d06" onclick="window.location.href='vol01-6.html'">
                    <span class="date-num">12</span><span class="ev-pill">DAY 06</span>
                    <div class="cal-popup">Vol.6 音楽生成基礎</div>
                </div>
                <div class="cal-cell"><span class="date-num">13</span></div>
                <div class="cal-cell"><span class="date-num">14</span></div>

                <div class="cal-cell"><span class="date-num">15</span></div>
                <div class="cal-cell"><span class="date-num">16</span></div>
                <div class="cal-cell has-event" data-day="d07" onclick="window.location.href='vol01-7.html'">
                    <span class="date-num">17</span><span class="ev-pill">DAY 07</span>
                    <div class="cal-popup">Vol.7 高度な画像生成</div>
                </div>
                <div class="cal-cell has-event" data-day="d08" onclick="window.location.href='vol01-8.html'">
                    <span class="date-num">18</span><span class="ev-pill">DAY 08</span>
                    <div class="cal-popup">Vol.8 高度な動画生成</div>
                </div>
                <div class="cal-cell has-event" data-day="d09" onclick="window.location.href='vol01-9.html'">
                    <span class="date-num">19</span><span class="ev-pill">DAY 09</span>
                    <div class="cal-popup">Vol.9 高度な音楽生成</div>
                </div>
                <div class="cal-cell"><span class="date-num">20</span></div>
                <div class="cal-cell"><span class="date-num">21</span></div>

                <div class="cal-cell"><span class="date-num">22</span></div>
                <div class="cal-cell"><span class="date-num">23</span></div>
                <div class="cal-cell has-event" data-day="d10" onclick="window.location.href='vol01-10.html'">
                    <span class="date-num">24</span><span class="ev-pill">DAY 10</span>
                    <div class="cal-popup">Vol.10 ビジネス利用</div>
                </div>
                <div class="cal-cell has-event" data-day="d11" onclick="window.location.href='vol01-11.html'">
                    <span class="date-num">25</span><span class="ev-pill">DAY 11</span>
                    <div class="cal-popup">Vol.11 プロンプト設計</div>
                </div>
                <div class="cal-cell has-event" data-day="d12" onclick="window.location.href='vol01-12.html'">
                    <span class="date-num">26</span><span class="ev-pill">DAY 12</span>
                    <div class="cal-popup">Vol.12 最新動向</div>
                </div>
                <div class="cal-cell"><span class="date-num">27</span></div>
                <div class="cal-cell"><span class="date-num">28</span></div>

                <div class="cal-cell"><span class="date-num">29</span></div>
                <div class="cal-cell"><span class="date-num">30</span></div>
                <div class="cal-cell has-event" data-day="d13" onclick="window.location.href='vol01-13.html'">
                    <span class="date-num">31</span><span class="ev-pill">DAY 13</span>
                    <div class="cal-popup">Vol.13 作品発表</div>
                </div>
                <div class="cal-cell other-month">1</div>
                <div class="cal-cell other-month">2</div>
                <div class="cal-cell other-month">3</div>
                <div class="cal-cell other-month">4</div>
            </div>'''
html = re.sub(r'<div class="calendar-grid">.*?</div>\s*</div>\s*<div class="list-area">', calendar_grid + r'\n        </div>\n\n        <div class="list-area">', html, flags=re.DOTALL)

list_items = '''<div class="curriculum-list">
                <a href="vol01-1.html" class="c-item" id="d01">
                    <div class="date-box"><span class="db-month">Tue</span><span class="db-day">03</span></div>
                    <div class="c-content"><span class="day-tag">DAY 01</span>
                        <h4>AI基本操作と画像生成</h4><p>検索方AIの基本操作と画像生成機能の紹介</p>
                    </div>
                </a>
                <a href="vol01-2.html" class="c-item" id="d02">
                    <div class="date-box"><span class="db-month">Wed</span><span class="db-day">04</span></div>
                    <div class="c-content"><span class="day-tag">DAY 02</span>
                        <h4>Canva基本と動画編集</h4><p>Canvaの基本操作、AI機能の活用法、および動画編集技術</p>
                    </div>
                </a>
                <a href="vol01-3.html" class="c-item" id="d03">
                    <div class="date-box"><span class="db-month">Thu</span><span class="db-day">05</span></div>
                    <div class="c-content"><span class="day-tag">DAY 03</span>
                        <h4>プロンプト指示方法</h4><p>生成AIのプロンプト指示方法とその応用</p>
                    </div>
                </a>
                <a href="vol01-4.html" class="c-item" id="d04">
                    <div class="date-box"><span class="db-month">Tue</span><span class="db-day">10</span></div>
                    <div class="c-content"><span class="day-tag">DAY 04</span>
                        <h4>画像生成の基礎</h4><p>テキストから画像への変換技術の基礎</p>
                    </div>
                </a>
                <a href="vol01-5.html" class="c-item" id="d05">
                    <div class="date-box"><span class="db-month">Wed</span><span class="db-day">11</span></div>
                    <div class="c-content"><span class="day-tag">DAY 05</span>
                        <h4>動画生成の基礎</h4><p>テキストから動画への変換技術の基礎</p>
                    </div>
                </a>
                <a href="vol01-6.html" class="c-item" id="d06">
                    <div class="date-box"><span class="db-month">Thu</span><span class="db-day">12</span></div>
                    <div class="c-content"><span class="day-tag">DAY 06</span>
                        <h4>音楽生成の基礎</h4><p>テキストから音楽への変換技術の基礎</p>
                    </div>
                </a>
                <a href="vol01-7.html" class="c-item" id="d07">
                    <div class="date-box"><span class="db-month">Tue</span><span class="db-day">17</span></div>
                    <div class="c-content"><span class="day-tag">DAY 07</span>
                        <h4>高度な画像生成</h4><p>応用的なテクニックによる高度な画像生成</p>
                    </div>
                </a>
                <a href="vol01-8.html" class="c-item" id="d08">
                    <div class="date-box" style="background:#e0f2f1; color:#333;"><span class="db-month">Wed</span><span class="db-day">18</span></div>
                    <div class="c-content"><span class="day-tag">DAY 08</span>
                        <h4>高度な動画生成</h4><p>応用的なテクニックによる高度な動画生成</p>
                    </div>
                </a>
                <a href="vol01-9.html" class="c-item" id="d09">
                    <div class="date-box" style="background:#e0f2f1; color:#333;"><span class="db-month">Thu</span><span class="db-day">19</span></div>
                    <div class="c-content"><span class="day-tag">DAY 09</span>
                        <h4>高度な音楽生成</h4><p>応用的なテクニックによる高度な音楽生成</p>
                    </div>
                </a>
                <a href="vol01-10.html" class="c-item" id="d10">
                    <div class="date-box" style="background:#e0f2f1; color:#333;"><span class="db-month">Tue</span><span class="db-day">24</span></div>
                    <div class="c-content"><span class="day-tag">DAY 10</span>
                        <h4>ビジネス応用事例</h4><p>共同作業AIのビジネスへの応用方法と活用事例</p>
                    </div>
                </a>
                <a href="vol01-11.html" class="c-item" id="d11">
                    <div class="date-box" style="background:#e0f2f1; color:#333;"><span class="db-month">Wed</span><span class="db-day">25</span></div>
                    <div class="c-content"><span class="day-tag">DAY 11</span>
                        <h4>プロンプト設計</h4><p>プロンプト設計と最適化技術</p>
                    </div>
                </a>
                <a href="vol01-12.html" class="c-item" id="d12">
                    <div class="date-box" style="background:#e0f2f1; color:#333;"><span class="db-month">Thu</span><span class="db-day">26</span></div>
                    <div class="c-content"><span class="day-tag">DAY 12</span>
                        <h4>最新動向と未来予測</h4><p>生成AI分野の最新動向と未来予測</p>
                    </div>
                </a>
                <a href="vol01-13.html" class="c-item" id="d13">
                    <div class="date-box" style="background:#e0f2f1; color:#333;"><span class="db-month">Tue</span><span class="db-day">31</span></div>
                    <div class="c-content"><span class="day-tag">DAY 13</span>
                        <h4>作品発表とFB</h4><p>作品の発表とフィードバックセッション</p>
                    </div>
                </a>
            </div>'''
html = re.sub(r'<div class="curriculum-list">.*?</div>\s*<a href="index_dev_notes.html" class="dev-link">', list_items + r'\n            <a href="index_dev_notes.html" class="dev-link">', html, flags=re.DOTALL)

with open(r'..\【202603】生成AIとプロンプト\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
