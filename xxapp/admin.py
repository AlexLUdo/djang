from django.contrib import admin
from .models import Vacancy, Skill, Article

# Register your models here.подключение моделей к админке

admin.site.register(Skill)

def set_unactive(modeladmin, request, queryset):
    queryset.update(is_active = False)

def set_active(modeladmin, request, queryset):
    queryset.update(is_active = True)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['art', 'ul', 'is_active']
    actions = [set_active, set_unactive]

admin.site.register(Article, ArticleAdmin)

# class VacancyAdmin(admin.ModelAdmin):
#     list_display = ['vac', 'reg', 'num',  'is_active', 'reverse_is_active']
#     actions = [set_active]

admin.site.register(Vacancy)
