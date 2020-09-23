import requests
from bs4 import BeautifulSoup

url = "https://gre.economist.com/gre-advice/gre-vocabulary/which-words-study/most-common-gre-vocabulary-list-organized-difficulty"
source = requests.get(url).text
soup = BeautifulSoup(source, "lxml")
gre_words = []

data = soup.find('div',class_ = "article-content")
# print(data.prettify())

for p in data.findAll('p'):
    # print(p.text.split('\n'))
    if p.find('a'):
        gre_words.append(p.a.text)

with open("Scraped_words.txt",'w+') as file:
    for i,word in enumerate(gre_words):
        file.writelines(str(i)+"  "+ word + "\n")
