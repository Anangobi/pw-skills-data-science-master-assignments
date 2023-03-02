import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/@PW-Foundation/videos'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
videos = soup.find_all('div', {'class': 'style-scope ytd-grid-video-renderer'})

for i in range(5):
    video = videos[i]
    title_element = video.find('a', {'id': 'video-title'})
    title = title_element.text.strip()
    views_element = video.find('span', {'class': 'style-scope ytd-grid-video-renderer'})
    views = views_element.text.strip()
    print(f"{title} - {views}")
