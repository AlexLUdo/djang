from django.db import models

# Create your models here. для хранения моделей

class Vacancy(models.Model):

    vac = models.CharField(max_length=30)
    reg = models.CharField(max_length=30)
    num = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.vac} {self.reg}  {self.num}'


class Skill(models.Model):

    skl = models.CharField(max_length=300, blank=True)
    reg = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.skl} {self.reg}'


class Article(models.Model):

    art = models.TextField(blank=True)
    ul = models.URLField(max_length=256)

    def __str__(self):
        return f'{self.art} {self.ul}'