from bs4 import BeautifulSoup
from news_class import FastTG

news = FastTG()

html = news.get_html_page('https://www.mk.ru/news/')
soup = BeautifulSoup(html, 'lxml')

mass_page = soup.find('section',  class_='news-listing__day-group')
