from xxapp import views
from django.urls import path

app_name = 'xxapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('address/', views.contact, name='contact'),
    path('zapros/', views.zapros, name='zapros'),
    path('base/', views.zaprosb, name='zaprosb'),
    path('vacancy/', views.VacancyView.as_view(), name='vacancyl'),
    path('vacancyc/', views.VacancyCreate.as_view(), name='vacancyc'),
    path('vac_update/<int:pk>/', views.VacancyUpd.as_view(), name='vac_update'),
    path('vac_delete/<int:pk>/', views.VacDeleteView.as_view(), name='vac_delete'),
    path('vac_det/<int:pk>/', views.VacDetailView.as_view(), name='vac_det'),
    path('article/', views.ArticleView.as_view(),  name='article'),
    path('articled/<int:pk>/', views.ArtDeleteView.as_view(),  name='art_del')
]

