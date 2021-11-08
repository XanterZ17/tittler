"""URL patterns for titles."""

from django.urls import path

from . import views

app_name = 'titles'
urlpatterns = [
    # Главаная
    path('', views.index, name='index'),
    # Список всех категорий
    path('titles/', views.titles_main, name='titles_main'),
    # Список аниме
    path('titles/anime/', views.anime, name='anime'),
    # Страница аниме
    path('titles/anime/<str:title_name>/', views.anime_page, name='anime_page'),
]