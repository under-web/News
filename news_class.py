class FastTG:
    '''Класс для работы с динамическими агрегаторами телеграма'''

    def get_news_tg(self, url='https://tgstat.ru/posts'):
        import time
        from bs4 import BeautifulSoup
        from selenium import webdriver

        try:
            driver = webdriver.Firefox(timeout=4)
            driver.get(url)
            time.sleep(3)
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

    def get_html_page(self, url, vie=False):
        """
        Возвращает html страницы
        vie - выводит в консоль результат метода
        """
        import requests
        from fake_useragent import UserAgent

        ua = UserAgent()
        fake_ua = ua.chrome
        r = requests.get(url, headers={'User-Agent': fake_ua})
        if vie:
            print(r.text)
        else:
            pass
        return r.text
# TODO: написать класс для извлечения данных из html страницы (title, time, links ) через try except
