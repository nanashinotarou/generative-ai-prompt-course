import os

directory = r'g:\マイドライブ\研修\【202603】生成AIとプロンプト'
files_to_check = [
    'build_day1.py',
    'build_day2.py',
    'build_day3.py',
    'build_day4.py', 'build_day4_part2.py',
    'build_day5.py', 'build_day5_part2.py',
    'index_dev_notes.html'
]

replacements = [
    ('**「AIに的確な指示を出し、意図した結果を引き出す力」**', '<strong>「AIに的確な指示を出し、意図した結果を引き出す力」</strong>'),
    ('**「テキスト生成AI（Gemini）」**', '<strong>「テキスト生成AI（Gemini）」</strong>'),
    ('**「画像生成AI 4天王」**', '<strong>「画像生成AI 4天王」</strong>'),
    ('**「呪文」**', '<strong>「呪文」</strong>'),
    ('**「Canva」と「AIの連携」**', '<strong>「Canva」と「AIの連携」</strong>'),
    ('- **初心者にもわかりやすい**ですます調<br>', '- <strong>初心者にもわかりやすい</strong>ですます調<br>'),
    ('**「プロンプトエンジニアリング」**', '<strong>「プロンプトエンジニアリング」</strong>'),
    ('**「画像生成と高度加工」**', '<strong>「画像生成と高度加工」</strong>'),
    ('**「テキストから動画への変換技術の基礎とカメラワーク」**', '<strong>「テキストから動画への変換技術の基礎とカメラワーク」</strong>'),
    (' **Bento Grid** ', ' <strong>Bento Grid</strong> '),
    (' **AudioContext** ', ' <strong>AudioContext</strong> '),
    (' **GitHub** と **Cloudflare Pages** ', ' <strong>GitHub</strong> と <strong>Cloudflare Pages</strong> '),
    (' **Persistent Progress** ', ' <strong>Persistent Progress</strong> ')
]

for filename in files_to_check:
    filepath = os.path.join(directory, filename)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    for old_str, new_str in replacements:
        content = content.replace(old_str, new_str)
        
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {filename}')
