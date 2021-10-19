from django.shortcuts import render

from .models import Anime

# Create your views here.

def index(request):
    """Главная"""
    return render(request, 'titles/index.html')


def titles_main(request):
    """Выбор категории"""
    return render(request, 'titles/titles_main.html')


def anime(request):
    """Список всего аниме в базе"""
    anime = Anime.objects.all()
    context = {'anime': anime}
    return render(request, 'titles/anime.html', context)