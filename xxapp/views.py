from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .forms import Vacform,Vacforml, ArticleForm
from xxapp.models import Vacancy, Skill, Article
import requests
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin
from django import forms

from bs4 import BeautifulSoup
@user_passes_test(lambda u: u.is_superuser)
def loadart(request):
    if request.method == "GET":
        url = 'https://3dnews.ru/news'
        r = requests.get(url)
        r.encoding = 'win1251'
        html = r.text
        soup = BeautifulSoup(html, 'lxml')
        head = soup.find('div', id='section-content').find_all('a', class_="entry-header")
        for i in head:
            link = 'https://3dnews.ru' + i.get('href')
            heads= i.find('h1').string
            data = {'head': heads,'link': link}
            Article.objects.create(art=data['head'], ul=data['link'])
        return HttpResponseRedirect(reverse('xxapp:article'))
    else:
        return HttpResponseRedirect(reverse('xxapp:article'))


# Create your views here. логика сайта
def main_view(request):
    return render(request, 'xxapp/indext.html', context={})

def contact(request):
    return render(request, 'xxapp/address.html', context={})
@login_required
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

def rezultatb(request):
    return render(request, 'xxapp/rezultatb.html', context={})

def zaprosb(request):
    if request.method == "GET":
        forml = Vacforml()
        return render(request, 'xxapp/zaprosb.html', context={'form': forml})
    else:
        forml = Vacforml(request.POST)
        if forml.is_valid():
            #Добавить в форму текущего пользователя - request.user
            forml.instance.user = request.user
            forml.save()
            return render(request, 'xxapp/vacancyl1.html', context={'forml': forml})
        else:
         return render(request, 'xxapp/zaprosb.html', context={'form': forml})


class NameContextMixin(ContextMixin):

    def get_context_data(self, *args, **kwargs):
        """
        Отвечает за передачу параметров в контекст
        :param args:
        :param kwargs:
        :return:
        """
        context = super().get_context_data(*args, **kwargs)

        context['vac'] = 'РЕДАКТИРОВАНИЕ'
        context['reg'] = 'РЕГИОН'
        context['det'] = 'ДЕТАЛИ ПО ДАННОЙ ВАКАНСИИ:'

        return context


class VacancyView(ListView, NameContextMixin):
    model = Vacancy
    fields = '__all__'
    template_name = 'vacancyl.html'
    context_object_name = 'vacs'
    def get_queryset(self):
            """
            Получение данных
            :return:
            """
            return Vacancy.objects.all()

class VacancyCreate(LoginRequiredMixin, CreateView, NameContextMixin):
    fields = ('vac','reg', 'num')
    model = Vacancy
    success_url = reverse_lazy('xxapp:vacancyl')
    template_name = 'vacancycreate.html'



    def form_valid(self, form):
        #self.request.user - текущий пользователь
        form.instance.user = self.request.user
        return super().form_valid(form)

class VacancyUpd(LoginRequiredMixin,UpdateView,NameContextMixin):
    fields = ('vac','reg', 'num')
    model = Vacancy
    context_object_name = 'vacs'
    success_url = reverse_lazy('xxapp:vacancyl')
    template_name = 'vacancycreate.html'
    def form_valid(self, form):
        #self.request.user - текущий пользователь
        form.instance.user = self.request.user
        return super().form_valid(form)

class VacDeleteView(LoginRequiredMixin,DeleteView,NameContextMixin):
    fields = '__all__'
    model = Vacancy
    context_object_name = 'vacs'
    success_url = reverse_lazy('xxapp:vacancyl')
    template_name = 'del_confirm.html'

class ArticleView(ListView,NameContextMixin):
    model = Article
    template_name = 'article.html'

class ArtDeleteView(LoginRequiredMixin,DeleteView,NameContextMixin):

    model = Article
    template_name = 'del_confirm.html'
    success_url = reverse_lazy('xxapp:article')


class VacDetailView(DetailView, NameContextMixin):
    model = Skill
    template_name = 'vac_detail.html'
    success_url = reverse_lazy('xxapp:vacancyl')
    context_object_name = 'skl'
    def get(self, request, *args, **kwargs):
        self.skill_id = kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        
        return get_object_or_404(Skill, pk=self.skill_id)

# class Load():
#     model = Article
#     template_name = 'article.html'
#     success_url = reverse_lazy('xapp:article')
#         