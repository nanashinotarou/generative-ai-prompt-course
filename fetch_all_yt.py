import urllib.request
import re

urls = [
    # Day 1
    'WJ1R3D0ntf8', 'KUNBWh9rprI', 'NBWGnzpeEHk', 'o5kXK5JvIt8',
    'j9XJJkh2OYM', 'xUXyDaMqL60', 'vJLDbXaSKW4',
    # Day 2
    'nRds9qeaLiM', 'nstHWt2_4LE', 'ThbMYDqI0VY', 'JiUFPy97nEU',
    # Day 3
    'yKI4eBOopF4', '3tVEkHG3FyQ', 'PmVtulQfOR0', 'i2Z2TtUe9Kk',
    'hf2-6gZmFlo', 'J9YtakGpqZQ', 'bZkGoWuQ3vg',
    # Day 4
    '3ATfzId9wrM', 'jyZ1D9dP4fI', 'SP4FceXU1e4', 'EcQNRpZE7Ns'
]

with open('all_titles.txt', 'w', encoding='utf-8') as f:
    for v_id in urls:
        url = f'https://www.youtube.com/watch?v={v_id}'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            html = urllib.request.urlopen(req).read().decode('utf-8')
            m = re.search(r'<title>(.*?)</title>', html)
            if m:
                title = m.group(1).replace(' - YouTube', '').replace('&amp;', '&').replace('&#39;', "'").replace('&quot;', '"')
                f.write(f"{v_id}: {title}\n")
            else:
                f.write(f"{v_id}: Not found\n")
        except Exception as e:
            f.write(f"{v_id}: Failed: {e}\n")
