class FastPostman:
    '''Класс для работы с динамическими агрегаторами телеграма'''

    @classmethod
    def get_news_tg(self, url='https://tgstat.ru/posts', pause=5):
        import time
        from bs4 import BeautifulSoup
        from selenium import webdriver

        try:
            driver = webdriver.Firefox(timeout=4)
            driver.get(url)
            time.sleep(pause)
            main_page = driver.page_source
        except ConnectionRefusedError:
            print('Проблема с соединением')
            driver.close()
            driver.quit()

        finally:
            driver.close()
            driver.quit()
        soup = BeautifulSoup(main_page, 'lxml')

        row_list = soup.find_all('div', class_='row channel')

        for i in row_list:
            try:
                title_text = i.find('a', class_='popup_ajax popup-link').text.replace('\n', '')  # текст новости
            except Exception as e:
                print(e)
                title_text = ''
            try:
                views = i.find('a', class_='popup_ajax table-link').text  # просмотры
            except Exception as e:
                print(e)
                views = ''
            try:
                time = i.find('div', class_='gray').text.strip()
            except Exception as e:
                print(e)
                time = ''
            try:
                tg_links = i.find('a').get('href')  # ссылка на канал
            except Exception as e:
                print(e)
                tg_links = ''
            print(time, '[{}]'.format(views), tg_links, title_text)

    @classmethod
    def get_html_page(self, url, vie=False):
        """
        Возвращает html страницы
        vie - выводит в консоль результат метода
        """
        import requests
        from fake_useragent import UserAgent

        ua = UserAgent()
        fake_ua = ua.chrome
        r = requests.get(url, headers={'User-Agent': fake_ua}, timeout=5)
        if vie:
            print(r.text)
        else:
            pass
        return r.text

# TODO: решить проблему с некорректным запуском методов через if или try
# TODO: отредактировать Sceleton добавить возможность сохранения в файл
# TODO: отредактировать Sceleton добавить возможность опционального выбора тегов(что парсить конкретно ссылки например)

class Sceleton:
    @classmethod
    def scraping_page(self, html, tag_time, class_time, tag_title, class_title, tag_link, class_link):
        for i in html:
            try:
                tm = i.find(tag_time, class_='{}'.format(class_time)).text
            except Exception:
                tm = ''
            try:
                tt = i.find(tag_title, class_='{}'.format(class_title)).text
            except Exception:
                tt = ''
            try:
                lk = i.find(tag_link, class_='{}'.format(class_link)).get('href')
            except Exception:
                lk = ''
            print(tm, tt, lk)
