from django import forms

class Vacform(forms.Form):

    vac = forms.CharField(label='Наименование вакансии:')
    reg = forms.CharField(label='В каком регионе ищем :')