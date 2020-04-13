from django.db import models
from userapp.models import XxUser


# Create your models here. для хранения моделей

class ActiveManager(models.Manager):

    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(is_active=True)


class IsActiveMixin(models.Model):
    objects = models.Manager()
    active_objects = ActiveManager()
    #is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True


class TimeStamp(models.Model):
    """
    Abstract - для нее не создаются новые таблицы
    данные хранятся в каждом наследнике
    """
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Vacancy(TimeStamp, models.Model):

    vac = models.CharField(max_length=30, verbose_name='Вакансия', null = True, blank=True)
    reg = models.CharField( max_length=30, verbose_name='Регион', null = True, blank=True)
    num = models.IntegerField(verbose_name='Количество', null = True, blank=True)
    user = models.ForeignKey(XxUser, on_delete = models.CASCADE, null = True, blank=True)
    #null = True, blank=True - записать пустыми данными создаваемые поля

    def some_met(self):
        return 'Who Are You?'

    def __str__(self):
         return f'{self.vac} {self.reg}  {self.num}'

    # @classmethod
    # def create_user(cls, username, email, password):
    #     pass



class Skill(TimeStamp, models.Model):

    skl = models.CharField(max_length=300, verbose_name='Требуемые знания', null = True, blank=True)
    reg = models.CharField(max_length=30, verbose_name='Регион', null = True, blank=True)
    user = models.ForeignKey(XxUser, on_delete = models.CASCADE, null = True, blank=True)
    def __str__(self):
        return f'{self.skl} {self.reg}'


class Article(TimeStamp,  IsActiveMixin):

    art = models.TextField(blank=True,null = True)
    ul = models.URLField(max_length=256,null = True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.art} {self.ul}'