import urllib.request
import re

urls = {
    '前半': 'https://www.youtube.com/playlist?list=PLoQApr14fcePHXVItDxSOBnqGC6n5GaTe',
    '後半': 'https://www.youtube.com/playlist?list=PLoQApr14fceM1VnrF1uTVceOH_56bBha0'
}

with open('playlist_titles.txt', 'w', encoding='utf-8') as f:
    for name, url in urls.items():
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            html = urllib.request.urlopen(req).read().decode('utf-8')
            titles = []
            for m in re.finditer(r'"title":\{"runs":\[\{"text":"(.*?)"\}\]', html):
                title = m.group(1).replace('\\u0026', '&')
                if title not in titles and title != "Private video" and title != "Deleted video":
                    titles.append(title)
            f.write(f"Playlist: {name}\n")
            for t in titles:
                f.write(f"- {t}\n")
            f.write("\n")
        except Exception as e:
            f.write(f"Failed {name}: {e}\n")
