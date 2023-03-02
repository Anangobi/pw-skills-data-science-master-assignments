import requests
from bs4 import BeautifulSoup
url = 'https://www.youtube.com/@PW-Foundation/videos'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
titles = soup.find_all('a', {'class': 'yt-simple-endpoint style-scope ytd-grid-video-renderer'})
for i in range(5):
    title = titles[i]['title']
    print(title)
