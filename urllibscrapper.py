#disregard this code... dont use urllib
from bs4 import BeautifulSoup
import urllib.request

url = input("Enter Website url: ")
source = urllib.request.urlopen(url).read()
soup = BeautifulSoup(source, 'lxml')

print(soup.title.text)