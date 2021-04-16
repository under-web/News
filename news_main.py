from bs4 import BeautifulSoup
from news_class import FastTG
from news_class import Sceleton
news = FastTG()

html = news.get_html_page('https://www.mk.ru/news/')
soup = BeautifulSoup(html, 'lxml')

mass_page = soup.find('section',  class_='news-listing__day-group')
data_page = Sceleton()
data_page.scraping_page(mass_page, 'span', 'news-listing__item-time', 'h3', 'news-listing__item-title', 'a', 'news-listing__item-link')
# print(data_page)