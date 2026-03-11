# -*- coding: utf-8 -*-
import re

with open("vol04-1_nano_banana.html", "r", encoding="utf-8") as f:
    content = f.read()

# CSS for highlight-box and bento-grid (if not already present)
css_block = """
        /* Highlight box */
        .highlight-box { background: linear-gradient(135deg, #fef3c7, #fde68a); border-radius: 16px; padding: 2rem; margin: 2rem 0; color: #92400e; box-shadow: 0 4px 15px rgba(245, 158, 11, 0.15); border: 1px solid #fcd34d; }
        .highlight-box h3 { font-size: 1.4rem; font-weight: 900; margin-top: 0; border-bottom: 2px dashed #f59e0b; padding-bottom: 10px; margin-bottom: 15px; display:flex; align-items:center; gap:8px;}
"""

if ".highlight-box" not in content:
    content = content.replace("/* Video Grid */", css_block + "\n        /* Video Grid */")

# Digest for the first half (after first video-grid)
day4_p1 = """
                <div class="highlight-box" style="margin-top:2.5rem;">
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

# Find the closing of the first video-grid (in TAB 2 section)
tab2_marker = "TAB 2: FIRST HALF"
tab3_marker = "TAB 3: SECOND HALF"

tab2_idx = content.find(tab2_marker)
tab3_idx = content.find(tab3_marker)

if tab2_idx != -1 and tab3_idx != -1:
    section = content[tab2_idx:tab3_idx]
    if "完全解説ダイジェスト" not in section:
        # Find the end of the first video-grid div
        vg_end = section.find("</div>", section.find("video-grid"))
        # Find the closing </a> before it
        last_a = section.rfind("</a>", 0, vg_end)
        insert_point = section.find("</div>", last_a)
        insert_point = section.find("\n", insert_point) + 1
        section = section[:insert_point] + day4_p1 + section[insert_point:]
        content = content[:tab2_idx] + section + content[tab3_idx:]

# Digest for the second half (after second video-grid)
day4_p2 = """
                <div class="highlight-box" style="background: linear-gradient(135deg, #e0f2fe, #bae6fd); border-color: #7dd3fc; color: #0369a1; margin-top:2.5rem;">
                    <h3 style="color:#0284c7; border-bottom-color:#38bdf8;"><i class="fa-solid fa-bolt"></i> 読むだけでわかる！完全解説ダイジェスト</h3>
                    <p style="margin-bottom:0; line-height:1.7;">Nano Banana Pro & Imagen 3(Google) の実践活用術と裏技です。</p>
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

tab3_idx = content.find(tab3_marker)
tab4_marker = "TAB 4: SUMMARY"
tab4_idx = content.find(tab4_marker)

if tab3_idx != -1 and tab4_idx != -1:
    section2 = content[tab3_idx:tab4_idx]
    if "完全解説ダイジェスト" not in section2:
        vg_end = section2.find("</div>", section2.find("video-grid"))
        last_a = section2.rfind("</a>", 0, vg_end)
        insert_point = section2.find("</div>", last_a)
        insert_point = section2.find("\n", insert_point) + 1
        section2 = section2[:insert_point] + day4_p2 + section2[insert_point:]
        content = content[:tab3_idx] + section2 + content[tab4_idx:]

with open("vol04-1_nano_banana.html", "w", encoding="utf-8") as f:
    f.write(content)

# Verify
count = content.count("完全解説ダイジェスト")
print(f"Done! Found {count} occurrences of digest marker in Day 4 HTML.")
