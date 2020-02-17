from django.contrib import admin
from .models import Vacancy, Skill, Article

# Register your models here.подключение моделей к админке

admin.site.register(Vacancy)
admin.site.register(Skill)
admin.site.register(Article)
