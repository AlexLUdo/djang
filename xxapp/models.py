from django.db import models

# Create your models here. для хранения моделей

class TimeStamp(models.Model):
    """
    Abstract - для нее не создаются новые таблицы
    данные хранятся в каждом наследнике
    """
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Vacancy(models.Model):

    vac = models.CharField(max_length=30, verbose_name='Вакансия')
    reg = models.CharField( max_length=30, verbose_name='Регион')
    num = models.IntegerField(blank=True, verbose_name='Количество')

    def __str__(self):
        return f'{self.vac} {self.reg}  {self.num}'


class Skill(models.Model):

    skl = models.CharField(max_length=300, verbose_name='Требуемые знания', blank=True)
    reg = models.CharField(max_length=30, verbose_name='Регион')

    def __str__(self):
        return f'{self.skl} {self.reg}'


class Article(models.Model):

    art = models.TextField(blank=True)
    ul = models.URLField(max_length=256)

    def __str__(self):
        return f'{self.art} {self.ul}'