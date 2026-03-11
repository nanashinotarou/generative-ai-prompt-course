import os

with open('build_day5_part1.py', 'r', encoding='utf-8') as f:
    p1 = f.read()

with open('build_day5_part2.py', 'r', encoding='utf-8') as f:
    p2 = f.read()

# Clean p1
import re
p1_clean = re.sub(r'with open\(.*?Generated build_day5_part1\.py["\']\)', '', p1, flags=re.DOTALL)
p1_clean = p1_clean.rstrip()
if p1_clean.endswith('"""'):
    p1_clean = p1_clean[:-3]

# Clean p2
p2_clean = re.sub(r'import os.*?html_content = """', '', p2, flags=re.DOTALL)

final_code = p1_clean + p2_clean
final_code = final_code.replace('build_day5_part2.py', 'vol05-1_text_to_video.html')

with open('build_day5.py', 'w', encoding='utf-8') as f:
    f.write(final_code)

print("Fixed build_day5.py")
