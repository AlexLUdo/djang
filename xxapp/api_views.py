from .models import Vacancy, Article
from .serializers import VacancySerializer, ArticleSerializer
from rest_framework import viewsets


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
