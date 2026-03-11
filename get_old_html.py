import subprocess

files = ['vol01-1_ai_start.html', 'vol02-1_canva_basics.html', 'vol01-3_prompt.html', 'vol04-1_nano_banana.html', 'vol05-1_text_to_video.html']
for p in files:
    res = subprocess.run(["git", "show", f"65ae8d4:{p}"], capture_output=True, text=True, encoding='utf-8')
    with open(f"old_{p}", "w", encoding='utf-8') as f:
        f.write(res.stdout)
