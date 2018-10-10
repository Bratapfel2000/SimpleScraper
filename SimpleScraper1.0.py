#simple scraper with BeautifulSoup and python3.6.6

from bs4 import BeautifulSoup
import requests
import random
source = requests.get('---enter website----').text

soup = BeautifulSoup(source, 'lxml')

#also good: soup = BeautifulSoup(source, 'html.parser')



#scrapes a word from the website

#also possible to use "dev" instead of "id". in this case replace id with dev
eins = soup.find(id="---enter id or dev----")
zwei = eins.find_all(class_="---enter class title----")
drei = zwei[0]

print(drei.text)
