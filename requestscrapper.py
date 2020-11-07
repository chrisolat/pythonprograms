import requests
from bs4 import BeautifulSoup
url = input("Enter website url: ")
source_code = requests.get(url).content
#plain_text = source_code.text

#soup = BeautifulSoup(source_code, "lxml") #try xml parser

soup = BeautifulSoup(source_code, 'xml')
print(soup)