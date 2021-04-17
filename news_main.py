from bs4 import BeautifulSoup
from news_class import FastPostman
from news_class import Sceleton

FastPostman.get_news_tg()

html = FastPostman.get_html_page('https://www.mk.ru/news/')

soup = BeautifulSoup(html, 'lxml')
mass_page = soup.find('ul', class_='news-listing__day-list')


Sceleton.scraping_page(mass_page, 'span', 'news-listing__item-time', 'h3', 'news-listing__item-title', 'a', 'news-listing__item-link')
# print(data_page)