# -*- coding: utf-8 -*-
"""
Day 4 ビルドスクリプト統合版
build_day4.py (Part 1) と build_day4_part2.py (Part 2) から
html_content 文字列だけを抽出して結合し、1つのHTMLとして書き出す。
"""
import re

# Part 1 を読む
with open("build_day4.py", "r", encoding="utf-8") as f:
    src1 = f.read()

# Part 1 の html_content を抽出 (最初の """ ... """ ブロック)
m1 = re.search(r'html_content\s*=\s*"""(.*?)"""', src1, re.DOTALL)
if not m1:
    raise RuntimeError("Part 1 の html_content が見つかりません")
part1_html = m1.group(1)

# Part 2 を読む（build_day4.py の後半部分、import os 以降）
# build_day4.py に2つ目の html_content がある
parts = list(re.finditer(r'html_content\s*=\s*"""(.*?)"""', src1, re.DOTALL))
if len(parts) >= 2:
    part2_html = parts[1].group(1)
else:
    raise RuntimeError("Part 2 の html_content が見つかりません")

# 結合
full_html = part1_html + part2_html

# 書き出し
with open("vol04-1_nano_banana.html", "w", encoding="utf-8") as f:
    f.write(full_html)

# 検証
print(f"Generated vol04-1_nano_banana.html ({len(full_html)} chars)")
print(f"Has DOCTYPE: {'<!DOCTYPE' in full_html}")
print(f"Has </html>: {'</html>' in full_html}")
print(f"Has tab-goal: {'tab-goal' in full_html}")
print(f"Has tab-first: {'tab-first' in full_html}")
print(f"Has tab-second: {'tab-second' in full_html}")
print(f"Has tab-summary: {'tab-summary' in full_html}")
print(f"Digest count: {full_html.count('完全解説ダイジェスト')}")
