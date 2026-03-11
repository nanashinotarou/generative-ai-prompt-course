import re

with open('build_day4.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the intermediate write code
content = re.sub(r'with open\(.*?["\']\)(?:\s*f\.write\(html_content\))?\s*print\(.*?["\']\)\s*import os\s*html_content = """', '', content, flags=re.DOTALL)

with open('build_day4_clean.py', 'w', encoding='utf-8') as f:
    f.write(content)
