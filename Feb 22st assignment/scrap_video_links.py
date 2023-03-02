import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/@PW-Foundation/videos"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

video_links = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href.startswith('/watch?v='):
        video_links.append('https://www.youtube.com' + href)
        if len(video_links) == 5:
            break

for link in video_links:
    print(link)
