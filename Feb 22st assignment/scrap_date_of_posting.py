import requests
from bs4 import BeautifulSoup
url = 'https://www.youtube.com/@PW-Foundation/videos'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
metadata = soup.find_all('div', {'class': 'style-scope ytd-grid-video-renderer'})
for i in range(5):
    video_metadata = metadata[i].find('span', {'class': 'style-scope ytd-grid-video-renderer'})
    time_of_posting = video_metadata.text.strip()
    print(time_of_posting)
