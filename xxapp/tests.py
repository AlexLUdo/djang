from django.test import TestCase
from .models import Vacancy, Skill, Article
from userapp.models import XxUser
# faker - простые данные, например случайное имя
from faker import Faker
# FactoryBoy - данные для конкретной модели django
# mixer - полностью создать fake модель
from mixer.backend.django import mixer
# Create your tests here.

class VacTestCase(TestCase):
    def setUp(self):

        user = XxUser.objects.create_user(username='test_user', email='t@t.com', password='u123456789')
        self.vacancy = Vacancy.objects.create(vac='TestVacancy', reg='Piter', num='888')
        self.skill = Skill.objects.create(reg='Москва', skl='Стрессоустойчивость')
        self.art = Article.objects.create(art='Куда переехал не помню', ul='www.leningrad.spb.ru')


    def test_some_met(self):
        vacan = Vacancy.objects.get()
        self.assertEqual(vacan.some_met(), 'Who Are You?')

    def test_str(self):
            self.assertEqual(str(self.vacancy), 'TestVacancy Piter  888')

    def test_str_skl(self):
        self.assertEqual(str(self.skill), 'Стрессоустойчивость Москва')

    def test_str_art(self):
        self.assertEqual(str(self.art), 'Куда переехал не помню www.leningrad.spb.ru')