from django import forms
from .models import Article, Vacancy, Skill

class Vacform(forms.Form):

    vac = forms.CharField(label='Наименование вакансии:')
    reg = forms.CharField(label='В каком регионе ищем :')
    class Meta:
        model = Vacancy
        # fields = '__all__'
        exclude =  ('user',)

class Vacforml(forms.ModelForm):
    vac = forms.CharField(label = 'Название вакансии')
    reg = forms.CharField(label = 'Название региона')
    num = forms.IntegerField(label = 'Количество вакансий')
    class Meta:
        model = Vacancy
        # fields = '__all__'
        exclude =  ('user',)

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        #fields = '__all__'
        exclude =  ('user',)

class ArticleForm(forms.ModelForm):
    art = forms.CharField(label = 'Название статью:')
    ul = forms.URLField(label = 'Ссылка на статью:')
    class Meta:
        model = Article
        #fields = '__all__'
        exclude =  ('user',)