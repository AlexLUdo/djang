from django.core.management.base import BaseCommand
from xxapp.models import Vacancy, Skill, Article
import requests
from bs4 import BeautifulSoup
#from flask import Flask, render_template, request, abort, redirect, url_for, send_file, jsonify
import requests
import json
import pprint

domain = 'https://api.hh.ru/'
url = f'{domain}vacancies'
params = {}

class Command(BaseCommand):
  def handle(self, *args, **options):
    vacancy = (input("введите наименование вакансии :"))
    region = (input("введите номер региона :"))
    if region == '1': area = "Москва"
    if region == '2': area = "Санкт-Петербург"
    if region == '113': area = "Россия"
    params = {}
    params['text'] = vacancy
    area_query = int(region)
    params['area'] = str(area_query)
    result = requests.get(url, params=params).json()
    all_found_vac = result['found']
    vse_stranitsy = result['found'] // 100 + 1 if result['found'] // 100 <= 20 else 20
    vse_skily = {}
    kolvo = 0
    for i in range(vse_stranitsy):
        params['page'] = i
        result = requests.get(url, params=params).json()
        for j in result['items']:
            rez_tmp = requests.get(j['url']).json()
            for i in rez_tmp['key_skills']:
                if i['name'] in vse_skily:
                    vse_skily[i['name']] += 1

                else:
                    vse_skily.setdefault(i['name'], 1)
        skl = list({name: dict.keys for name in dict.keys(vse_skily)})
        skl = str(skl)
        Vacancy.objects.create(vac=vacancy, reg=area, num = all_found_vac)
        Skill.objects.create(skl=list(vse_skily), reg=area)
        print(all_found_vac, vacancy, vse_skily, area)
        print('End')
        return all_found_vac, vacancy, vse_skily, area

