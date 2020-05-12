from django.conf.urls import url, include
from .models import Vacancy, Article, Skill
from rest_framework import routers, serializers, viewsets


class VacancySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vacancy
        exclude = ['user', 'update']
        #fields = '__all__'


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        #exclude = ['user', 'update']

class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        user = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        #user = serializers.StringRelatedField(many=True)
        model = Skill
        exclude = ['user', 'update']
        #fields = '__all__'