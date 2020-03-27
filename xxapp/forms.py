from django import forms
from .models import Article, Vacancy, Skill

class Vacform(forms.Form):

    vac = forms.CharField(label='Наименование вакансии:')
    reg = forms.CharField(label='В каком регионе ищем :')


class Vacforml(forms.ModelForm):
    vac = forms.CharField(label = 'Название вакансии')
    reg = forms.CharField(label = 'Название региона')
    num = forms.IntegerField(label = 'Количество вакансий')
    class Meta:
        model = Vacancy
        fields = '__all__'

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'


class ArticleForm(forms.ModelForm):
    art = forms.CharField(label = 'Название статью:')
    ul = forms.URLField(label = 'Ссылка на статью:')
    class Meta:
        model = Article
        fields = '__all__'