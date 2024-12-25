from django.shortcuts import render, redirect
from .forms import UserRegister
from .models import Buyer
from .models import Game, News
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import UserRegister
from .models import Buyer

def home(request):
    return render(request, 'main/home.html')


def store(request):
    # Получаем все игры из базы данных
    games = Game.objects.all()
    paginator = Paginator(games, 5)  # 5 игр на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/store.html', {'page_obj': page_obj})
    # return render(request, 'main/store.html', {'games': games})

def cart(request):
    return render(request, 'main/cart.html')

def base(request):
    return render(request, 'main/base.html')


def game_list(request):
    # Получаем все игры из базы данных
    games = Game.objects.all()

    # Передаем игры в контексте шаблона
    return render(request, 'main/game_list.html', {'games': games})

def news_list(request):
    # Получаем все новости из базы данных
    news = News.objects.all().order_by('-pub_date')
    paginator = Paginator(news, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/news.html', {'page_obj': page_obj})


def register(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            # Сохраняем нового пользователя, если форма валидна
            new_user = form.save()
            request.session['username'] = new_user.username  # Сохраняем имя в сессии
            return redirect("home")  # Перенаправление на главную страницу
        else:
            # Если форма не валидна, возвращаем ошибки
            return render(request, "main/register.html", {"form": form})

    # GET запрос: отображаем пустую форму
    form = UserRegister()
    return render(request, "main/register.html", {"form": form})


