from bs4 import BeautifulSoup
import requests

# Parses the article from the simple.html.
with open('simple.html') as html_file:
	soup = BeautifulSoup(html_file, 'lxml')
article = soup.find('div', class_='article')
print(article)