from bs4 import BeautifulSoup
import requests

page = requests.get("https://sn.dk/ringsted")
# page = requests.get("https://www.cs.ucf.edu/~kstanley/neat.html")

soup = BeautifulSoup(page.content, 'html.parser')

# mydivs = soup.findAll("div", {"class": "list_news_container"})
# mydivs = soup.find_all(class_="clear")

print(soup)

# print(soup.prettify())
