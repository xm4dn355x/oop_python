# -*- coding: utf-8 -*-
########################################################################
#                                                                      #
#                                                                      #
#                                                                      #
# MIT License                                                          #
# Copyright (c) 2021 Michael Nikitenko                                 #
#                                                                      #
########################################################################


from bs4 import BeautifulSoup
import urllib.request


req = urllib.request.urlopen('https://www.ua-football.com/sport')
html = req.read()

soup = BeautifulSoup(html, 'lxml')
news = soup.find_all('li', class_='liga-news-item')

results = []

for item in news:
    title = item.find('span', class_='d-block').get_text(strip=True)
    desc = item.find('span', class_='name-dop').get_text(strip=True)
    url = item.a.get('href')
    results.append({
        'title': title,
        'desc': desc,
        'url': url,
    })


class SomeParser():
    raw_html = ''
    html = ''
    soup = BeautifulSoup()
    news = []

    def __init__(self, url: str, file_path: str):
        self.url = url
        self.file_path = file_path

    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.raw_html = req.read()
        self.html = BeautifulSoup(self.raw_html, 'lxml')

    def parse_news(self):
        news_containers = [
            {'title': 'title1', 'desc': 'desc1', 'url': 'url1'},
            {'title': 'title2', 'desc': 'desc2', 'url': 'url2'},
            {'title': 'title3', 'desc': 'desc3', 'url': 'url3'},
        ]
        for item in news_containers:
            title = item['title']
            desc = item['desc']
            url = item['url']
            self.news.append({'title': title, 'desc': desc, 'url': url})

    def run(self):
        self.get_html()
        self.parse_news()
        self.save()

    def save(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            for index, item in enumerate(self.news):
                f.write(f"Новость №{index}:\n\nЗаголовок:{item['title']}\n\nОписание: {item['desc']}\n"
                        f"Ссылка: {item['url']}\n\n")


if __name__ == '__main__':
    parser = SomeParser(url='https://www.ua-football.com/sport', file_path='result.txt')
    parser.run()
    # print(parser.raw_html)
    # print(parser.html)
    print(parser.news)
