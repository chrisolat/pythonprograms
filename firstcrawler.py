import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
	page = 1
	while page < max_pages:
		url = 'https://buckysroom.org/trade/search.php?page=' + str(page)
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(palin_text)
		for link in soup.find_all('a',{'class':'item-name'}):
			href = link.get('href')
			print(href)
			
trade_spider(5)