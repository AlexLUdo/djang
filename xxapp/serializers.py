from django.conf.urls import url, include
from .models import Vacancy, Article
from rest_framework import routers, serializers, viewsets


class VacancySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        #exclude = ['update']