import requests
from bs4 import BeautifulSoup
url = 'https://www.youtube.com/@PW-Foundation/videos'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
thumbnails = soup.find_all('div', {'class': 'style-scope ytd-thumbnail'})
thumbnails
