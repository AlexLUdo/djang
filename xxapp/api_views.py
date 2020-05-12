from .models import Vacancy, Article, Skill
from .serializers import VacancySerializer, ArticleSerializer, SkillSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from .permissions import ReadOnly, IsAuthor


class VacancyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthor]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class SkillViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer