from django.core.management.base import BaseCommand
from xxapp.models import Vacancy, Skill, Article
import requests
from bs4 import BeautifulSoup
url = 'https://3dnews.ru/news'

class Command(BaseCommand):
  def handle(self, *args, **options):
    def get_html(url):
            r = requests.get(url)
            r.encoding = 'win1251'
            return r.text

    def get_link(html):
        soup = BeautifulSoup(html, 'lxml')
        head = soup.find('div', id='section-content').find_all('a', class_="entry-header")
        for i in head:
            link = 'https://3dnews.ru' + i.get('href')
            heads= i.find('h1').string
            data = {'head': heads,
                 'link': link}
            Article.objects.create(art=data['head'], ul=data['link'])
            #print(data)
    def main():
        get_link(get_html('https://3dnews.ru/news'))
    #print('Every thing is Fine! Please look at file data.csv, Thank You so much!')

    main()

print('End')