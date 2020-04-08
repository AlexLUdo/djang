from django.test import Client
from django.test import TestCase
from faker import Faker
from userapp.models import XxUser
from .forms import Vacforml



class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.fake = Faker()

    def test_statuses(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Что мы можем проверить
        response = self.client.get('/address/')
        self.assertEqual(response.status_code, 200)

        # # post зарос
        response = self.client.post('/vacancyc/',
                                   {'vac': self.fake.name(), 'reg': self.fake.name(),
                                    'num': 100})

        self.assertEqual(response.status_code, 302)

        # Какие данные передаются в контексте
        # response = self.client.get('/zaprosb/')
        # forml = Vacforml()
        # self.assertTrue({'form': forml} in response.context)

    def test_login_required(self):
        XxUser.objects.create_user(username='test_user', email='t@t.com', password='u123456789')

        # Он не вошел
        response = self.client.get('/vacancyc/')
        self.assertEqual(response.status_code, 302)

        # Логиним
        self.client.login(username='test_user', password='u123456789')

        response = self.client.get('/zapros/')
        self.assertEqual(response.status_code, 200)
