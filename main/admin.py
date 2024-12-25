from django.contrib import admin
from .models import Game, Buyer, News  # Импортируем модели

# Register your models here.

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    # Отображаемые поля в списке
    list_display = ('title', 'price', 'size')
    # Поля для фильтрации
    list_filter = ('size', 'price')
    # Поле для поиска
    search_fields = ('title',)
    # Ограничение на количество записей на странице
    list_per_page = 10

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    # Отображаемые поля в списке
    list_display = ('username', 'balance', 'age')
    # Поля для фильтрации
    list_filter = ('balance', 'age')
    # Поле для поиска
    search_fields = ('username',)
    # Ограничение на количество записей на странице
    list_per_page = 10
    # Поле доступно только для чтения
    readonly_fields = ('balance',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')  # Поля для отображения в списке
    search_fields = ('title',)  # Поля для поиска
    list_filter = ('pub_date',)  # Фильтрация по дате