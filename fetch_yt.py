import urllib.request
import re

urls = [
    "https://www.youtube.com/playlist?list=PLoQApr14fcePHXVItDxSOBnqGC6n5GaTe",
    "https://www.youtube.com/playlist?list=PLoQApr14fceM1VnrF1uTVceOH_56bBha0"
]

for url in urls:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        titles = set()
        for title in re.findall(r'"title":\{"runs":\[\{"text":"(.*?)"\}\]', html):
            if title and title != "Private video" and title != "Deleted video":
                titles.add(title)
        print(f"Playlist: {url}")
        for title in titles:
            print("- " + title)
        print()
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
