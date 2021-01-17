from django.urls import path

from . import views

app_name = 'sondages'
urlpatterns = [
    path('index', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/resultat/', views.results, name='resultat'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]