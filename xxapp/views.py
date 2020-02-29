from django.shortcuts import render
# from .models import Vacancy
from .forms import Vacform
# from django.core.management.base import BaseCommand
from xxapp.models import Vacancy, Skill, Article
# import requests
# from bs4 import BeautifulSoup
import requests
# import json
# import pprint

# Create your views here. логика сайта
def main_view(request):
    return render(request, 'xxapp/indext.html', context={})

def contact(request):
    return render(request, 'xxapp/address.html', context={})

def zapros(request):
    if request.method == "POST":
         form = Vacform(request.POST)
         if form.is_valid():
            vac = form.cleaned_data['vac']
            reg = form.cleaned_data['reg']
            rg = {"Москва":1, "Санкт-Петербург":2, "Россия":113,"ДРУГИЕ РЕГИОНЫ":1001,"УКРАИНА":5,"БЕЛОРУССИЯ":16,"Казахстан":40,"ЕЙСК":70}
            region = rg[reg]
            domain = 'https://api.hh.ru/'
            url = f'{domain}vacancies'
            params = {}
            params['text'] = vac
            params['area'] = region
            result = requests.get(url, params=params).json()
            all_found_vac = result['found']
            vse_stranitsy = result['found'] // 100 + 1 if result['found'] // 100 <= 20 else 20
            vse_skily = {}
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

                        if all_found_vac == False: all_found_vac = 0
                        print(vac, reg, region, all_found_vac, vse_skily)
                        skl = list({name: dict.keys for name in dict.keys(vse_skily)})
                        #skl = str(skl)
                        Vacancy.objects.create(vac=vac, reg=reg, num = all_found_vac)
                        Skill.objects.create(skl=skl, reg=reg)
                        return render(request, 'xxapp/rezultat.html', context={'vacanc': vac, 'area': reg, 'salary': all_found_vac, 'data':vse_skily})
         else:
            form = Vacform()
            return render(request, 'xxapp/zaprost.html', context={'form': form})
    else:
        form = Vacform()
        return render(request, 'xxapp/zaprost.html', context={'form': form})


def zaprosb(request):
    if request.method == "POST":
        return render(request, 'xxapp/zaprosb.html', context={})
    else:
        return render(request, 'xxapp/zaprosb.html', context={})

def rezultatb(request):
    return render(request, 'xxapp/rezultatb.html', context={})